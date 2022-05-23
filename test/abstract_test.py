import unittest
import requests

class AbstractTest(unittest.TestCase):
    def get_root_url(self):
        return 'http://localhost:9000/api/v1/'

    def api_call(self, method, endpoint, payload = {}, authenticated_with_default_user = False, headers = None):
        method_to_call = getattr(requests, method)

        headers = {} if headers is None else headers

        if authenticated_with_default_user is True:
            headers['x-access-tokens'] = 'tokentest123'

        return method_to_call(url=self.get_root_url() + endpoint, data = payload, headers = headers)
