import requests
from test.abstract_test import AbstractTest

class TestHometforms(AbstractTest):
    def test_home(self):
        resp = requests.get(self.get_server_url())
        data = resp.json()

        self.assertEqual({'message': 'Hello!'}, data)
