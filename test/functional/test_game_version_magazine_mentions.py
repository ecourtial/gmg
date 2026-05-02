from test.abstract_tests import AbstractTests

class TestGameVersionMagazineMentions(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('game-version-magazine-mention')
        super().check_all_routes_error_missing_user_token('game-version-magazine-mention')

    def test_get_mention(self):
        # Does not exist
        resp = self.api_call('get', 'game-version-magazine-mention/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_magazine_mention' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exists
        resp = self.api_call('get', 'game-version-magazine-mention/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'magazineIssueId': 1, 'gameVersionId': 1, 'type': 'Test', 'notes': ''}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'game-version-magazine-mention', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: magazineIssueId.', 'code': 6}, resp.json())

    def test_create_unsupported_type(self):
        resp = self.api_call('post', 'game-version-magazine-mention', {'magazineIssueId': 1, 'gameVersionId': 1, 'type': 'Review'}, True)

        self.assertEqual(400, resp.status_code)

    def test_create_magazine_issue_not_found(self):
        resp = self.api_call('post', 'game-version-magazine-mention', {'magazineIssueId': 666, 'gameVersionId': 1, 'type': 'Test'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'magazine_issue' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_create_game_version_not_found(self):
        resp = self.api_call('post', 'game-version-magazine-mention', {'magazineIssueId': 1, 'gameVersionId': 666, 'type': 'Test'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {'magazineIssueId': 1, 'gameVersionId': 1, 'type': 'Preview', 'notes': 'A preview mention.'}
        resp = self.api_call('post', 'game-version-magazine-mention', payload, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Preview', resp.json()['type'])
        mention_id = str(resp.json()['id'])

        resp = self.api_call('get', 'game-version-magazine-mention/' + mention_id, None, True)
        payload['id'] = 3
        self.assertEqual(payload, resp.json())

        # Patch
        resp = self.api_call('patch', 'game-version-magazine-mention/' + mention_id, {'notes': 'Updated.'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Updated.', resp.json()['notes'])

        # Delete
        resp = self.api_call('delete', 'game-version-magazine-mention/' + mention_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'game-version-magazine-mention/' + mention_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'game_version_magazine_mention' with id #{mention_id} has not been found.", 'code': 1}, resp.json())

    def test_update_not_found(self):
        resp = self.api_call('patch', 'game-version-magazine-mention/666', {'notes': 'Whatever'}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'game_version_magazine_mention' with id #666 has not been found.", 'code': 1}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'game-version-magazine-mentions', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_get_list_filter_by_magazine_issue(self):
        resp = self.api_call('get', 'game-version-magazine-mentions?magazineIssueId[]=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(1, resp.json()['result'][0]['id'])

    def test_get_list_filter_by_game_version(self):
        resp = self.api_call('get', 'game-version-magazine-mentions?gameVersionId[]=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
