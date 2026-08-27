from test.abstract_tests import AbstractTests

class TestGameVersionCategoryAssociations(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('game-version-category-associations')
        super().check_all_routes_error_missing_user_token('game-version-category-associations')

    def test_get_all_associations(self):
        resp = self.api_call('get', 'game-version-category-associations', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, resp.json()['resultCount'])
        self.assertEqual(3, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(1, resp.json()['result'][0]['id'])
        self.assertEqual(1, resp.json()['result'][0]['categoryId'])
        self.assertEqual(2, resp.json()['result'][0]['versionId'])
        self.assertEqual('Cool!', resp.json()['result'][0]['notes'])
        self.assertEqual('Category #1', resp.json()['result'][0]['categoryName'])
        self.assertEqual('Megadrive II', resp.json()['result'][0]['versionPlatformName'])
        self.assertEqual('Columns', resp.json()['result'][0]['gameTitle'])

    def test_get_one_association(self):
        resp = self.api_call('get', 'game-version-category-associations/1', None, True)
        self.assertEqual(200, resp.status_code)

        self.assertEqual(1, resp.json()['id'])
        self.assertEqual(1, resp.json()['categoryId'])
        self.assertEqual(2, resp.json()['versionId'])
        self.assertEqual('Cool!', resp.json()['notes'])
        self.assertEqual('Category #1', resp.json()['categoryName'])
        self.assertEqual('Megadrive II', resp.json()['versionPlatformName'])
        self.assertEqual('Columns', resp.json()['gameTitle'])

    def test_create_association_incomplete_payload(self):
        resp = self.api_call('post', 'game-version-category-associations', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: categoryId.', 'code': 6}, resp.json())    

    def test_create_duplicate_association(self):
        resp = self.api_call('post', 'game-version-category-associations', {'categoryId': 1, 'versionId': 2}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_category_association' with category id '1' already exists.", 'code': 8}, resp.json())  

    # def test_create_update_delete_category_success(self):
    #     # Create
    #     payload = {'name': 'Something', 'description': 'For those played at it in 1997.'}
    #     resp = self.api_call('post', 'game-version-categories', payload, True)

    #     self.assertEqual(200, resp.status_code)
    #     self.assertEqual('Something', resp.json()["name"])
    #     category_id = str(resp.json()["id"])

    #     resp = self.api_call('get', 'game-version-categories/' + category_id, None, True)
    #     payload['id'] = 3
    #     payload['versionCount'] = 0
    #     self.assertEqual(payload, resp.json())

    #     # Patch
    #     new_name = 'Something II - ' + category_id
    #     resp = self.api_call('patch', 'game-version-categories/' + category_id, {'name': new_name}, True)

    #     self.assertEqual(200, resp.status_code)
    #     self.assertEqual(new_name, resp.json()["name"]) 

    # #     # Delete
    #     resp = self.api_call('delete', 'game-version-categories/' + category_id, {}, True)
    #     self.assertEqual(200, resp.status_code)

    #     resp = self.api_call('delete', 'game-version-categories/' + category_id, {}, True)
    #     self.assertEqual(404, resp.status_code)
    #     self.assertEqual({'message': f"The resource of type 'game_version_category' with id #{category_id} has not been found.", 'code': 1}, resp.json()) 

    def test_update_association_duplicate_name(self):
        resp = self.api_call('patch', 'game-version-category-associations/1', {'categoryId': 2, 'versionId': 3}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_category_association' with category id '1' already exists.", 'code': 8}, resp.json())  
