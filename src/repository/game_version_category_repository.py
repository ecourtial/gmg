from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.game_version_category import GameVersionCategory
from src.entity.version import Version


class GameVersionCategoryRepository(AbstractRepository):
    entity = GameVersionCategory

    def get_select_request_start(self) -> str:
        request = f"SELECT {GameVersionCategory.table_name}.*, v.versionCount AS versionCount "
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS versionCount, {GameVersionCategory.table_name}.id AS game_id "
        request += f"      FROM {Version.table_name}, {GameVersionCategory.table_name}  "
        request += f"      WHERE {Version.table_name}.game_id = {GameVersionCategory.table_name}.{GameVersionCategory.primary_key} "
        request += f"      GROUP BY {GameVersionCategory.table_name}.{GameVersionCategory.primary_key}) AS v "
        request += f"RIGHT JOIN {GameVersionCategory.table_name} ON "
        request += f"{GameVersionCategory.table_name}.{GameVersionCategory.primary_key} = v.game_id WHERE TRUE "

        return request

    def get_by_name(self, name: str) -> GameVersionCategory | None:
        request = self.get_select_request_start() + f"AND {GameVersionCategory.table_name}.name = %s LIMIT 1;"

        return self.fetch_one(request, (name,))

    def hydrate(self, row: dict[str, Any]) -> GameVersionCategory:
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_version_count(row['versionCount'])

        return version
