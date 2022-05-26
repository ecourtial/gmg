import unittest
import requests
import json

class AbstractTest(unittest.TestCase):
    maxDiff = None
    
    def get_server_url(self):
        return 'http://localhost:9000'
    
    def get_api_root_url(self):
        return self.get_server_url() + '/api/v1/'

    def api_call(self, method, endpoint, payload = None, authenticated_with_default_user = False, headers = None):
        method_to_call = getattr(requests, method)

        payload = {} if payload is None else json.dumps(payload)
        headers = {} if headers is None else headers

        if authenticated_with_default_user is True:
            headers['x-access-tokens'] = 'tokentest123'

        headers['Content-Type'] = 'application/json'

        return method_to_call(url=self.get_api_root_url() + endpoint, data = payload, headers = headers)
