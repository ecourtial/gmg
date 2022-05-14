import unittest
import requests

class HomeTest(unittest.TestCase):
    def test_home(self):
        resp = requests.get(url='http://localhost:9000')
        data = resp.json()

        self.assertEqual({'message': 'Hello!'}, data)

if __name__ == '__main__':
    unittest.main()
