"""An abstract repository"""
import math

class AbstractRepository:
    """Another useless comment"""
    def __init__(self, mysql):
        self.mysql = mysql

    def fetch_one(self, request, data_tuple):
        """Fetch one result from a given request."""
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()

        if row is None:
            return None
        
        hydrated = self.hydrate(row)
        cursor.close()

        return hydrated

    def fetch_multiple(self, request, data_tuple):
        """Fetch mutliple items and return a list."""
        items_list = []
        cursor = self.mysql.cursor(dictionary=True, buffered=True)
        cursor.execute(request, data_tuple)

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            items_list.append(self.hydrate(row))

        cursor.close()
        return items_list

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row. Must be overriden"""

    def write(self, request, data, commit=True):
        """Performs an UPDATE or WRITE statement"""
        cursor = self.mysql.cursor()
        cursor.execute(request, data)

        if commit:
            self.mysql.commit()
        else:
            self.mysql.autocommit = False

        return cursor.lastrowid

    def fetch_cursor(self, request, data_tuple = None):
        """Fetch one result"""
        if (data_tuple is None):
            data_tuple = {}

        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()
        cursor.close()

        return row

    def get_object_list(self, table, page, limit):
        request = "SELECT COUNT(*) as count FROM " + table + ";"
        totalResultCount = self.fetch_cursor(request)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit;

        request = "SELECT * FROM " + table + " LIMIT " + str(limit) + " OFFSET " + str(offset)
        result = self.fetch_multiple(request, ())

        totalPageCount = int(math.ceil(totalResultCount/limit));
        totalPageCount = 1 if totalResultCount == 0 else totalPageCount

        return {
            "resultCount": len(result),
            "totalResultCount": totalResultCount,
            "page": page,
            "totalPageCount": totalPageCount,
            "result": [entry.serialize() for entry in result]
        }
