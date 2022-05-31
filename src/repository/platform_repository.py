""" Repository to handle the platforms """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.platform import Platform
from src.entity.version import Version

class PlatformRepository(AbstractRepository):
    entity = Platform

    def get_by_name(self, name):
        """Get one support by its name."""
        request = self.get_select_request_start() + "AND name = %s LIMIT 1;"

        return self.fetch_one(request, (name,))

    def get_versions_count_for_platform(self, platform_id):
        request = f"SELECT COUNT(*) as count FROM {Version.table_name} WHERE platform_id = %s"
        
        return self.fetch_cursor(request, (platform_id,))
