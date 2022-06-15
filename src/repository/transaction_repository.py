from src.repository.abstract_repository import AbstractRepository
from src.entity.transaction import Transaction
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class TransactionRepository(AbstractRepository):
    entity = Transaction

    def get_select_request_start(self):
        request = f"SELECT {Transaction.table_name}.*, {Game.table_name}.title AS gameTitle, "
        request += f"{Platform.table_name}.name AS platformName " # pylint: disable=C0301
        request += f"FROM {Transaction.table_name}, {Version.table_name}, {Game.table_name}, {Platform.table_name} " # pylint: disable=C0301
        request += f"WHERE {Transaction.table_name}.version_id = {Version.table_name}.{Version.primary_key} " # pylint: disable=C0301
        request += f"AND {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} " # pylint: disable=C0301

        return request

    def get_count_by_version(self, version_id):
        return self.fetch_cursor(
            f"SELECT COUNT(*) AS count FROM {Transaction.table_name} WHERE version_id = %s",
            (version_id,)
        )['count']

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_platform_name(row['platformName'])
        version.set_game_title(row['gameTitle'])

        return version
