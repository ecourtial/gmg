from test.abstract_tests import AbstractTests

class TestGameVersionCategories(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('game-version-categories')
        super().check_all_routes_error_missing_user_token('game-version-categories')

    def test_get_all_categories(self):
        resp = self.api_call('get', 'game-version-categories', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(1, resp.json()['result'][0]['id'])
        self.assertEqual('Category #1', resp.json()['result'][0]['name'])
        self.assertEqual('Awesome games', resp.json()['result'][0]['description'])
        self.assertEqual(2, resp.json()['result'][0]['versionCount'])

    def test_get_single_category(self):
        resp = self.api_call('get', 'game-version-categories/1', None, True)
        self.assertEqual(200, resp.status_code)

        self.assertEqual(1, resp.json()['id'])
        self.assertEqual('Category #1', resp.json()['name'])
        self.assertEqual('Awesome games', resp.json()['description'])
        self.assertEqual(2, resp.json()['versionCount'])

        # Fetch all the associations for this category

        resp = self.api_call('get', 'game-version-category-associations?categoryId[]=1', None, True)

        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])

        self.assertEqual(1, resp.json()['result'][0]['id'])
        self.assertEqual(1, resp.json()['result'][0]['categoryId'])
        self.assertEqual(2, resp.json()['result'][0]['versionId'])
        self.assertEqual('Cool!', resp.json()['result'][0]['notes'])
        self.assertEqual('Category #1', resp.json()['result'][0]['categoryName'])
        self.assertEqual('Megadrive II', resp.json()['result'][0]['versionPlatformName'])
        self.assertEqual('Columns', resp.json()['result'][0]['gameTitle'])

        self.assertEqual(3, resp.json()['result'][1]['id'])
        self.assertEqual(1, resp.json()['result'][1]['categoryId'])
        self.assertEqual(4, resp.json()['result'][1]['versionId'])
        self.assertEqual(None, resp.json()['result'][1]['notes'])
        self.assertEqual('Category #1', resp.json()['result'][1]['categoryName'])
        self.assertEqual('Megadrive II', resp.json()['result'][1]['versionPlatformName'])
        self.assertEqual('Revenge Of Shinobi', resp.json()['result'][1]['gameTitle'])

    def test_create_category_incomplete_payload(self):
        resp = self.api_call('post', 'game-version-categories', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: name.', 'code': 6}, resp.json())    

    def test_create_category_duplicate_name(self):
        resp = self.api_call('post', 'game-version-categories', {'name': 'Category #2'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_category' with name 'Category #2' already exists.", 'code': 8}, resp.json())  

    def test_create_update_delete_category_success(self):
        # Create
        payload = {'name': 'Something', 'description': 'For those played at it in 1997.'}
        resp = self.api_call('post', 'game-version-categories', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Something', resp.json()["name"])
        category_id = str(resp.json()["id"])

        resp = self.api_call('get', 'game-version-categories/' + category_id, None, True)
        payload['id'] = 3
        payload['versionCount'] = 0
        self.assertEqual(payload, resp.json())

        # Patch
        new_name = 'Something II - ' + category_id
        resp = self.api_call('patch', 'game-version-categories/' + category_id, {'name': new_name}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(new_name, resp.json()["name"]) 

    #     # Delete
        resp = self.api_call('delete', 'game-version-categories/' + category_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'game-version-categories/' + category_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'game_version_category' with id #{category_id} has not been found.", 'code': 1}, resp.json()) 

    def test_update_category_duplicate_name(self):
        resp = self.api_call('patch', 'game-version-categories/2', {'name': 'Category #1'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_category' with name 'Category #1' already exists.", 'code': 8}, resp.json())  

    def test_delete_category_fails_because_has_associations(self):
        resp = self.api_call('delete', 'game-version-categories/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'game_version_category' has children of type 'version', so it cannot be deleted.", 'code': 9}, resp.json())  

        resp = self.api_call('get', 'game-version-categories/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'name': 'Category #1', 'description': 'Awesome games', 'versionCount': 2}, resp.json())
