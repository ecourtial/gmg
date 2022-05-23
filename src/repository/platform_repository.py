""" Repository to handle the platforms """
from itertools import count
import math
from platform import platform
from src.repository.abstract_repository import AbstractRepository
from src.entity.platform import Platform

class PlatformRepository(AbstractRepository):
    def get_by_id(self, platform_id):
        """Get one support by its id."""
        request = "SELECT id, name FROM platforms "
        request += "WHERE id = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id,))

    def get_by_name(self, name):
        """Get one support by its name."""
        request = "SELECT id, name FROM platforms "
        request += "WHERE name = %s LIMIT 1;"

        return self.fetch_one(request, (name,))

    def insert(self, name):
        """Insert a new platform"""
        request = "INSERT INTO platforms (name) VALUES (%s)"
        self.write(request, (name,))

        return self.get_by_name(name)

    def update(self, platform):
        """Update a platform"""
        request = "UPDATE platforms SET name = %s WHERE id = %s;"
        self.write(request, (platform.get_name(), platform.get_id()))

        return self.get_by_id(platform.get_id())

    def get_versions_count_for_platform(self, platform_id):
        request = "SELECT COUNT(*) as count FROM versions WHERE platform = %s"
        
        return self.fetch_cursor(request, (platform_id,))
    
    def delete(self, platform_id):
        request = "DELETE FROM platforms WHERE id = %s"
        self.write(request, (platform_id,), True)

    def get_platforms_list(self, page, limit):
        request = "SELECT COUNT(*) as count FROM platforms;"
        totalResultCount = self.fetch_cursor(request)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit;

        request = "SELECT * FROM platforms LIMIT " + str(limit) + " OFFSET " + str(offset)
        result = self.fetch_multiple(request, ())

        totalPageCount = int(math.ceil(totalResultCount/limit));
        totalPageCount = 1 if totalResultCount == 0 else totalPageCount

        return {
            "resultCount": len(result),
            "totalResultCount": totalResultCount,
            "page": page,
            "totalPageCount": totalPageCount,
            "result": [platform.serialize() for platform in result]
        }

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Platform(row['id'], row['name'])
