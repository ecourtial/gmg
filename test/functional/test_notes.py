from test.abstract_tests import AbstractTests

class TestNotes(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('notes')
        super().check_all_routes_error_missing_user_token('notes')

    def test_get_note(self):
        # Does not exist
        resp = self.api_call('get', 'notes/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'note' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exist
        resp = self.api_call('get', 'notes/1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual({'id': 1, 'title': 'Note 1', 'content': 'Some comment 1.'}, resp.json())

    def test_create_incomplete_payload(self):
        resp = self.api_call('post', 'notes', {}, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: title.', 'code': 6}, resp.json())    

    def test_create_update_delete_success(self):
        # Create
        resp = self.api_call('post', 'notes', {'title': 'Genesis', 'content': 'Pues'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Genesis', resp.json()["title"])
        self.assertEqual('Pues', resp.json()["content"])
        note_id = str(resp.json()["id"])

        # Patch
        resp = self.api_call('patch', 'notes/' + note_id, {'title': 'Playstation III'}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('Playstation III', resp.json()["title"]) 

        # Delete
        resp = self.api_call('delete', 'notes/' + note_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'notes/' + note_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'note' with id #4 has not been found.", 'code': 1}, resp.json())

    def test_get_list_basic_filters(self):
        resp = self.api_call('get', 'notes?page=2&limit=1', {}, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(2, resp.json()['page'])
        self.assertEqual(2, resp.json()['totalPageCount'])

        self.assertEqual(2, resp.json()['result'][0]['id'])
        self.assertEqual('Note 2', resp.json()['result'][0]['title'])
