from test.abstract_tests_tools import AbstractTestsTools

class AbstractTests(AbstractTestsTools):
    def check_all_routes_error_missing_user_token(self, singular_endpoint, plural_endpoint):
        # get by id
        resp = self.api_call('get', singular_endpoint + '/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token', 'code': 12}, resp.json())
    
        # create
        resp = self.api_call('post', singular_endpoint)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token', 'code': 12}, resp.json())

        # patch
        resp = self.api_call('patch', singular_endpoint + '/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token', 'code': 12}, resp.json())

        # delete
        resp = self.api_call('delete', singular_endpoint + '/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token', 'code': 12}, resp.json())

        # get list
        resp = self.api_call('get', plural_endpoint)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token', 'code': 12}, resp.json())

    def check_all_routes_error_bad_user_token(self, singular_endpoint, plural_endpoint):
        headers = {'Authorization': 'token foo'}

        # get by id
        resp = self.api_call('get', singular_endpoint + '/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid', 'code': 13}, resp.json())
    
        # create
        resp = self.api_call('post', singular_endpoint, None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid', 'code': 13}, resp.json())

        # patch
        resp = self.api_call('patch', singular_endpoint + '/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid', 'code': 13}, resp.json())
        
        # delete
        resp = self.api_call('delete', singular_endpoint + '/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid', 'code': 13}, resp.json())

        # get list
        resp = self.api_call('get', plural_endpoint, None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid', 'code': 13}, resp.json())
