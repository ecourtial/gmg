from typing import Any

from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.unsupported_value_exception import UnsupportedValueException
from src.helpers.json_helper import JsonHelper


class AbstractService:  # pylint: disable=no-member
    def get_by_id(self, entity_id: int) -> Any:
        object = self.repository.get_by_id(entity_id)

        if object is None:
            raise ResourceNotFoundException(self.resource_type, entity_id)

        return object

    def insert(self, object: Any) -> Any:
        return self.repository.insert(object)

    def update(self, object: Any) -> Any:
        return self.repository.update(object)

    def validate_payload_for_creation_and_hydrate(self, object: type) -> Any:
        values: list[Any] = []
        values.append(None)

        for api_field, data in object.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)

                if 'default' in data:
                    values.append(data['default'])
                else:
                    values.append(None)
            else:
                if 'allowed_values' in data and value not in data['allowed_values']:
                    raise UnsupportedValueException(api_field, value, data['allowed_values'])

                value = self.cast_type(data, value)
                values.append(value)

        return object(*values)

    def hydrate_for_update(self, object: Any) -> None:
        for api_field, data in object.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is not None:
                if 'allowed_values' in data and value not in data['allowed_values']:
                    raise UnsupportedValueException(api_field, value, data['allowed_values'])

                method_to_call = getattr(object, 'set' + data['method'])
                value = self.cast_type(data, value)
                method_to_call(value)

    def cast_type(self, data: dict[str, Any], value: Any) -> Any:
        if data['type'] == 'int':
            try:
                value = int(value)
            except ValueError:
                value = 0

        return value
