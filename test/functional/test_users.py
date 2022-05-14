import unittest
import requests

class TestUsers(unittest.TestCase):
    def test_authentication_incomplete_payload(self):
        payload = {'email': 'foo', 'someKey': 'bar'}
        resp = requests.post(url='http://localhost:9000/api/v1/user/authenticate', data=payload)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need the email and password fields to be filled.'}, resp.json())

    def test_authentication_user_not_found(self):
        payload = {'email': 'foo', 'password': 'bar'}
        resp = requests.post(url='http://localhost:9000/api/v1/user/authenticate', data=payload)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'User not found.'}, resp.json())

    def test_creation_missing_auth_header(self):
        payload = {'email': 'foo', 'password': 'bar', 'username': 'someusername'}
        resp = requests.post(url='http://localhost:9000/api/v1/user', data=payload)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

    def test_creation_incomplete_payload(self):
        payload = {'email': 'foo', 'password': 'bar'}
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.post(url='http://localhost:9000/api/v1/user', data=payload, headers=headers)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need the email, password and username fields to be filled.'}, resp.json())

    def test_update_fails_user_not_found(self):
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.patch(url='http://localhost:9000/api/v1/user/666', headers=headers)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'User not found.'}, resp.json())

    def test_update_fails_duplicate_value(self):
        headers = {'x-access-tokens': 'tokentest123'}
        payload = {'email': 'foo@bar.com', 'password': 'barz', 'username': 'mephistophelesz', 'status': 1}
        resp = requests.patch(url='http://localhost:9000/api/v1/user/1', headers=headers, data=payload)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: email'}, resp.json())

    def test_creation_update_activate_renew_token(self):
        # Create the user
        payload = {'email': 'foo', 'password': 'bar', 'username': 'mephistopheles'}
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.post(url='http://localhost:9000/api/v1/user', data=payload, headers=headers)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(False, resp.json()["active"])
        self.assertEqual('foo', resp.json()["email"])
        self.assertEqual('mephistopheles', resp.json()["userName"])
        user_id = resp.json()["id"]

        # Try to authenticate as the new user: fail because not active by default
        payload = {'email': 'foo', 'password': 'bar'}
        resp = requests.post(url='http://localhost:9000/api/v1/user/authenticate', data=payload)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'User not found.'}, resp.json())

        # Activate the user and update all the available data
        payload = {'email': 'fooz', 'password': 'barz', 'username': 'mephistophelesz', 'status': 1}
        resp = requests.patch(url='http://localhost:9000/api/v1/user/' + str(user_id), data=payload, headers=headers)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(True, resp.json()["active"])
        self.assertEqual('fooz', resp.json()["email"])
        self.assertEqual('mephistophelesz', resp.json()["userName"])
        self.assertEqual(user_id, resp.json()["id"])

        # Try to authenticate as the new user: success
        payload = {'email': 'fooz', 'password': 'barz'}
        resp = requests.post(url='http://localhost:9000/api/v1/user/authenticate', data=payload)

        self.assertEqual(200, resp.status_code)
        token = resp.json()["token"]

        # Renew my token
        headers = {'x-access-tokens': token}
        resp = requests.post(url='http://localhost:9000/api/v1/user/renew-token', headers=headers)
        self.assertEqual(200, resp.status_code)

        self.assertEqual(True, resp.json()["active"])
        self.assertEqual('fooz', resp.json()["email"])
        self.assertEqual('mephistophelesz', resp.json()["userName"])
        self.assertEqual(user_id, resp.json()["id"])

        # Try again: fail because the token has been properly changed
        headers = {'x-access-tokens': token}
        resp = requests.post(url='http://localhost:9000/api/v1/user/renew-token', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # Try to create the same user: fail because already exist
        payload = {'email': 'fooz', 'password': 'barbar', 'username': 'mephistophelesZ'}
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.post(url='http://localhost:9000/api/v1/user', data=payload, headers=headers)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: email'}, resp.json())

    def test_get_by_filter_fails_unknown_filter(self):
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.get(url='http://localhost:9000/api/v1/user?filter=toto', headers=headers)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Unknown filter. Allowed filters are: id, email, username.'}, resp.json())

    def test_get_by_filter_no_result(self):
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.get(url='http://localhost:9000/api/v1/user?filter=username&value=toto', headers=headers)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'No user found.'}, resp.json())

    def test_get_by_filters(self):
        headers = {'x-access-tokens': 'tokentest123'}
        resp = requests.get(url='http://localhost:9000/api/v1/user?filter=username&value=Eric', headers=headers)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())

        resp = requests.get(url='http://localhost:9000/api/v1/user?filter=email&value=foo@bar.com', headers=headers)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())

        resp = requests.get(url='http://localhost:9000/api/v1/user?filter=id&value=1', headers=headers)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())


if __name__ == '__main__':
    unittest.main()
