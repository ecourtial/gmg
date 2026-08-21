from test.abstract_tests import AbstractTests

class TestGameCategories(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('game-version-categories')
        super().check_all_routes_error_missing_user_token('game-version-categories')

        super().check_all_routes_error_bad_user_token('game-version-category-associations')
        super().check_all_routes_error_missing_user_token('game-version-category-associations')

    def test_get_all_categories(self):
        resp = self.api_call('get', 'game-version-categories', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

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

# test get all associations
# test get one association

# PLUS TARD (VOIR TODO D'ABORD)
# Test CRUD
# Tests errors cases (invalid payload, duplicates...)