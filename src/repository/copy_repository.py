from src.repository.abstract_repository import AbstractRepository
from src.entity.copy import Copy
from src.entity.transaction import Transaction
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class CopyRepository(AbstractRepository):
    entity = Copy

    def get_trades_count_for_copy(self, copy_id):
        request = f"SELECT COUNT(*) as count FROM {Transaction.table_name} WHERE copy_id = %s"

        return self.fetch_cursor(request, (copy_id,))

    def get_select_request_start(self):
        request = f"SELECT {Copy.table_name}.*, {Game.table_name}.title AS gameTitle, "
        request += f"{Platform.table_name}.name AS platformName "
        request += f"FROM {Copy.table_name}, {Version.table_name}, {Game.table_name}, {Platform.table_name} " # pylint: disable=C0301
        request += f"WHERE {Copy.table_name}.copy_id = {Version.table_name}.{Version.primary_key} "
        request += f"AND {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} " # pylint: disable=C0301

        return request

    def hydrate(self, row):
        """Hydrate an object from a row."""
        copy = super().hydrate(row)
        copy.set_platform_name(row['platformName'])
        copy.set_game_title(row['gameTitle'])

        return copy
