from test.abstract_tests import AbstractTests

class TestPlatforms(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('platform', 'platforms')
        super().check_all_routes_error_missing_user_token('platform', 'platforms')

    def test_get_platform(self):
        # Does not exist
        resp = self.api_call('get', 'platform/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exist
        resp = self.api_call('get', 'platform/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'name': 'PC', 'versionCount': 232}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'platform', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: name.', 'code': 6}, resp.json())    

    def test_create_duplicate_name(self):
        resp = self.api_call('post', 'platform', {'name': 'PC'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform' with name 'PC' already exists.", 'code': 8}, resp.json())  

    def test_create_update_delete_success(self):
        # Create
        resp = self.api_call('post', 'platform', {'name': 'Genesis'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Genesis', resp.json()["name"])
        self.assertEqual(0, resp.json()["versionCount"])
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
        self.assertEqual({'message': "The resource of type 'platform' with id #12 has not been found.", 'code': 1}, resp.json())

    def test_update_duplicate_name(self):
        resp = self.api_call('patch', 'platform/4', {'name': 'PC'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'platform' with name 'Nintendo 64' already exists.", 'code': 8}, resp.json())  

    def test_delete_fails_because_platform_has_versions(self):
        resp = self.api_call('delete', 'platform/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message':  "The following resource type 'platform' has children of type 'version', so it cannot be deleted.", 'code': 9}, resp.json())  

        resp = self.api_call('get', 'platform/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'name': 'PC', 'versionCount': 232}, resp.json())

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

        self.assertEqual(3, resp.json()['result'][0]['id'])
        self.assertEqual('Playstation 2', resp.json()['result'][0]['name'])

        self.assertEqual(4, resp.json()['result'][1]['id'])
        self.assertEqual('Nintendo 64', resp.json()['result'][1]['name'])

    def test_filter_extra_field(self):
        resp = self.api_call('get', 'platforms?versionCount[]=10', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(8, resp.json()['result'][0]['id'])
        self.assertEqual('Saturn', resp.json()['result'][0]['name'])

        self.assertEqual(9, resp.json()['result'][1]['id'])
        self.assertEqual('Dreamcast', resp.json()['result'][1]['name'])

    def test_numerical_comparator_on_extra_field(self):
        resp = self.api_call('get', 'platforms?versionCount[]=lt-10', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, resp.json()['resultCount'])
        self.assertEqual(3, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        resp = self.api_call('get', 'platforms?versionCount[]=gt-10', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(6, resp.json()['resultCount'])
        self.assertEqual(6, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        resp = self.api_call('get', 'platforms?versionCount[]=eq-10', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        resp = self.api_call('get', 'platforms?versionCount[]=neq-10', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(9, resp.json()['resultCount'])
        self.assertEqual(9, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])


    def test_numerical_comparator_on_native_field(self):
        resp = self.api_call('get', 'platforms?id[]=neq-1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(10, resp.json()['resultCount'])
        self.assertEqual(10, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(2, resp.json()['result'][0]['id'])
        self.assertEqual('Playstation', resp.json()['result'][0]['name'])

        self.assertEqual(11, resp.json()['result'][9]['id'])
        self.assertEqual('Super Nintendo', resp.json()['result'][9]['name'])
