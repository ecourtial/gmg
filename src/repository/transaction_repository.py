from src.repository.abstract_repository import AbstractRepository
from src.entity.transaction import Transaction
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class TransactionRepository(AbstractRepository):
    entity = Transaction

    def get_select_request_start(self):
        request = f"SELECT {Transaction.table_name}.*, {Game.table_name}.title AS gameTitle, "
        request += f"{Platform.table_name}.name AS platformName "
        request += f"FROM {Transaction.table_name}, {Version.table_name}, {Game.table_name}, {Platform.table_name} "
        request += f"WHERE {Transaction.table_name}.version_id = {Version.table_name}.{Version.primary_key} "
        request += f"AND {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} "

        return request

    def get_count_by_version(self, version_id):
        return self.fetch_cursor(
            f"SELECT COUNT(*) AS count FROM {Transaction.table_name} WHERE version_id = %s",
            (version_id,)
        )['count']

    def reset_copy_id_for_transactions(self, copy_id, commit=True):
        self.write(f"UPDATE {Transaction.table_name} SET copy_id = NULL WHERE copy_id = %s", (copy_id,), commit)

    def get_last_transaction_for_copy(self, copy_id):
        return self.fetch_one(
            f"{self.get_select_request_start()} AND copy_id = %s ORDER BY transaction_id DESC LIMIT 1",
            (copy_id,)
        )

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_platform_name(row['platformName'])
        version.set_game_title(row['gameTitle'])

        return version
