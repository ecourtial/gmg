from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.game_version_category_repository import GameVersionCategoryRepository
from src.entity.game_version_category import GameVersionCategory
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper


class GameVersionCategoryService(AbstractService):
    resource_type = 'game_version_category'

    def __init__(self, mysql: Any) -> None:
        self.repository = GameVersionCategoryRepository(mysql)

    def get_for_create(self) -> GameVersionCategory:
        category = super().validate_payload_for_creation_and_hydrate(GameVersionCategory)

        existing_version = self.repository.get_by_name(category.get_name())

        if existing_version is not None:
            raise ResourceAlreadyExistsException(self.resource_type, category.get_name(), 'name')

        return category

    def get_for_update(self, category_id: int) -> GameVersionCategory:
        # Verification
        category = self.repository.get_by_id(category_id)

        if category_id is None:
            raise ResourceNotFoundException(self.resource_type, category_id)

        name = JsonHelper.get_value_from_request('name', category.get_name())
        existing_version = self.repository.get_by_name(name)

        if existing_version is not None and existing_version.get_id() != category.get_id():
            raise ResourceAlreadyExistsException(self.resource_type, category.get_name(), 'name')

        super().hydrate_for_update(category)

        return category

    def delete(self, category_id: int) -> bool:
        category = self.repository.get_by_id(category_id)

        if category is None:
            raise ResourceNotFoundException(self.resource_type, category_id)

        if category.get_version_count() > 0:
            raise RessourceHasChildrenException(self.resource_type, 'version')

        self.repository.delete(category_id)

        return True
