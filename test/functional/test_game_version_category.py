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
        print(resp.json())

# test get all associations
# test get one association

# PLUS TARD (VOIR TODO D'ABORD)
# Test CRUD
# Tests errors cases (invalid payload, duplicates...)