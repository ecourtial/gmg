from src.repository.abstract_repository import AbstractRepository
from src.entity.copy import Copy
from src.entity.transaction import Transaction
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class CopyRepository(AbstractRepository):
    entity = Copy

    def get_select_request_start(self):
        request = f"SELECT {Copy.table_name}.*, v.transactionCount AS transactionCount, "
        request += f"{Game.table_name}.title AS gameTitle, {Platform.table_name}.name AS platformName " # pylint: disable=C0301
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS transactionCount, {Copy.table_name}.{Copy.primary_key} AS copy_id " # pylint: disable=C0301
        request += f"      FROM {Transaction.table_name}, {Copy.table_name}  "
        request += f"      WHERE {Transaction.table_name}.copy_id = {Copy.table_name}.{Copy.primary_key} " # pylint: disable=C0301
        request += f"      GROUP BY {Copy.table_name}.{Copy.primary_key}) AS v "
        request += f"RIGHT JOIN {Copy.table_name} ON "
        request += f"{Copy.table_name}.{Copy.primary_key} = v.copy_id, "
        request += f"{Version.table_name}, {Game.table_name}, {Platform.table_name} "
        request += f"WHERE {Copy.table_name}.version_id = {Version.table_name}.{Version.primary_key} " # pylint: disable=C0301
        request += f"AND {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} " # pylint: disable=C0301

        return request

    def hydrate(self, row):
        """Hydrate an object from a row."""
        copy = super().hydrate(row)
        copy.set_platform_name(row['platformName'])
        copy.set_game_title(row['gameTitle'])
        copy.set_transaction_count(row['transactionCount'])

        return copy
