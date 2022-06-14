from test.abstract_tests import AbstractTests

class TestTransactions(AbstractTests):
    def test_commons(self):
        super().check_all_routes_error_bad_user_token('transaction', 'transactions')
        super().check_all_routes_error_missing_user_token('transaction', 'transactions')

    def test_create_incomplete_payload(self):
        payload = {
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": ""
        }
        resp = self.api_call('post', 'transaction', payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': 'The following field is missing: copyId.', 'code': 6}, resp.json())
    
    def test_create_fails_copy_id_not_found(self):
        payload = {
            "copyId": 99999,
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": ""
        }
        resp = self.api_call('post', 'transaction', payload, True)
        
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'copy' with id #99999 has not been found.", 'code': 1}, resp.json())

    def test_create_invalid_types(self):
        payload = {
            "copyId": 99999,
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-oute",
            "notes": ""
        }

        resp = self.api_call('post', 'transaction', payload, True)
        
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The field 'type' does not support the value 'Loan-oute'. Supported values are: Bought, Loan-in, Loan-in-return, Loan-out, Loan-out-return, Sold.", 'code': 11}, resp.json())

    def test_get_transaction(self):
        # Does not exist
        resp = self.api_call('get', 'transaction/666', {}, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'transaction' with id #666 has not been found.", 'code': 1}, resp.json())

        # Exist
        resp = self.api_call('get', 'transaction/90', {}, True)

        expectedPayload = {
            "id": 90,
            "copyId": 1,
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": "",
            'gameTitle': 'Tonic Trouble',
            'platformName': 'PC',
        }

        self.assertEqual(200, resp.status_code)
        self.assertEqual(expectedPayload, resp.json())

    def test_create_update_delete_success(self):
        # Create
        payload = {
            "copyId": 2,
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": ""
        }

        resp = self.api_call('post', 'transaction', payload, True)

        self.assertEqual(200, resp.status_code)
        transaction_id = str(resp.json()["id"])
        payload['id'] = int(transaction_id)
        payload['platformName'] = resp.json()["platformName"]
        payload['gameTitle'] = resp.json()["gameTitle"]
        self.assertEqual(payload, resp.json())

        resp = self.api_call('get', 'transaction/' + str(transaction_id), None, True)
        self.assertEqual(payload, resp.json())

        # Patch
        payload = {
            "copyId": 2,
            "year": 2022,
            "month": 2,
            "day": 5,
            "type": "Loan-in",
            "notes": ""
        }

        resp = self.api_call('patch', 'transaction/' + transaction_id, payload, True)
        payload['id'] = int(transaction_id)
        payload['platformName'] = resp.json()["platformName"]
        payload['gameTitle'] = resp.json()["gameTitle"]

        self.assertEqual(200, resp.status_code)
        self.assertEqual(payload, resp.json()) 

        # Delete
        resp = self.api_call('delete', 'transaction/' + transaction_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'transaction/' + transaction_id, {}, True)
        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': f"The resource of type 'transaction' with id #{transaction_id} has not been found.", 'code': 1}, resp.json())

    def test_update_fails_because_transaction_not_found(self):
        resp = self.api_call('patch', 'transaction/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'transaction' with id #9999 has not been found.", 'code': 1}, resp.json())

    def test_update_fails_invalid_types(self):
        payload = {
            "copyId": 2,
            "year": 2022,
            "month": 2,
            "day": 5,
            "type": "Loan-ine",
            "notes": ""
        }

        resp = self.api_call('patch', 'transaction/90', payload, True)
        
        self.assertEqual(400, resp.status_code)
        self.assertEqual({'message': "The field 'type' does not support the value 'Loan-ine'. Supported values are: Bought, Loan-in, Loan-in-return, Loan-out, Loan-out-return, Sold.", 'code': 11}, resp.json())

    def test_delete_fails_because_not_found(self):
        resp = self.api_call('delete', 'transaction/9999', None, True)

        self.assertEqual(404, resp.status_code)
        self.assertEqual({'message': "The resource of type 'transaction' with id #9999 has not been found.", 'code': 1}, resp.json())

    def test_get_list_default_filters(self):
        resp = self.api_call('get', 'transactions', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(4, resp.json()['resultCount'])
        self.assertEqual(4, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

    def test_filter_single_a(self):
        resp = self.api_call('get', 'transactions?type[]=Loan-out', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(1, resp.json()['totalPageCount'])

        self.assertEqual(90, resp.json()['result'][0]['id'])
        self.assertEqual(1, resp.json()['result'][0]['copyId'])

    def test_filter_multiple(self):
        resp = self.api_call('get', 'transactions?type[]=Loan-out&orderBy[]=id-DESC&page=1&limit=1', None, True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json()['resultCount'])
        self.assertEqual(2, resp.json()['totalResultCount'])
        self.assertEqual(1, resp.json()['page'])
        self.assertEqual(2, resp.json()['totalPageCount'])

        self.assertEqual(92, resp.json()['result'][0]['id'])
        self.assertEqual(2, resp.json()['result'][0]['copyId'])

    def test_copy_status_toggle(self):
        # First, let's create a copy
        payload = {
                "versionId": 338,
                "original": True,
                "boxType": "Big box",
                "casingType": "CD",
                "onCompilation": True,
                "reedition": True,
                "hasManual": False,
                "status": "In",
                'type': 'Physical',
                "comments": "Well well well..."
        }

        resp = self.api_call('post', 'copy', payload, True)

        copy_id = str(resp.json()["id"])
        payload['id'] = int(copy_id)
        self.assertEqual('In', resp.json()['status'])

        # Next: create an outbound transaction
        tr_payload = {
            "copyId": int(copy_id),
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": "",
            'gameTitle': 'Faust',
            'platformName': 'PC',
        }

        resp = self.api_call('post', 'transaction', tr_payload, True)

        self.assertEqual(200, resp.status_code)
        tr_id = str(resp.json()["id"])
        tr_payload['id'] = int(tr_id)
        self.assertEqual(tr_payload, resp.json())

        # Now, the current copy status should be "Out"
        resp = self.api_call('get', 'copy/' + copy_id, {}, True)
        self.assertEqual('Out', resp.json()['status'])

        # If we DELETE the transaction (let's say it was a mistake to create it...)
        # The status of the copy must remain at "Out"
        resp = self.api_call('delete', 'transaction/' + tr_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('get', 'copy/' + copy_id, {}, True)
        self.assertEqual('Out', resp.json()['status'])

        # Now let's create an inbound transaction
        tr_payload = {
            "copyId": int(copy_id),
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out-return",
            "notes": ""
        }

        resp = self.api_call('post', 'transaction', tr_payload, True)

        self.assertEqual(200, resp.status_code)
        tr_id = str(resp.json()["id"])
        
        # Now, the current copy status should be "In"
        resp = self.api_call('get', 'copy/' + copy_id, {}, True)
        self.assertEqual('In', resp.json()['status'])

        # Delete for cleanup
        resp = self.api_call('delete', 'transaction/' + tr_id, {}, True)
        self.assertEqual(200, resp.status_code)

        resp = self.api_call('delete', 'copy/' + copy_id, {}, True)
        self.assertEqual(200, resp.status_code)

    def test_inconsistent_operation(self):
        # First, let's create a copy with the status to "Out"
        payload = {
                "versionId": 338,
                "original": True,
                "boxType": "Big box",
                "casingType": "CD",
                "onCompilation": True,
                "reedition": True,
                "hasManual": False,
                'type': 'Physical',
                "status": "Out",
                "comments": "Well well well..."
        }

        resp = self.api_call('post', 'copy', payload, True)

        copy_id = str(resp.json()["id"])
        payload['id'] = int(copy_id)
        self.assertEqual('Out', resp.json()['status'])

        # Now let's try to create an outbound transaction, it should fail
        tr_payload = {
            "copyId": int(copy_id),
            "year": 2022,
            "month": 2,
            "day": 4,
            "type": "Loan-out",
            "notes": ""
        }

        resp = self.api_call('post', 'transaction', tr_payload, True)

        self.assertEqual(400, resp.status_code)
        self.assertEqual("Inconsistent transaction. You tried to create a transaction of type 'Loan-out' while the copy status is 'Out'.", resp.json()['message'])

        # The current copy status should still be "Out"
        resp = self.api_call('get', 'copy/' + copy_id, {}, True)
        self.assertEqual('Out', resp.json()['status'])

        # Delete for cleanup
        resp = self.api_call('delete', 'copy/' + copy_id, {}, True)
        self.assertEqual(200, resp.status_code)
