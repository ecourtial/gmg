from test.abstract_tests import AbstractTests

class TestMagazineIssueCopies(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('magazine-issue-copy')
        super().check_all_routes_error_missing_user_token('magazine-issue-copy')

    def test_get_magazine_issue_copy(self):
        # Does not exist
        resp = self.api_call('get', 'magazine-issue-copy/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue_copy' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exists
        resp = self.api_call('get', 'magazine-issue-copy/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'magazineIssueId': 1, 'type': 'Paper', 'notes': 'Original'}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'magazine-issue-copy', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: magazineIssueId.', 'code': 6}, resp.json())

    def test_create_unsupported_type(self):
        resp = self.api_call('post', 'magazine-issue-copy', {'magazineIssueId': 1, 'type': 'Vinyl'}, True)

        self.assertEqual(400, resp.status_code)

    def test_create_magazine_issue_not_found(self):
        resp = self.api_call('post', 'magazine-issue-copy', {'magazineIssueId': 666, 'type': 'Paper'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {'magazineIssueId': 1, 'type': 'Digital', 'notes': 'Second digital copy.'}
        resp = self.api_call('post', 'magazine-issue-copy', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Digital', resp.json()['type'])
        copy_id = str(resp.json()['id'])

        resp = self.api_call('get', 'magazine-issue-copy/' + copy_id, None, True)
        payload['id'] = 3
        self.assertEqual(payload, resp.json())

        # Patch
        resp = self.api_call('patch', 'magazine-issue-copy/' + copy_id, {'notes': 'Updated note.'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Updated note.', resp.json()['notes'])

        # Delete
        resp = self.api_call('delete', 'magazine-issue-copy/' + copy_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'magazine-issue-copy/' + copy_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'magazine_issue_copy' with id #{copy_id} has not been found.", 'code': 1}, resp.json())

    def test_update_not_found(self):
        resp = self.api_call('patch', 'magazine-issue-copy/666', {'notes': 'Whatever'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue_copy' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'magazine-issue-copies', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_get_list_filter_by_magazine_issue(self):
        resp = self.api_call('get', 'magazine-issue-copies?magazineIssueId[]=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])

        resp = self.api_call('get', 'magazine-issue-copies?magazineIssueId[]=2', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(0, resp.json()['resultCount'])
