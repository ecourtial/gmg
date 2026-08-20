from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.game_version_category_association import GameVersionCategoryAssociation
from src.entity.game_version_category import GameVersionCategory
from src.entity.game_version_category_association import GameVersionCategoryAssociation
from src.entity.version import Version
from src.entity.game import Game

class GameVersionCategoryAssociationRepository(AbstractRepository):
    entity = GameVersionCategoryAssociation

    def get_select_request_start(self) -> str:
        request = f"SELECT {GameVersionCategoryAssociation.table_name}.*, {GameVersionCategory.table_name}.name AS category_name, {Version.table_name}.game_id AS game_id, {Game.table_name}.title AS game_title  "
        request += f"FROM  {GameVersionCategoryAssociation.table_name}, {GameVersionCategory.table_name}, {Version.table_name}, {Game.table_name} "
        request += f"WHERE {GameVersionCategoryAssociation.table_name}.category_id = {GameVersionCategory.table_name}.id "
        request += f"AND {Version.table_name}.version_id = {GameVersionCategoryAssociation.table_name}.version_id "
        request += f"AND game_id = {Game.table_name}.id "

        return request

    def hydrate(self, row: dict[str, Any]) -> GameVersionCategoryAssociation:
        """Hydrate an object from a row."""
        association = super().hydrate(row)
        association.set_category_name(row['category_name'])
        association.set_game_title(row['game_title'])

        return association
