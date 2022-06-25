"""An abstract repository"""
import math
from src.repository.abstract_core_repository import AbstractCoreRepository

class AbstractRepository(AbstractCoreRepository):
    def get_by_id(self, entity_id):
        """Get one support by its primary key."""
        request = self.get_select_request_start()
        request += f" AND {self.entity.table_name}.{self.entity.primary_key} = %s LIMIT 1;" # pylint: disable=E1101

        return self.fetch_one(request, (entity_id,))

    def delete(self, entity_id, commit = True):
        request = f"DELETE FROM {self.entity.table_name} WHERE {self.entity.primary_key} = %s" # pylint: disable=E1101
        self.write(request, (entity_id,), commit)

    def get_select_request_start(self):
        return f"SELECT * FROM {self.entity.table_name} WHERE {self.entity.primary_key} IS NOT NULL " # pylint: disable=E1101

    def get_list(self, filters, page, limit):
        filter_request = ''
        values = []

        usable_fields = {
            **self.entity.expected_fields, # pylint: disable=E1101
            **self.entity.authorized_extra_fields_for_filtering # pylint: disable=E1101
        }

        # Create the filter part of the SQL request

        # Loop on each field to see if a related filter is given
        for api_field, data in usable_fields.items():
            field = 'e.' + data['field']
            current_filter_values = filters.getlist(api_field + '[]')
            # A filter is given for this field
            if 0 != len(current_filter_values):
                filter_request += AbstractRepository.create_get_list_filter_condition(current_filter_values, data, field, values)

        # Count the total of result without pagination
        count_request = "SELECT count(*) as count "
        count_request += f"FROM ({self.get_select_request_start()}) AS e, {self.entity.table_name} " # pylint: disable=E1101
        count_request += f"WHERE {self.entity.table_name}.{self.entity.primary_key} IS NOT NULL " # pylint: disable=E1101
        count_request += f"AND {self.entity.table_name}.{self.entity.primary_key} = e.{self.entity.primary_key} " # pylint: disable=E1101
        count_request += filter_request
        total_result_count = self.fetch_cursor(count_request, values)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit

        # ORDER BY
        order_by_conditions = self.get_order_by_conditions(usable_fields, filters)

        # Process the actual SELECT request
        request = f"SELECT * FROM ({self.get_select_request_start()}) AS e "
        request += 'WHERE TRUE ' + filter_request + order_by_conditions
        request += "LIMIT " + str(limit) + " OFFSET " + str(offset)
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

    def get_order_by_conditions(self, usable_fields, filters):
        filter_request = ''
        order_by_filters = filters.getlist('orderBy[]')

        if 0 != len(order_by_filters):
            for filter_value in order_by_filters:
                if filter_value.find('-') != -1:
                    array = filter_value.split('-')
                    field = array[0]
                    order = array[1].lower()
                    # EX: id-ASC
                    if (field in usable_fields and
                        order in ['asc', 'desc']):
                        filter_request += usable_fields[field]['field']
                        filter_request += f" {order}, "
                elif filter_value == 'rand':
                    filter_request += 'RAND(), '

        if filter_request == '':
            filter_request = 'ORDER BY ' + self.entity.primary_key + ' ASC ' # pylint: disable=E1101
        else:
            length = len(filter_request)
            filter_request = 'ORDER BY ' + filter_request[:length-2] + ' '

        return filter_request

    # This method handles the creation of the SQL conditions for each filter
    @classmethod
    def create_get_list_filter_condition(cls, current_filter_values, filter_data, field, values):
        comparison_operators = {
            'lt': '<',
            'gt': '>',
            'eq': '=',
            'neq': '!=',
        }

        or_request = ' AND ('
        # Loop on all the values given for this filter
        for filter_value in current_filter_values:
            # Various possibility according to the field type
            if filter_data['type'] == 'int' or filter_data['type']== 'strict-text':
                comparison_operator = ' = '

                if filter_data['type'] == 'int':
                    for comp_url_key, comp_sql_key in comparison_operators.items():# pylint: disable=W0612
                        if filter_value.startswith(comp_url_key + '-'):
                            array = filter_value.split('-')
                            comparison_operator = comparison_operators[array[0]]
                            filter_value = array[1]

                or_request += field + f" {comparison_operator} %s OR "
                value_to_bind = filter_value
            else: # text
                or_request += field + " LIKE %s OR "
                value_to_bind = f"%{filter_value}%"

            values.append(value_to_bind)

        length = len(or_request)
        or_request = or_request[:length-3]
        or_request += ') '

        return or_request

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
