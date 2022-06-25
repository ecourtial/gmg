class AbstractEntity: # pylint: disable=too-few-public-methods,E1101
    expected_fields = {}
    authorized_extra_fields_for_filtering = {}

    def serialize(self):
        values = {}
        values['id'] = self.get_id()

        for api_field, data in self.expected_fields.items():
            method_to_call = getattr(self, 'get' + data['method'])
            values[api_field] = method_to_call()

        return values
