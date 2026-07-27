from typing import Any


class AbstractEntity:  # pylint: disable=too-few-public-methods,E1101
    expected_fields: dict[str, Any] = {}
    authorized_extra_fields_for_filtering: dict[str, Any] = {}

    def serialize(self) -> dict[str, Any]:
        values: dict[str, Any] = {}
        values['id'] = self.get_id()

        for api_field, data in self.expected_fields.items():
            method_to_call = getattr(self, 'get' + data['method'])
            values[api_field] = method_to_call()

        return values
