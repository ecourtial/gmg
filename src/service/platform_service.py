from src.repository.platform_repository import PlatformRepository
from src.entity.platform import Platform
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class PlatformService:
    def __init__(self, mysql):
        self.platform_repository = PlatformRepository(mysql)

    def get_by_id(self, platform_id):
        platform = self.platform_repository.get_by_id(platform_id)
        
        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        return platform

    def validate_payload_for_creation_and_hydrate(self):
        values = []
        values.append(None)

        for api_field, data in Platform.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)
                else:
                    values.append(data['default'])
            else:
                values.append(value)

        platform = Platform(*values)

        existing_version = self.platform_repository.get_by_name(platform.get_name())

        if existing_version is not None:
            raise ResourceAlreadyExistsException('platform', platform.get_name(), 'name')

        return platform

    def validate_payload_for_update_and_hydrate(self, platform_id):
        # Verification
        platform = self.platform_repository.get_by_id(platform_id)

        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        name = JsonHelper.get_value_from_request('name', platform.get_name())
        existing_version = self.platform_repository.get_by_name(name)

        if existing_version is not None and existing_version.get_id() != platform.get_id():
            raise ResourceAlreadyExistsException('platform', platform.get_name(), 'name')

        # Hydratation
        for api_field, data in Platform.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is not None:
                method_to_call = getattr(platform, 'set' + data['method'])
                method_to_call(value)

        return platform

    def delete(self, platform_id):
        platform = self.platform_repository.get_by_id(platform_id)

        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        count = self.platform_repository.get_versions_count_for_platform(platform_id)['count']

        if count > 0:
            raise RessourceHasChildrenException('platform', 'version')

        self.platform_repository.delete(platform_id)

        return True
