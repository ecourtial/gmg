from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.game_version_category_association import GameVersionCategoryAssociation
from src.entity.game_version_category import GameVersionCategory
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class GameVersionCategoryAssociationRepository(AbstractRepository):
    entity = GameVersionCategoryAssociation

    def get_select_request_start(self) -> str:
        request = f"SELECT {GameVersionCategoryAssociation.table_name}.*, {GameVersionCategory.table_name}.name AS category_name, "
        request += f"{Version.table_name}.game_id AS game_id, {Game.table_name}.title AS game_title, {Platform.table_name}.id AS version_platform_id, "
        request += f"{Platform.table_name}.name AS version_platform_name "
        request += f"FROM  {GameVersionCategoryAssociation.table_name}, {GameVersionCategory.table_name}, {Version.table_name}, {Game.table_name}, {Platform.table_name} "
        request += f"WHERE {GameVersionCategoryAssociation.table_name}.category_id = {GameVersionCategory.table_name}.id "
        request += f"AND {Version.table_name}.version_id = {GameVersionCategoryAssociation.table_name}.version_id "
        request += f"AND game_id = {Game.table_name}.id "
        request += f"AND  {Platform.table_name}.id = {Version.table_name}.platform_id "

        return request

    def get_by_unique_index(self, version_id: int, category_id: int) -> Version | None:
        """Get one association by the unique combination of the version and the category."""
        request = self.get_select_request_start()
        request += f"AND {GameVersionCategoryAssociation.table_name}.category_id = %s "
        request += f"AND {GameVersionCategoryAssociation.table_name}.version_id = %s LIMIT 1;"

        return self.fetch_one(request, (category_id, version_id,))

    def hydrate(self, row: dict[str, Any]) -> GameVersionCategoryAssociation:
        """Hydrate an object from a row."""
        association = super().hydrate(row)
        association.set_category_name(row['category_name'])
        association.set_game_title(row['game_title'])
        association.set_version_platform_name(row['version_platform_name'])

        return association
