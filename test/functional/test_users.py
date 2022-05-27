from test.abstract_test import AbstractTest

class TestUsers(AbstractTest):
    def test_authentication_incomplete_payload(self):
        payload = {'email': 'foo', 'someKey': 'bar'}
        resp = self.api_call('post', 'user/authenticate', payload)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: password.'}, resp.json())

    def test_authentication_user_not_found(self):
        payload = {'email': 'foo', 'password': 'bar'}
        resp = self.api_call('post', 'user/authenticate', payload)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': "The resource of type 'user' with email 'foo' has not been found."}, resp.json())

    def test_creation_missing_auth_header(self):
        payload = {'email': 'foo', 'password': 'bar', 'username': 'someusername'}
        resp = self.api_call('post', 'user', payload)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

    def test_creation_incomplete_payload(self):
        payload = {'email': 'foo', 'password': 'bar'}
        resp = self.api_call('post', 'user', payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: username.'}, resp.json())

    def test_update_fails_user_not_found(self):
        resp = self.api_call('patch', 'user/666', {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'user' with id #666 has not been found."}, resp.json())

    def test_update_fails_duplicate_value(self):
        payload = {'email': 'foo@bar.com', 'password': 'barz', 'username': 'mephistophelesz', 'status': 1}
        resp = self.api_call('patch', 'user/1', payload, True)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'user' with email 'foo@bar.com' already exists."}, resp.json())

    def test_creation_update_activate_renew_token(self):
        # Create the user
        payload = {'email': 'foo', 'password': 'bar', 'username': 'mephistopheles'}
        resp = self.api_call('post', 'user', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(False, resp.json()["active"])
        self.assertEqual('foo', resp.json()["email"])
        self.assertEqual('mephistopheles', resp.json()["userName"])
        user_id = resp.json()["id"]

        # Try to authenticate as the new user: fail because not active by default
        payload = {'email': 'foo', 'password': 'bar'}
        resp = self.api_call('post', 'user/authenticate', payload, True)

        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'The user with email = foo is inactive.'}, resp.json())

        # Activate the user and update all the available data
        payload = {'email': 'fooz', 'password': 'barz', 'username': 'mephistophelesz', 'status': 1}
        resp = self.api_call('patch', 'user/' + str(user_id), payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(True, resp.json()["active"])
        self.assertEqual('fooz', resp.json()["email"])
        self.assertEqual('mephistophelesz', resp.json()["userName"])
        self.assertEqual(user_id, resp.json()["id"])

        # Try to authenticate as the new user: success
        payload = {'email': 'fooz', 'password': 'barz'}
        resp = self.api_call('post', 'user/authenticate', payload, True)

        self.assertEqual(200, resp.status_code)
        token = resp.json()["token"]

        # Renew my token
        resp = self.api_call('post', 'user/renew-token', payload, False, {'x-access-tokens': token})
        self.assertEqual(200, resp.status_code)

        self.assertEqual(True, resp.json()["active"])
        self.assertEqual('fooz', resp.json()["email"])
        self.assertEqual('mephistophelesz', resp.json()["userName"])
        self.assertEqual(user_id, resp.json()["id"])

        # Try again: fail because the token has been properly changed
        resp = self.api_call('post', 'user/renew-token', payload, False, {'x-access-tokens': token})
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # Try to create the same user: fail because already exist
        payload = {'email': 'fooz', 'password': 'barbar', 'username': 'mephistophelesZ'}
        resp = self.api_call('post', 'user', payload, True)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'user' with email 'fooz' already exists."}, resp.json())

    def test_get_by_filter_fails_unknown_filter(self):
        resp = self.api_call('get', 'user?filter=toto', {}, True)
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following filter is not allowed: toto. Allowed filters are: id, email, userName.'}, resp.json())

    def test_get_by_filter_no_result(self):
        resp = self.api_call('get', 'user?filter=username&value=toto', {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'user' with username 'toto' has not been found."}, resp.json())

    def test_get_by_filters(self):
        resp = self.api_call('get', 'user?filter=username&value=Eric', {}, True)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())

        resp = self.api_call('get', 'user?filter=email&value=foo@bar.com', {}, True)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())

        resp = self.api_call('get', 'user?filter=id&value=1', {}, True)
        self.assertEqual(200, resp.status_code)
        self.assertEqual({'active': True, 'email': 'foo@bar.com', 'id': 1, 'userName': 'Eric'}, resp.json())
