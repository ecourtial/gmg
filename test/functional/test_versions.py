from test.abstract_test import AbstractTest

class TestVersions(AbstractTest):
    
    def test_all_routes_error_missing_user_token(self):
        # get by id
        resp = self.api_call('get', 'version/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())
    
        # create
        resp = self.api_call('post', 'version')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # patch
        resp = self.api_call('patch', 'version/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # delete
        resp = self.api_call('delete', 'version/666')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

        # get list
        resp = self.api_call('get', 'versions')
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Missing token'}, resp.json())

    def test_all_routes_error_bad_user_token(self):
        headers = {'x-access-tokens': 'foo'}

        # get by id
        resp = self.api_call('get', 'version/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
    
        # create
        resp = self.api_call('post', 'version', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # patch
        resp = self.api_call('patch', 'version/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())
        
        # delete
        resp = self.api_call('delete', 'version/666', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

        # get list
        resp = self.api_call('get', 'versions', None, False, headers)
        self.assertEqual(403, resp.status_code)
        self.assertEqual({'message': 'Token is invalid'}, resp.json())

    def test_get_version(self):
        # Does not exist
        resp = self.api_call('get', 'version/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': 'Version not found.'}, resp.json())

        # Exist
        resp = self.api_call('get', 'version/1', {}, True)

        self.assertEqual(200, resp.status_code)
        expected_result = {
            "bestGameForever": False,
            "comments": None,
            "gameId": 1,
            "gameTitle": "Sega Soccer",
            "hallOfFame": False,
            "hallOfFamePosition": 0,
            "hallOfFameYear": 0,
            "id": 1,
            "multiplayerRecurring": False,
            "ongoing": False,
            "platformId": 7,
            "platformName": "Megadrive II",
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }

        self.assertEqual(expected_result, resp.json())

    def test_create_incomplete_payload(self):
        payload = {
            "bestGameForever": False,
            "comments": None,
            "gameId": 1,
            "hallOfFame": False,
            "hallOfFamePosition": 0,
            "hallOfFameYear": 0,
            "id": 1,
            "multiplayerRecurring": False,
            "ongoing": False,
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }
        resp = self.api_call('post', 'version', payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: platformId.'}, resp.json())
    
    def test_create_fails_platform_not_found(self):
        payload = {
            "bestGameForever": False,
            "comments": None,
            "gameId": 1,
            "hallOfFame": False,
            "hallOfFamePosition": 0,
            "hallOfFameYear": 0,
            "multiplayerRecurring": False,
            "ongoing": False,
            "platformId": 700,
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }
        resp = self.api_call('post', 'version', payload, True)
        
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform' with id #700 has not been found."}, resp.json())

    def test_create_fails_game_not_found(self):
        payload = {
            "bestGameForever": False,
            "comments": None,
            "gameId": 1000,
            "hallOfFame": False,
            "hallOfFamePosition": 0,
            "hallOfFameYear": 0,
            "multiplayerRecurring": False,
            "ongoing": False,
            "platformId": 7,
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }
        resp = self.api_call('post', 'version', payload, True)
        
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game' with id #1000 has not been found."}, resp.json())

    def test_create_fails_duplicate_platform_game_couple(self):
        payload = {
            "bestGameForever": False,
            "comments": None,
            "gameId": 1,
            "hallOfFame": False,
            "hallOfFamePosition": 0,
            "hallOfFameYear": 0,
            "multiplayerRecurring": False,
            "ongoing": False,
            "platformId": 7,
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }
        resp = self.api_call('post', 'version', payload, True)
        
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform-game couple' with id #7:1 already exists."}, resp.json())

    def test_create_update_delete_success(self):
        # Create the game
        resp = self.api_call('post', 'game', {'finished': True, 'title': 'Something'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Something', resp.json()["title"])
        game_id = str(resp.json()["id"])
        
        payload = {
            "bestGameForever": False,
            "comments": None,
            "gameId": game_id,
            'gameTitle': None,
            "hallOfFame": True,
            "hallOfFamePosition": 1,
            "hallOfFameYear": 1999,
            "id": "to_define",
            "multiplayerRecurring": False,
            "ongoing": False,
            "platformId": 7,
            "platformName": None,
            "playedItOften": True,
            "releaseYear": 0,
            "singleplayerRecurring": False,
            "toBuy": False,
            "toDo": False,
            "toDoPosition": 0,
            "toRewatch": False,
            "toWatchBackground": False,
            "toWatchPosition": 0,
            "toWatchSerious": False,
            "todoMultiplayerSometimes": False,
            "todoSoloSometimes": False,
            "todoWithHelp": False,
            "topGame": False
        }

        # Create
        resp = self.api_call('post', 'version', payload, True)

        self.assertEqual(200, resp.status_code)

        payload['id'] = int(resp.json()["id"])
        payload['comments'] = ''
        payload['gameTitle'] = 'Something'
        payload['gameId'] = int(resp.json()["gameId"])
        payload['platformName'] = 'Megadrive II'

        self.assertEqual(payload, resp.json())

        # Patch
        str_id = str(resp.json()["id"])
        str_game_id = str(resp.json()["gameId"])

        resp = self.api_call('patch', 'version/' + str_id, {'topGame': True}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(True, resp.json()["topGame"])
        self.assertEqual(False, resp.json()["todoWithHelp"])
        self.assertEqual(0, resp.json()["toWatchPosition"])

        # Delete
        resp = self.api_call('delete', 'version/' + str_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'version/' + str_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #351 has not been found."}, resp.json())

        # Remove the game too (otherwise it will pollute the DB)
        resp = self.api_call('delete', 'game/' + str_game_id, {}, True)
        self.assertEqual(200, resp.status_code)
        
    def test_update_fails_because_resource_not_found(self):
        resp = self.api_call('patch', 'version/9999', {'topGame': True}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #9999 has not been found."}, resp.json())

    def test_update_fails_because_platform_not_found(self):
        resp = self.api_call('patch', 'version/1', {'platformId': 9999}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform' with id #9999 has not been found."}, resp.json())

    def test_update_fails_because_game_not_found(self):
        resp = self.api_call('patch', 'version/1', {'gameId': 9999}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game' with id #9999 has not been found."}, resp.json())

    def test_update_fails_because_platform_game_couple_already_exist(self):
        resp = self.api_call('patch', 'version/347', {'platformId': 8, 'gameId': 377}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform-game couple' with id #377-8 already exists."}, resp.json())

    def test_delete_fails_because_not_found(self):
        resp = self.api_call('delete', 'version/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #9999 has not been found."}, resp.json())

    def test_delete_fails_because_has_copies(self):
        resp = self.api_call('delete', 'version/349', None, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'version' has children of type 'copy', so it cannot be deleted."}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'versions', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(30, resp.json()['resultCount'])
        self.assertEqual(349, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(12, resp.json()['totalPageCount'])

    def test_filter_single(self):
        resp = self.api_call('get', 'versions?hallOfFameYear[]=2008', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(1, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(85, resp.json()['result'][0]['gameId'])
        self.assertEqual('Mario Kart Wii', resp.json()['result'][0]['gameTitle'])

    def test_filter_multiple(self):
        resp = self.api_call('get', 'versions?hallOfFameYear[]=2008&hallOfFameYear[]=2012', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(85, resp.json()['result'][0]['gameId'])
        self.assertEqual('Mario Kart Wii', resp.json()['result'][0]['gameTitle'])

        self.assertEqual(201, resp.json()['result'][1]['gameId'])
        self.assertEqual('Discworld', resp.json()['result'][1]['gameTitle'])

    def test_filter_multiple_with_unknown_sorting(self):
        resp = self.api_call('get', 'versions?hallOfFameYear[]=2008&hallOfFameYear[]=2012&order_by=foo&order=bar', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(85, resp.json()['result'][0]['gameId'])
        self.assertEqual('Mario Kart Wii', resp.json()['result'][0]['gameTitle'])

        self.assertEqual(201, resp.json()['result'][1]['gameId'])
        self.assertEqual('Discworld', resp.json()['result'][1]['gameTitle'])

    def test_filter_multiple_with_custom_sorting(self):
            resp = self.api_call('get', 'versions?hallOfFameYear[]=2008&hallOfFameYear[]=2012&order_by=gameId&order=DESC', None, True)

            self.assertEqual(200, resp.status_code)
            self.assertEqual(2, resp.json()['resultCount'])
            self.assertEqual(2, resp.json()['totalResultCount'])
            self.assertEqual(1, resp.json()['page'])
            self.assertEqual(1, resp.json()['totalPageCount'])

            self.assertEqual(201, resp.json()['result'][0]['gameId'])
            self.assertEqual('Discworld', resp.json()['result'][0]['gameTitle'])

            self.assertEqual(85, resp.json()['result'][1]['gameId'])
            self.assertEqual('Mario Kart Wii', resp.json()['result'][1]['gameTitle'])

    def test_filter_multiple_with_custom_sorting_not_native_fields(self):
            resp = self.api_call('get', 'versions?hallOfFameYear[]=2008&hallOfFameYear[]=2012&order_by=platformName&order=DESC', None, True)

            self.assertEqual(200, resp.status_code)
            self.assertEqual(2, resp.json()['resultCount'])
            self.assertEqual(2, resp.json()['totalResultCount'])
            self.assertEqual(1, resp.json()['page'])
            self.assertEqual(1, resp.json()['totalPageCount'])

            self.assertEqual(85, resp.json()['result'][0]['gameId'])
            self.assertEqual('Mario Kart Wii', resp.json()['result'][0]['gameTitle'])

            self.assertEqual(201, resp.json()['result'][1]['gameId'])
            self.assertEqual('Discworld', resp.json()['result'][1]['gameTitle'])

    def test_filter_pagination_and_offset(self):
            resp = self.api_call('get', 'versions?hallOfFame[]=1&page=3', None, True)

            self.assertEqual(200, resp.status_code)
            self.assertEqual(21, resp.json()['resultCount'])
            self.assertEqual(81, resp.json()['totalResultCount'])
            self.assertEqual(3, resp.json()['page'])
            self.assertEqual(3, resp.json()['totalPageCount'])
    
    def test_filter_comments(self):
            resp = self.api_call('get', 'versions?comments[]=coop', None, True)

            self.assertEqual(200, resp.status_code)
            self.assertEqual(1, resp.json()['resultCount'])
            self.assertEqual(1, resp.json()['totalResultCount'])
            self.assertEqual(1, resp.json()['page'])
            self.assertEqual(1, resp.json()['totalPageCount'])

            self.assertEqual(376, resp.json()['result'][0]['gameId'])
            self.assertEqual('Fifa 99', resp.json()['result'][0]['gameTitle'])
