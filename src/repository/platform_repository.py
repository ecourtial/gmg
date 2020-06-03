""" Repository to handle the platforms """
from src.repository.abstract_repository import AbstractRepository
from src.entity.platform import Platform

class PlatformRepository(AbstractRepository):
    """ Another useless comment """

    def get_total_count(self):
        """The total count of platforms registered in the app."""
        request = "SELECT COUNT(*) as total FROM platforms;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_list(self):
        """The list of plaforms with their games count."""
        request = "SELECT games.platform AS platform_id, platforms.name AS platform_name, "
        request += "count(*) AS total FROM games, platforms "
        request += "WHERE games.platform = platforms.id GROUP BY platform "
        request += "UNION "
        request += "SELECT platforms.id, platforms.name AS platform_name, 0 AS total FROM platforms"
        request += " WHERE platforms.id NOT IN (SELECT DISTINCT games.platform FROM games) "
        request += "ORDER BY platform_name;"

        return self.fetch_multiple(request, ())

    def get_by_id(self, platform_id):
        """Get one support."""
        request = "SELECT platforms.id as platform_id, platforms.name as platform_name,"
        request += " count(*) as total FROM games, platforms "
        request += "WHERE games.platform = platforms.id and platforms.id = %s;"

        return self.fetch_one(request, (platform_id,))

    def insert(self, name):
        """Insert a new platform"""
        request = "INSERT INTO platforms (name) VALUES (%s)"
        self.write(request, (name,))

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Platform(row['platform_id'], row['platform_name'], row['total'])
