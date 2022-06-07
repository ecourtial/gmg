from test.abstract_tests import AbstractTests

class TestCopies(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('story', 'stories')
        super().check_all_routes_error_missing_user_token('story', 'stories')

    def test_create_incomplete_payload(self):
        payload = {
            "year": 2022,
            "position": 1,
            "watched": True,
            "played": False
        }
        resp = self.api_call('post', 'story', payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: versionId.'}, resp.json())
    
    def test_create_fails_version_not_found(self):
        payload = {
            "versionId": 9999,
            "year": 2022,
            "position": 1,
            "watched": True,
            "played": False
        }
        resp = self.api_call('post', 'story', payload, True)
        
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #9999 has not been found."}, resp.json())

    def test_get_story(self):
        # Does not exist
        resp = self.api_call('get', 'story/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'story' with id #666 has not been found."}, resp.json())

        # Exist
        resp = self.api_call('get', 'story/2', {}, True)

        expectedPayload = {
            "id": 2,
            "versionId": 231,
            "year": 2018,
            "position": 1,
            "watched": True,
            "played": False,
            'gameTitle': 'Gabriel Knight I: Sins of The Father',
            'platformName': 'PC',
        }

        self.assertEqual(200, resp.status_code)
        self.assertEqual(expectedPayload, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {
            "versionId": 232,
            "year": 2019,
            "position": 3,
            "watched": True,
            "played": False
        }

        resp = self.api_call('post', 'story', payload, True)

        self.assertEqual(200, resp.status_code)
        story_id = str(resp.json()["id"])
        payload['id'] = int(story_id)
        payload['platformName'] = resp.json()["platformName"]
        payload['gameTitle'] = resp.json()["gameTitle"]
        self.assertEqual(payload, resp.json())

        resp = self.api_call('get', 'story/' + str(story_id), None, True)
        self.assertEqual(payload, resp.json())

        # Patch
        payload = {
            "versionId": 232,
            "year": 2019,
            "position": 4,
            "watched": True,
            "played": False
        }

        resp = self.api_call('patch', 'story/' + story_id, payload, True)
        payload['id'] = int(story_id)
        payload['platformName'] = resp.json()["platformName"]
        payload['gameTitle'] = resp.json()["gameTitle"]

        self.assertEqual(200, resp.status_code)
        self.assertEqual(payload, resp.json()) 

        # Delete
        resp = self.api_call('delete', 'story/' + story_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'story/' + story_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'story' with id #{story_id} has not been found."}, resp.json())

    def test_update_fails_because_resource_not_found(self):
        resp = self.api_call('patch', 'story/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'story' with id #9999 has not been found."}, resp.json())

    def test_delete_fails_because_not_found(self):
        resp = self.api_call('delete', 'story/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'story' with id #9999 has not been found."}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'stories', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(30, resp.json()['resultCount'])
        self.assertEqual(79, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(3, resp.json()['totalPageCount'])

    def test_filter_single_a(self):
        resp = self.api_call('get', 'stories?watched[]=1', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(30, resp.json()['resultCount'])
        self.assertEqual(61, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(3, resp.json()['totalPageCount'])

        self.assertEqual(2, resp.json()['result'][0]['id'])
        self.assertEqual(231, resp.json()['result'][0]['versionId'])

    def test_filter_multiple(self):
        resp = self.api_call('get', 'stories?&position[]=1&orderBy[]=year-DESC&page=1&limit=3', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, resp.json()['resultCount'])
        self.assertEqual(7, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(3, resp.json()['totalPageCount'])

        self.assertEqual(74, resp.json()['result'][0]['id'])
        self.assertEqual(324, resp.json()['result'][0]['versionId'])
