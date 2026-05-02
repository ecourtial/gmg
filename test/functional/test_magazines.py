from test.abstract_tests import AbstractTests

class TestMagazines(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('magazine')
        super().check_all_routes_error_missing_user_token('magazine')

    def test_get_magazine(self):
        # Does not exist
        resp = self.api_call('get', 'magazine/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exists
        resp = self.api_call('get', 'magazine/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Gen4', 'notes': 'Découvert en 1997.', 'issueCount': 2}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'magazine', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: title.', 'code': 6}, resp.json())

    def test_create_duplicate_title(self):
        resp = self.api_call('post', 'magazine', {'title': 'Gen4'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine' with title 'Gen4' already exists.", 'code': 8}, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {'title': 'Joystick', 'notes': 'French gaming magazine.'}
        resp = self.api_call('post', 'magazine', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Joystick', resp.json()['title'])
        magazine_id = str(resp.json()['id'])

        resp = self.api_call('get', 'magazine/' + magazine_id, None, True)
        payload['id'] = 3
        payload['issueCount'] = 0  # newly created, no issues yet
        self.assertEqual(payload, resp.json())

        # Patch
        new_title = 'Joystick II - ' + magazine_id
        resp = self.api_call('patch', 'magazine/' + magazine_id, {'title': new_title}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(new_title, resp.json()['title'])

        # Delete
        resp = self.api_call('delete', 'magazine/' + magazine_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'magazine/' + magazine_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'magazine' with id #{magazine_id} has not been found.", 'code': 1}, resp.json())

    def test_update_not_found(self):
        resp = self.api_call('patch', 'magazine/666', {'title': 'Whatever'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_update_duplicate_title(self):
        resp = self.api_call('patch', 'magazine/2', {'title': 'Gen4'}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine' with title 'PC PLayer' already exists.", 'code': 8}, resp.json())

    def test_delete_fails_because_magazine_has_issues(self):
        resp = self.api_call('delete', 'magazine/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'magazine' has children of type 'issue', so it cannot be deleted.", 'code': 9}, resp.json())

        resp = self.api_call('get', 'magazine/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Gen4', resp.json()['title'])

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'magazines', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_get_list_basic_filters(self):
        resp = self.api_call('get', 'magazines?page=1&limit=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(2, resp.json()['totalPageCount'])

        self.assertEqual(1, resp.json()['result'][0]['id'])
        self.assertEqual('Gen4', resp.json()['result'][0]['title'])
