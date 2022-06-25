from src.service.abstract_service import AbstractService
from src.repository.platform_repository import PlatformRepository
from src.entity.platform import Platform
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class PlatformService(AbstractService):
    resource_type = 'platform'

    def __init__(self, mysql):
        self.repository = PlatformRepository(mysql)

    def get_for_create(self):
        platform = super().validate_payload_for_creation_and_hydrate(Platform)

        existing_version = self.repository.get_by_name(platform.get_name())

        if existing_version is not None:
            raise ResourceAlreadyExistsException('platform', platform.get_name(), 'name')

        return platform

    def get_for_update(self, platform_id):
        # Verification
        platform = self.repository.get_by_id(platform_id)

        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        name = JsonHelper.get_value_from_request('name', platform.get_name())
        existing_version = self.repository.get_by_name(name)

        if existing_version is not None and existing_version.get_id() != platform.get_id():
            raise ResourceAlreadyExistsException('platform', platform.get_name(), 'name')

        super().hydrate_for_update(platform)

        return platform

    def delete(self, platform_id):
        platform = self.repository.get_by_id(platform_id)

        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        if platform.get_version_count() > 0:
            raise RessourceHasChildrenException('platform', 'version')

        self.repository.delete(platform_id)

        return True
