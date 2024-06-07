from test.abstract_tests import AbstractTests

class TestPlatforms(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('game')
        super().check_all_routes_error_missing_user_token('game')

    def test_get_game(self):
        # Does not exist
        resp = self.api_call('get', 'game/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exist
        resp = self.api_call('get', 'game/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Sega Soccer', 'notes': 'super jeu !!!', 'versionCount': 1}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'game', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: title.', 'code': 6}, resp.json())    

    def test_create_duplicate_title(self):
        resp = self.api_call('post', 'game', {'title': 'Fifa 97', 'finished': False}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game' with title 'Fifa 97' already exists.", 'code': 8}, resp.json())  

    def test_create_update_delete_success(self):
        # Create
        payload = {'title': 'Something', 'notes': 'First played at it in 1997.'}
        resp = self.api_call('post', 'game', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Something', resp.json()["title"])
        game_id = str(resp.json()["id"])

        resp = self.api_call('get', 'game/' + game_id, None, True)
        payload['id'] = 381
        payload['versionCount'] = 0
        self.assertEqual(payload, resp.json())

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
        self.assertEqual({'message': f"The resource of type 'game' with id #{game_id} has not been found.", 'code': 1}, resp.json()) 

    def test_update_duplicate_title(self):
        resp = self.api_call('patch', 'game/4', {'title': 'Fifa 97'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game' with title 'Revenge Of Shinobi' already exists.", 'code': 8}, resp.json())  

    def test_delete_fails_because_game_has_versions(self):
        resp = self.api_call('delete', 'game/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'game' has children of type 'version', so it cannot be deleted.", 'code': 9}, resp.json())  

        resp = self.api_call('get', 'game/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Sega Soccer', 'notes': 'super jeu !!!', 'versionCount': 1}, resp.json())

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

        self.assertEqual(3, resp.json()['result'][0]['id'])
        self.assertEqual('Super Monaco GP', resp.json()['result'][0]['title'])

        self.assertEqual(4, resp.json()['result'][1]['id'])
        self.assertEqual('Revenge Of Shinobi', resp.json()['result'][1]['title'])

    def test_filter_extra_field(self):
        resp = self.api_call('get', 'games?versionCount[]=gt-1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(8, resp.json()['resultCount'])
        self.assertEqual(8, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(8, resp.json()['result'][0]['id'])
        self.assertEqual('Tomb Raider', resp.json()['result'][0]['title'])
        self.assertEqual(2, resp.json()['result'][0]['versionCount'])

        self.assertEqual(287, resp.json()['result'][7]['id'])
        self.assertEqual('Tomb Raider V', resp.json()['result'][7]['title'])
        self.assertEqual(2, resp.json()['result'][7]['versionCount'])

    def test_filter_order_by_on_native_and_extra_field(self):
        resp = self.api_call('get', 'games?orderBy[]=versionCount-desc&orderBy[]=title-asc', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(30, resp.json()['resultCount'])
        self.assertEqual(341, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(12, resp.json()['totalPageCount'])

        self.assertEqual(29, resp.json()['result'][0]['id'])
        self.assertEqual('Fifa 97', resp.json()['result'][0]['title'])
        self.assertEqual(2, resp.json()['result'][0]['versionCount'])

        self.assertEqual(27, resp.json()['result'][1]['id'])
        self.assertEqual('Fifa 98', resp.json()['result'][1]['title'])
        self.assertEqual(2, resp.json()['result'][1]['versionCount'])

        self.assertEqual(373, resp.json()['result'][29]['id'])
        self.assertEqual('Anno 1602', resp.json()['result'][29]['title'])
        self.assertEqual(1, resp.json()['result'][29]['versionCount'])
