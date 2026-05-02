from test.abstract_tests import AbstractTests

class TestMagazineIssues(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('magazine-issue')
        super().check_all_routes_error_missing_user_token('magazine-issue')

    def test_get_magazine_issue(self):
        # Does not exist
        resp = self.api_call('get', 'magazine-issue/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exists
        resp = self.api_call('get', 'magazine-issue/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'magazineId': 1, 'issueNumber': 1, 'year': 1997, 'month': 8, 'notes': 'Le premier !'}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'magazine-issue', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: magazineId.', 'code': 6}, resp.json())

    def test_create_magazine_not_found(self):
        resp = self.api_call('post', 'magazine-issue', {'magazineId': 666, 'issueNumber': 1, 'year': 2000, 'month': 1}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_create_duplicate_issue_number(self):
        resp = self.api_call('post', 'magazine-issue', {'magazineId': 1, 'issueNumber': 1, 'year': 1997, 'month': 8}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with issue_number '1' already exists.", 'code': 8}, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {'magazineId': 1, 'issueNumber': 3, 'year': 1997, 'month': 10, 'notes': 'Le troisième.'}
        resp = self.api_call('post', 'magazine-issue', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, resp.json()['issueNumber'])
        issue_id = str(resp.json()['id'])

        resp = self.api_call('get', 'magazine-issue/' + issue_id, None, True)
        payload['id'] = 3
        self.assertEqual(payload, resp.json())

        # Patch
        resp = self.api_call('patch', 'magazine-issue/' + issue_id, {'notes': 'Mis à jour.'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Mis à jour.', resp.json()['notes'])

        # Delete
        resp = self.api_call('delete', 'magazine-issue/' + issue_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'magazine-issue/' + issue_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'magazine_issue' with id #{issue_id} has not been found.", 'code': 1}, resp.json())

    def test_update_not_found(self):
        resp = self.api_call('patch', 'magazine-issue/666', {'notes': 'Whatever'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_update_duplicate_issue_number(self):
        resp = self.api_call('patch', 'magazine-issue/2', {'issueNumber': 1}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with issue_number '1' already exists.", 'code': 8}, resp.json())

    def test_delete_fails_because_issue_has_copies(self):
        resp = self.api_call('delete', 'magazine-issue/1', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'magazine_issue' has children of type 'copy', so it cannot be deleted.", 'code': 9}, resp.json())

        resp = self.api_call('get', 'magazine-issue/1', {}, True)
        self.assertEqual(200, resp.status_code)

    def test_delete_fails_because_issue_has_mentions(self):
        resp = self.api_call('delete', 'magazine-issue/2', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'magazine_issue' has children of type 'game_version_magazine_mention', so it cannot be deleted.", 'code': 9}, resp.json())

        resp = self.api_call('get', 'magazine-issue/2', {}, True)
        self.assertEqual(200, resp.status_code)

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'magazine-issues', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_get_list_filter_by_magazine(self):
        resp = self.api_call('get', 'magazine-issues?magazineId[]=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])

        resp = self.api_call('get', 'magazine-issues?magazineId[]=2', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(0, resp.json()['resultCount'])
