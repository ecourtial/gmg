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

    def get_by_id(self, entity_id):
        """Get one support by its primary key."""
        request = f"SELECT * FROM {self.entity.table_name} "
        request += f"WHERE {self.entity.primary_key} = %s LIMIT 1;"

        return self.fetch_one(request, (entity_id,))

    def get_list(self, filters, page, limit, order_by, order):
        filter_request = ''
        values = []

        for api_field, data in self.entity.expected_fields.items():
            current_filter_values = filters.getlist(api_field + '[]')
            if 0 != len(current_filter_values):
                orRequest = ' AND ('
                for filter_value in current_filter_values:
                    if data['type']== 'int':
                        orRequest += data['field'] + f" = %s OR "
                        value_to_bind = filter_value
                    else:
                        orRequest += data['field'] + f" LIKE %s OR "
                        value_to_bind = f"%{filter_value}%"
                    
                    values.append(value_to_bind)

                length = len(orRequest)
                orRequest = orRequest[:length-3]
                orRequest += ') '
                filter_request += orRequest

    
        count_request = f"SELECT count(*) as count FROM {self.entity.table_name} WHERE version_id IS NOT NULL {filter_request}"
        totalResultCount = self.fetch_cursor(count_request, values)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit

        if order_by in self.entity.expected_fields:
            order_by = self.entity.expected_fields[order_by]['field']
        elif order_by in self.entity.authorized_extra_fields_for_filtering:
            order_by = order_by # Well, it's OK
        else:
            order_by = self.entity.primary_key
        
        if order not in ['ASC', 'DESC']:
            order = 'ASC'

        request = self.get_select_request_start() + filter_request + f" ORDER BY {order_by} {order}"
        request += " LIMIT " + str(limit) + " OFFSET " + str(offset)
        result = self.fetch_multiple(request, values)

        totalPageCount = int(math.ceil(totalResultCount/limit))
        totalPageCount = 1 if totalResultCount == 0 else totalPageCount

        return {
            "resultCount": len(result),
            "totalResultCount": totalResultCount,
            "page": page,
            "totalPageCount": totalPageCount,
            "result": [entry.serialize() for entry in result]
        }

    def insert(self, object):
        """Insert a new entry"""
        request = f"INSERT INTO {object.table_name} ("
        
        for api_field, data in object.expected_fields.items():
            request += data['field'] + ', '

        length = len(request)
        request = request[:length-2]
        request += ') VALUES ('

        for api_field, data in object.expected_fields.items():
            request += '%s, '

        length = len(request)
        request = request[:length-2]
        request += ')'
                    
        values = []
        for api_field, data in object.expected_fields.items():
            method_to_call = getattr(object, 'get' + data['method'])
            values.append(method_to_call())  

        self.write(request, values)

    def update(self, object):
        request = f"UPDATE {object.table_name} SET "

        for api_field, data in object.expected_fields.items():
            request += data['field'] + ' = %s, '

        length = len(request)
        request = request[:length-2]

        request += f" WHERE {object.primary_key} = %s"

        values = []
        for api_field, data in object.expected_fields.items():
            method_to_call = getattr(object, 'get' + data['method'])
            values.append(method_to_call())  

        values.append(object.get_id())
        self.write(request, values)
