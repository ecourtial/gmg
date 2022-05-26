from src.repository.version_repository import VersionRepository
from src.repository.platform_repository import PlatformRepository
from src.repository.game_repository import GameRepository
from src.entity.version import Version
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class VersionService:
    def __init__(self, mysql):
        self.version_repository = VersionRepository(mysql)
        self.game_repository = GameRepository(mysql)
        self.platform_repository = PlatformRepository(mysql)

    def validate_payload_for_creation_and_hydrate(self):
        values = []
        values.append(None)

        for api_field, data in Version.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)
                else:
                    values.append(data['default'])
            else:
                values.append(value)
            

        version = Version(*values)

        platform = self.platform_repository.get_by_id(version.get_platform_id())
        game = self.game_repository.get_by_id(version.get_game_id())

        if platform is None:
            raise ResourceNotFoundException('platform', version.get_platform_id())

        if game is None:
            raise ResourceNotFoundException('game', version.get_game_id())

        existing_version = self.version_repository.get_by_unique_index(version.get_platform_id(), version.get_game_id())

        if existing_version is not None:
            raise ResourceAlreadyExistsException('platform-game couple', str(version.get_platform_id()) + ':' + str(version.get_game_id()))

        return version

    def validate_payload_for_update_and_hydrate(self, version_id):
        # Verification
        version = self.version_repository.get_by_id(version_id)

        if version is None:
            raise ResourceNotFoundException('version', version_id)

        platform_id = JsonHelper.get_value_from_request('platformId', version.get_platform_id())
        game_id = JsonHelper.get_value_from_request('gameId', version.get_game_id())

        game = self.game_repository.get_by_id(game_id)
        platform = self.platform_repository.get_by_id(platform_id)

        if game is None:
            raise ResourceNotFoundException('game', game_id)

        if platform is None:
            raise ResourceNotFoundException('platform', platform_id)

        existing_version = self.version_repository.get_by_unique_index(platform_id, game_id)

        if existing_version is not None and existing_version.get_id() != version.get_id():
            raise ResourceAlreadyExistsException('platform-game couple', f"{game_id}-{platform_id}")

        # Hydratation
        for api_field, data in Version.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is not None:
                method_to_call = getattr(version, 'set' + data['method'])
                method_to_call(value)

        return version

    def delete(self, version_id):
        """Delete a version"""
        version = self.version_repository.get_by_id(version_id)

        if version is None:
            raise ResourceNotFoundException('version', version_id)

        count = self.version_repository.get_copies_count_for_version(version_id)['count']

        if count > 0:
            raise RessourceHasChildrenException('version', 'copy')

        self.version_repository.delete(version_id)

        return True
