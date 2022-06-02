"""An abstract repository"""
import math

class AbstractRepository:# pylint: disable=no-member
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

    def hydrate(self, row):
        """Hydrate an object from a row."""
        values = []
        values.append(row[self.entity.primary_key])

        for api_field, data in self.entity.expected_fields.items():# pylint: disable=W0612
            values.append(row[data['field']])

        object = self.entity(*values)

        return object

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
        if data_tuple is None:
            data_tuple = {}

        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()
        cursor.close()

        return row

    def get_by_id(self, entity_id):
        """Get one support by its primary key."""
        request = self.get_select_request_start()
        request += f" AND {self.entity.table_name}.{self.entity.primary_key} = %s LIMIT 1;"

        return self.fetch_one(request, (entity_id,))

    def delete(self, entity_id):
        request = f"DELETE FROM {self.entity.table_name} WHERE {self.entity.primary_key} = %s"
        self.write(request, (entity_id,), True)

    def get_select_request_start(self):
        return f"SELECT * FROM {self.entity.table_name} WHERE {self.entity.primary_key} IS NOT NULL " # pylint: disable=C0301

    def get_list(self, filters, page, limit, order_by, order):
        filter_request = ''
        values = []

        usable_fields = {
            **self.entity.expected_fields,
            **self.entity.authorized_extra_fields_for_filtering
        }

        for api_field, data in usable_fields.items():
            current_filter_values = filters.getlist(api_field + '[]')
            if 0 != len(current_filter_values):
                or_request = ' AND ('
                for filter_value in current_filter_values:
                    if data['type']== 'int' or data['type']== 'strict-text':
                        or_request += data['field'] + " = %s OR "
                        value_to_bind = filter_value
                    else: # text
                        or_request += data['field'] + " LIKE %s OR "
                        value_to_bind = f"%{filter_value}%"

                    values.append(value_to_bind)

                length = len(or_request)
                or_request = or_request[:length-3]
                or_request += ') '
                filter_request += or_request


        count_request = f"SELECT count(*) as count FROM {self.entity.table_name} "
        count_request += f"WHERE {self.entity.primary_key} IS NOT NULL {filter_request}"
        total_result_count = self.fetch_cursor(count_request, values)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit

        if order_by in usable_fields:
            order_by = usable_fields[order_by]['field']
        else:
            order_by = self.entity.primary_key

        order = order.lower()
        if order not in ['asc', 'desc']:
            order = 'asc'

        request = self.get_select_request_start() + filter_request + f" ORDER BY {order_by} {order}"
        request += " LIMIT " + str(limit) + " OFFSET " + str(offset)
        result = self.fetch_multiple(request, values)

        total_page_count = int(math.ceil(total_result_count/limit))
        total_page_count = 1 if total_result_count == 0 else total_page_count

        return {
            "resultCount": len(result),
            "totalResultCount": total_result_count,
            "page": page,
            "totalPageCount": total_page_count,
            "result": [entry.serialize() for entry in result]
        }

    def insert(self, object, commit = True):
        """Insert a new entry"""
        request = f"INSERT INTO {object.table_name} ("

        for api_field, data in object.expected_fields.items(): # pylint: disable=W0612
            request += data['field'] + ', '

        length = len(request)
        request = request[:length-2]
        request += ') VALUES ('

        for api_field, data in object.expected_fields.items(): # pylint: disable=W0612
            request += '%s, '

        length = len(request)
        request = request[:length-2]
        request += ')'

        values = []
        for api_field, data in object.expected_fields.items(): # pylint: disable=W0612
            method_to_call = getattr(object, 'get' + data['method'])
            values.append(method_to_call())

        return self.get_by_id(self.write(request, values, commit))

    def update(self, object, commit = True):
        request = f"UPDATE {object.table_name} SET "

        for api_field, data in object.expected_fields.items(): # pylint: disable=W0612
            request += data['field'] + ' = %s, '

        length = len(request)
        request = request[:length-2]

        request += f" WHERE {object.primary_key} = %s"

        values = []
        for api_field, data in object.expected_fields.items():
            method_to_call = getattr(object, 'get' + data['method'])
            values.append(method_to_call())

        values.append(object.get_id())
        self.write(request, values, commit)

        return self.get_by_id(object.get_id())
