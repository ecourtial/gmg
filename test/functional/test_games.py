from email.header import Header
from test.abstract_test import AbstractTest

class TestPlatforms(AbstractTest):
    
    def test_all_routes_error_missing_user_token(self):
        # get by id
        resp = self.api_call('get', 'game/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())
    
        # create
        resp = self.api_call('post', 'game')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # patch
        resp = self.api_call('patch', 'game/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # delete
        resp = self.api_call('delete', 'game/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # get list
        resp = self.api_call('get', 'games')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

    def test_all_routes_error_bad_user_token(self):
        headers = {'x-access-tokens': 'foo'}

        # get by id
        resp = self.api_call('get', 'game/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
    
        # create
        resp = self.api_call('post', 'game', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # patch
        resp = self.api_call('patch', 'game/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
        
        # delete
        resp = self.api_call('delete', 'game/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # get list
        resp = self.api_call('get', 'games', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

    def test_get_game(self):
        # Does not exist
        resp = self.api_call('get', 'game/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'Game not found.'}, resp.json())

        # Exist
        resp = self.api_call('get', 'game/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Sega Soccer'}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'game', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need the title field to be filled.'}, resp.json())    

    def test_create_duplicate_title(self):
        resp = self.api_call('post', 'game', {'title': 'Fifa 97'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: title'}, resp.json())  

    def test_create_update_delete_success(self):
        # Create
        resp = self.api_call('post', 'game', {'title': 'Something'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Something', resp.json()["title"])
        game_id = str(resp.json()["id"])

        # Patch
        new_title = 'Something II - ' + game_id
        resp = self.api_call('patch', 'game/' + game_id, {'title': new_title}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(new_title, resp.json()["title"]) 

        # Delete
        resp = self.api_call('delete', 'game/' + game_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'game/' + game_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'Game not found.'}, resp.json())

    def test_update_fails_incomplete_payload(self):
        resp = self.api_call('patch', 'game/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Incomplete payload. The request need the title field to be filled.'}, resp.json())  

    def test_update_duplicate_title(self):
        resp = self.api_call('patch', 'game/4', {'title': 'Fifa 97'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field must be unique: title'}, resp.json())  

    def test_delete_fails_because_game_has_versions(self):
        resp = self.api_call('delete', 'game/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'Game has versions. Cannot delete it.'}, resp.json())  

        resp = self.api_call('get', 'game/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Sega Soccer'}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'games', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(30, resp.json()['resultCount'])
        self.assertEqual(341, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(12, resp.json()['totalPageCount'])

    def test_get_list_basic_filters(self):
        resp = self.api_call('get', 'games?page=2&limit=2', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(341, resp.json()['totalResultCount'])
        self.assertEqual(2, resp.json()['page'])
        self.assertEqual(171, resp.json()['totalPageCount'])

        self.assertEqual(146, resp.json()['result'][0]['id'])
        self.assertEqual('688 Sumarine', resp.json()['result'][0]['title'])

        self.assertEqual(135, resp.json()['result'][1]['id'])
        self.assertEqual('A-10 Tank Killer', resp.json()['result'][1]['title'])
