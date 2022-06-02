from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.unsupported_value_exception import UnsupportedValueException
from src.helpers.json_helper import JsonHelper

class AbstractService: # pylint: disable=no-member, R0201
    def get_by_id(self, entity_id):
        object = self.repository.get_by_id(entity_id)

        if object is None:
            raise ResourceNotFoundException(self.resource_type, entity_id)

        return object

    def validate_payload_for_creation_and_hydrate(self, object):
        values = []
        values.append(None)

        for api_field, data in object.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)
                values.append(data['default'])
            else:
                if 'allowed_values' in data and value not in data['allowed_values']:
                    raise UnsupportedValueException(api_field, value, data['allowed_values'])

                values.append(value)

        return object(*values)

    def hydrate_for_update(self, object):
        for api_field, data in object.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is not None:
                if 'allowed_values' in data and value not in data['allowed_values']:
                    raise UnsupportedValueException(api_field, value, data['allowed_values'])

                method_to_call = getattr(object, 'set' + data['method'])
                method_to_call(value)
