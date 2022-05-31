class AbstractEntity:
    def serialize(self):
        values = {}
        values['id'] = self.get_id()

        for api_field, data in self.expected_fields.items():
            method_to_call = getattr(self, 'get' + data['method'])
            values[api_field] = method_to_call()

        return values
