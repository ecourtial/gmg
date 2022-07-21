from test.abstract_tests import AbstractTests

class TestCopies(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('copy', 'copies')
        super().check_all_routes_error_missing_user_token('copy', 'copies')

    def test_create_incomplete_payload(self):
        payload = {
            "original": True,
            "boxType": "Big box",
            "casingType": "CD-like",
            "onCompilation": True,
            "reedition": True,
            "hasManual": False,
            "status": "In",
            "comments": "Found it somewhere"
        }
        resp = self.api_call('post', 'copy', payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: versionId.', 'code': 6}, resp.json())
    
    def test_create_fails_version_not_found(self):
        payload = {
            "versionId": 9999,
            "original": True,
            'language': 'fr',
            "boxType": "Big box",
            "casingType": "CD-like",
            'supportType': 'CD-ROM',
            "onCompilation": True,
            "reedition": True,
            "hasManual": False,
            "status": "In",
            'type': 'Physical',
            "comments": "Found it somewhere"
        }
        resp = self.api_call('post', 'copy', payload, True)
        
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'version' with id #9999 has not been found.", 'code': 1}, resp.json())

    def test_create_invalid_types(self):
        payload = {
            "versionId": 1,
            "original": True,
            'language': 'fr',
            "boxType": "Big boxe",
            "casingType": "CD-like",
            'supportType': 'CD-ROM',
            "onCompilation": True,
            "reedition": True,
            "hasManual": False,
            "status": "In",
            "comments": "Found it somewhere"
        }

        resp = self.api_call('post', 'copy', payload, True)
        
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The field 'boxType' does not support the value 'Big boxe'. Supported values are: Big box, Cartridge box, None, Other.", 'code': 11}, resp.json())

    def test_get_copy(self):
        # Does not exist
        resp = self.api_call('get', 'copy/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'copy' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exist
        resp = self.api_call('get', 'copy/1', {}, True)

        expectedPayload = {
                "id": 1,
                "versionId": 348,
                "original": True,
                'language': 'fr',
                "boxType": "Big box",
                "casingType": "CD-like",
                'supportType': 'CD-ROM',
                "onCompilation": False,
                "reedition": False,
                "hasManual": True,
                "status": "In",
                'type': 'Physical',
                "comments": "Bought it in 2004",
                'isROM': False,
                'gameTitle': 'Tonic Trouble',
                'platformName': 'PC',
                'transactionCount': 2,
        }

        self.assertEqual(200, resp.status_code)
        self.assertEqual(expectedPayload, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {
                "versionId": 348,
                "original": True,
                'language': 'fr',
                "boxType": "Big box",
                "casingType": "CD-like",
                'supportType': 'CD-ROM',
                "onCompilation": True,
                "reedition": True,
                "hasManual": False,
                "status": "In",
                'type': 'Virtual',
                "comments": "Found it somewhere",
                'gameTitle': 'Tonic Trouble',
                'platformName': 'PC',
                'transactionCount': 0
        }

        resp = self.api_call('post', 'copy', payload, True)

        self.assertEqual(200, resp.status_code)
        copy_id = str(resp.json()["id"])
        payload['id'] = int(copy_id)
        payload['isROM'] = False
        self.assertEqual(payload, resp.json())

        resp = self.api_call('get', 'copy/' + str(copy_id), None, True)
        self.assertEqual(payload, resp.json())

        # Patch
        payload = {
            "versionId": 348,
            "original": False,
            'language': 'fr',
            "boxType": "Big box",
            "casingType": "CD-like",
            'supportType': 'CD-ROM',
            "onCompilation": True,
            "reedition": True,
            "hasManual": False,
            "status": "In",
            "comments": "Found it somewhere",
            "isROM": True,
            'platformName': 'PC',
            'gameTitle': 'Tonic Trouble',
            'transactionCount': 0,
            'type': 'Physical',
        }

        resp = self.api_call('patch', 'copy/' + copy_id, payload, True)
        payload['id'] = int(copy_id)
        payload['isROM'] = True

        self.assertEqual(200, resp.status_code)
        self.assertEqual(payload, resp.json()) 

        # Delete
        resp = self.api_call('delete', 'copy/' + copy_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'copy/' + copy_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'copy' with id #{copy_id} has not been found.", 'code': 1}, resp.json())

    def test_update_fails_because_resource_not_found(self):
        resp = self.api_call('patch', 'copy/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'copy' with id #9999 has not been found.", 'code': 1}, resp.json())

    def test_update_fails_invalid_types(self):
        payload = {
            "versionId": 1,
            "original": True,
            "boxType": "Big boxe",
            "casingType": "CD-like",
            "onCompilation": True,
            "reedition": True,
            "hasManual": False,
            "status": "In",
            "comments": "Found it somewhere"
        }

        resp = self.api_call('patch', 'copy/1', payload, True)
        
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The field 'boxType' does not support the value 'Big boxe'. Supported values are: Big box, Cartridge box, None, Other.", 'code': 11}, resp.json())

    def test_delete_fails_because_not_found(self):
        resp = self.api_call('delete', 'copy/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'copy' with id #9999 has not been found.", 'code': 1}, resp.json())

    def test_delete_fails_because_has_transactions(self):
        resp = self.api_call('delete', 'copy/1', None, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The following resource type 'copy' has children of type 'transaction', so it cannot be deleted.", 'code': 9}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'copies', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, resp.json()['resultCount'])
        self.assertEqual(3, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_filter_single_a(self):
        resp = self.api_call('get', 'copies?hasManual[]=1', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(1, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(1, resp.json()['result'][0]['id'])
        self.assertEqual(348, resp.json()['result'][0]['versionId'])

    def test_filter_single_b(self):
        resp = self.api_call('get', 'copies?boxType[]=none', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(2, resp.json()['result'][0]['id'])
        self.assertEqual(349, resp.json()['result'][0]['versionId'])

    def test_filter_multiple(self):
        resp = self.api_call('get', 'copies?&original[]=1&orderBy[]=id-desc&page=1&limit=1', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(3, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(3, resp.json()['totalPageCount'])

        self.assertEqual(3, resp.json()['result'][0]['id'])
        self.assertEqual(245, resp.json()['result'][0]['versionId'])
