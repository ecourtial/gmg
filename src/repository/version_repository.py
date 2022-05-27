""" Repository to handle the versions """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.version import Version
import math

class VersionRepository(AbstractRepository):
    def get_select_request_start(self):
        request = "SELECT versions.*, games.title AS gameTitle, platforms.name AS platformName FROM versions, games, platforms "
        request += "WHERE versions.game_id = games.id "
        request += "AND versions.platform_id = platforms.id "

        return request
    
    def get_by_id(self, version_id):
        """Get one version by its id."""
        request = self.get_select_request_start() + "AND versions.version_id = %s LIMIT 1;"

        return self.fetch_one(request, (version_id,))

    def get_by_unique_index(self, platform_id, game_id):
        """Get one version by the unique combination of the platform and the game."""
        request = self.get_select_request_start()
        request += "AND versions.platform_id = %s "
        request += "AND versions.game_id = %s LIMIT 1;"

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
        request = "SELECT COUNT(*) as count FROM copies WHERE version_id = %s"
        
        return self.fetch_cursor(request, (version_id,))
    
    def delete(self, version_id):
        request = "DELETE FROM versions WHERE version_id = %s"
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
