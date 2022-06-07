""" Repository to handle the games """
from src.repository.abstract_repository import AbstractRepository
from src.entity.game import Game
from src.entity.version import Version

class GameRepository(AbstractRepository):
    entity = Game

    def get_select_request_start(self):
        request = f"SELECT {Game.table_name}.*, v.versionCount AS versionCount "
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS versionCount, {Game.table_name}.id AS game_id " # pylint: disable=C0301
        request += f"      FROM {Version.table_name}, {Game.table_name}  "
        request += f"      WHERE {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} " # pylint: disable=C0301
        request += f"      GROUP BY {Game.table_name}.{Game.primary_key}) AS v "
        request += f"RIGHT JOIN {Game.table_name} ON "
        request += f"{Game.table_name}.{Game.primary_key} = v.game_id WHERE TRUE "

        return request

    def get_by_title(self, title):
        """Get one support by its title."""
        request = self.get_select_request_start() + f"AND {Game.table_name}.title = %s LIMIT 1;"

        return self.fetch_one(request, (title,))

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_version_count(row['versionCount'])

        return version
