""" Repository to handle the versions """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform
from src.entity.copy import Copy

class VersionRepository(AbstractRepository):
    def get_select_request_start(self):
        request = f"SELECT {Version.table_name}.*, {Game.table_name}.title AS gameTitle, {Platform.table_name}.name AS platformName "
        request += f"FROM {Version.table_name}, {Game.table_name}, {Platform.table_name} "
        request += f"WHERE {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} "

        return request
    
    def get_by_id(self, version_id):
        """Get one version by its id."""
        request = self.get_select_request_start() + f"AND {Version.table_name}.{Version.primary_key} = %s LIMIT 1;"

        return self.fetch_one(request, (version_id,))

    def get_by_unique_index(self, platform_id, game_id):
        """Get one version by the unique combination of the platform and the game."""
        request = self.get_select_request_start()
        request += f"AND {Version.table_name}.platform_id = %s "
        request += f"AND {Version.table_name}.game_id = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id, game_id,))

    def insert(self, version):
        """Insert a new version"""
        super().insert(version)

        return self.get_by_unique_index(version.get_platform_id(), version.get_game_id())

    def update(self, version):
        """Update a version"""
        super().update(version)

        return self.get_by_id(version.get_id())

    def get_copies_count_for_version(self, version_id):
        request = f"SELECT COUNT(*) as count FROM {Copy.table_name} WHERE version_id = %s"
        
        return self.fetch_cursor(request, (version_id,))
    
    def delete(self, version_id):
        request = f"DELETE FROM {Version.table_name} WHERE {Version.primary_key} = %s"
        self.write(request, (version_id,), True)

    def get_list(self, filters, page, limit, order_by, order):
        return super().get_list(Version, filters, page, limit, order_by, order)

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        values = []
        values.append(row['version_id'])

        for api_field, data in Version.expected_fields.items():
            values.append(row[data['field']])

        version = Version(*values)
        version.set_platform_name(row['platformName'])
        version.set_game_title(row['gameTitle'])

        return version
