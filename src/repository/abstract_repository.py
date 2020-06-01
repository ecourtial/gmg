from abc import ABC, abstractmethod 

class AbstractRepository:

    def __init__(self, mysql):
        self.mysql = mysql

    def fetch_one(self, request, data_tuple):
        """Fetch one result from a given request."""
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()

        if row is None:
            return None

        return self.hydrate(row)

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
        pass

    def write(self, request, data):
        cursor = self.mysql.cursor()
        cursor.execute(request, data)
        self.mysql.commit()