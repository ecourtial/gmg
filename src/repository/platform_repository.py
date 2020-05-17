""" Repository to handle the platforms """
from src.entity.platform import Platform

class PlatformRepository:
    """ Another useless comment """

    def __init__(self, mysql):
        self.mysql = mysql

    def get_total_count(self):
        """The total count of platforms registered in the app."""
        request = "SELECT COUNT(*) as total FROM platforms;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_list(self):
        """The list of plaforms with their games count."""
        platform_list = []
        cursor = self.mysql.cursor(dictionary=True)
        request = "SELECT games.platform AS platform_id, platforms.name AS platform_name, "
        request += "count(*) AS total FROM games, platforms "
        request += "WHERE games.platform = platforms.id GROUP BY platform "
        request += "UNION "
        request += "SELECT platforms.id, platforms.name AS platform_name, 0 AS total FROM platforms"
        request += " WHERE platforms.id NOT IN (SELECT DISTINCT games.platform FROM games) "
        request += "ORDER BY platform_name;"

        cursor.execute(request)

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            platform_list.append(self.hydrate(row))

        cursor.close()
        return platform_list

    def get_by_id(self, platform_id):
        """Get one support."""
        cursor = self.mysql.cursor(dictionary=True)
        request = "SELECT platforms.id as platform_id, platforms.name as platform_name,"
        request += " count(*) as total FROM games, platforms "
        request += "WHERE games.platform = platforms.id and platforms.id = %s;"

        data_tuple = (platform_id,)
        cursor.execute(request, data_tuple)
        return self.hydrate(cursor.fetchone())

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Platform(row['platform_id'], row['platform_name'], row['total'])
