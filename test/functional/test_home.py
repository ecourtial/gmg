import requests
from test.abstract_tests_tools import AbstractTestsTools

class TestHometforms(AbstractTestsTools):
    def test_home(self):
        resp = requests.get(self.get_server_url())
        data = resp.json()

        self.assertEqual({'message': 'Hello!'}, data)
