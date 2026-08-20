from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.game_version_category_association_repository import GameVersionCategoryAssociationRepository
from src.repository.game_version_category_repository import GameVersionCategoryRepository
from src.repository.version_repository import VersionRepository
from src.entity.game_version_category_association import GameVersionCategoryAssociation
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.helpers.json_helper import JsonHelper
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException

class GameVersionCategoryAssociationService(AbstractService):
    resource_type = 'game_version_category_association'

    def __init__(self, mysql: Any) -> None:
        self.repository = GameVersionCategoryAssociationRepository(mysql)
        self.game_version_category_repository = GameVersionCategoryRepository(mysql)
        self.version_repository = VersionRepository(mysql)

    def get_for_create(self) -> GameVersionCategoryAssociation:
        association = super().validate_payload_for_creation_and_hydrate(GameVersionCategoryAssociation)

        if self.version_repository.get_by_id(association.get_version_id()) is None:
            raise ResourceNotFoundException('version', association.get_version_id())

        if self.game_version_category_repository.get_by_id(association.get_category_id()) is None:
            raise ResourceNotFoundException('category', association.get_category_id())

        return association

    def get_for_update(self, association_id: int) -> GameVersionCategoryAssociation:
        # Verification
        association = self.repository.get_by_id(association_id)

        if association is None:
            raise ResourceNotFoundException(self.resource_type, association_id)

        version_id = JsonHelper.get_value_from_request('versionId', association.get_version_id())
        category_id = JsonHelper.get_value_from_request('categoryId', association.get_category_id())

        if self.version_repository.get_by_id(version_id) is None:
            raise ResourceNotFoundException('version', version_id)

        if self.game_version_category_repository.get_by_id(category_id) is None:
            raise ResourceNotFoundException('category', category_id)

        existing_association = self.repository.get_by_association(version_id, category_id)

        if existing_association is not None and existing_association.get_id() != association.get_id():
            raise ResourceAlreadyExistsException(self.resource_type, association.get_id(), 'version and category id')

        super().hydrate_for_update(association)

        return association


    def delete(self, association_id: int) -> bool:
        association = self.repository.get_by_id(association_id)

        if association is None:
            raise ResourceNotFoundException('category', association_id)

        self.repository.delete(association_id)

        return True
