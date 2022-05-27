""" Repository to handle the platforms """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.platform import Platform
from src.entity.version import Version

class PlatformRepository(AbstractRepository):
    def get_by_id(self, platform_id):
        """Get one support by its id."""
        request = f"SELECT * FROM {Platform.table_name} "
        request += f"WHERE {Platform.primary_key} = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id,))

    def get_by_name(self, name):
        """Get one support by its name."""
        request = f"SELECT * FROM {Platform.table_name} "
        request += f"WHERE name = %s LIMIT 1;"

        return self.fetch_one(request, (name,))

    def insert(self, platform):
        super().insert(platform)

        return self.get_by_name(platform.get_name())

    def update(self, platform):
        super().update(platform)

        return self.get_by_id(platform.get_id())

    def get_versions_count_for_platform(self, platform_id):
        request = f"SELECT COUNT(*) as count FROM {Version.table_name} WHERE platform_id = %s"
        
        return self.fetch_cursor(request, (platform_id,))
    
    def delete(self, platform_id):
        request = f"DELETE FROM {Platform.table_name} WHERE id = %s"
        self.write(request, (platform_id,), True)

    def get_list(self, page, limit):
        return self.get_object_list('platforms', page, limit)

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Platform(row['id'], row['name'])
