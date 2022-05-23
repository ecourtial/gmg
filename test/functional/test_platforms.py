from test.abstract_test import AbstractTest
import requests

class TestPlatforms(AbstractTest):
    
    def test_all_routes_error_missing_user_token(self):
        # get by id
        resp = self.api_call('get', 'platform/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())
    
        # create
        resp = self.api_call('post', 'platform')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # patch
        resp = self.api_call('patch', 'platform/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # delete
        resp = self.api_call('delete', 'platform/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # get list
        resp = self.api_call('get', 'platforms')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

    def test_all_routes_error_bad_user_token(self):
        headers = {'x-access-tokens': 'foo'}

        # get by id
        resp = requests.get(url=self.get_root_url()+'platform/666', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
    
        # create
        resp = requests.post(url=self.get_root_url()+'platform', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # patch
        resp = requests.patch(url=self.get_root_url()+'platform/666', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
        
        # delete
        resp = requests.delete(url=self.get_root_url()+'platform/666', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # get list
        resp = requests.get(url=self.get_root_url()+'platforms', headers=headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

    def test_get_platform(self):
        # Does not exist
        resp = self.api_call('get', 'platform/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'Platform not found.'}, resp.json())

        # Exist
        resp = self.api_call('get', 'platform/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'name': 'PC'}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'platform', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need name field to be filled.'}, resp.json())    

    def test_create_duplicate_name(self):
        resp = self.api_call('post', 'platform', {'name': 'PC'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: name'}, resp.json())  

    def test_create_update_delete_success(self):
        # Create
        resp = self.api_call('post', 'platform', {'name': 'Genesis'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Genesis', resp.json()["name"])
        platform_id = str(resp.json()["id"])

        # Patch
        resp = self.api_call('patch', 'platform/' + platform_id, {'name': 'Playstation III'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Playstation III', resp.json()["name"]) 

        # Delete
        resp = self.api_call('delete', 'platform/' + platform_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'platform/' + platform_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'Platform not found.'}, resp.json())

    def test_update_fails_incomplete_payload(self):
        resp = self.api_call('patch', 'platform/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need name field to be filled.'}, resp.json())  

    def test_update_duplicate_name(self):
        resp = self.api_call('patch', 'platform/4', {'name': 'PC'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: name'}, resp.json())  

    def test_delete_fails_because_platform_has_versions(self):
        resp = self.api_call('delete', 'platform/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Platform has games. Cannot delete it.'}, resp.json())  

        resp = self.api_call('get', 'platform/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'name': 'PC'}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'platforms', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(11, resp.json()['resultCount'])
        self.assertEqual(11, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_get_list_basic_filters(self):
        resp = self.api_call('get', 'platforms?page=2&limit=2', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(11, resp.json()['totalResultCount'])
        self.assertEqual(2, resp.json()['page'])
        self.assertEqual(6, resp.json()['totalPageCount'])

        self.assertEqual(5, resp.json()['result'][0]['id'])
        self.assertEqual('GameCube', resp.json()['result'][0]['name'])

        self.assertEqual(7, resp.json()['result'][1]['id'])
        self.assertEqual('Megadrive II', resp.json()['result'][1]['name'])
