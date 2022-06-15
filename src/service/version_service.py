from src.service.abstract_service import AbstractService
from src.repository.version_repository import VersionRepository
from src.repository.platform_repository import PlatformRepository
from src.repository.game_repository import GameRepository
from src.repository.transaction_repository import TransactionRepository
from src.entity.version import Version
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class VersionService(AbstractService):
    resource_type = 'version'

    def __init__(self, mysql):
        self.repository = VersionRepository(mysql)
        self.game_repository = GameRepository(mysql)
        self.platform_repository = PlatformRepository(mysql)
        self.transaction_repository = TransactionRepository(mysql)

    def get_for_create(self):
        version = super().validate_payload_for_creation_and_hydrate(Version)

        platform = self.platform_repository.get_by_id(version.get_platform_id())
        game = self.game_repository.get_by_id(version.get_game_id())

        if platform is None:
            raise ResourceNotFoundException('platform', version.get_platform_id())

        if game is None:
            raise ResourceNotFoundException('game', version.get_game_id())

        existing_version = self.repository.get_by_unique_index(
            version.get_platform_id(),
            version.get_game_id()
        )

        if existing_version is not None:
            raise ResourceAlreadyExistsException(
                'platform-game couple',
                str(version.get_platform_id()) + ':' + str(version.get_game_id())
            )

        return version

    def get_for_update(self, version_id):
        # Verification
        version = self.repository.get_by_id(version_id)

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

        existing_version = self.repository.get_by_unique_index(platform_id, game_id)

        if existing_version is not None and existing_version.get_id() != version.get_id():
            raise ResourceAlreadyExistsException('platform-game couple', f"{game_id}-{platform_id}")

        # Hydratation
        super().hydrate_for_update(version)

        return version

    def delete(self, version_id):
        """Delete a version"""
        version = self.repository.get_by_id(version_id)

        if version is None:
            raise ResourceNotFoundException('version', version_id)

        if version.get_story_count() > 0:
            raise RessourceHasChildrenException('version', 'story')

        if version.get_copy_count() > 0:
            raise RessourceHasChildrenException('version', 'copy')

        # Note (TODO): use an alias in the query instead (as above)
        if self.transaction_repository.get_count_by_version(version_id) > 0:
            raise RessourceHasChildrenException('version', 'transaction')

        self.repository.delete(version_id)

        return True
