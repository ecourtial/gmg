""" Repository to handle the versions """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.version import Version
import math

class VersionRepository(AbstractRepository):
    def get_select_request_start(self):
        request = "SELECT versions.*, games.title AS gameTitle, platforms.name AS platformName FROM versions, games, platforms "
        request += "WHERE versions.game_id = games.id "
        request += "AND versions.platform_id = platforms.id "

        return request
    
    def get_by_id(self, version_id):
        """Get one version by its id."""
        request = self.get_select_request_start() + "AND versions.version_id = %s LIMIT 1;"

        return self.fetch_one(request, (version_id,))

    def get_by_unique_index(self, platform_id, game_id):
        """Get one version by the unique combination of the platform and the game."""
        request = self.get_select_request_start()
        request += "AND versions.platform_id = %s "
        request += "AND versions.game_id = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id, game_id,))

    def insert(self, version):
        """Insert a new version"""
        request = "INSERT INTO versions ("
        
        for api_field, data in Version.expected_fields.items():
            request += data['field'] + ', '

        length = len(request)
        request = request[:length-2]
        request += ') VALUES ('

        for api_field, data in Version.expected_fields.items():
            request += '%s, '

        length = len(request)
        request = request[:length-2]
        request += ')'
                    
        values = []
        for api_field, data in Version.expected_fields.items():
            method_to_call = getattr(version, 'get' + data['method'])
            values.append(method_to_call())  

        self.write(request, values)

        return self.get_by_unique_index(version.get_platform_id(), version.get_game_id())

    def update(self, version):
        """Update a version"""
        request = "UPDATE versions SET "

        for api_field, data in Version.expected_fields.items():
            request += data['field'] + ' = %s, '

        length = len(request)
        request = request[:length-2]

        request += ' WHERE version_id = %s'

        values = []
        for api_field, data in Version.expected_fields.items():
            method_to_call = getattr(version, 'get' + data['method'])
            values.append(method_to_call())  

        values.append(version.get_id())
        self.write(request, values)

        return self.get_by_id(version.get_id())

    def get_copies_count_for_version(self, version_id):
        request = "SELECT COUNT(*) as count FROM copies WHERE version_id = %s"
        
        return self.fetch_cursor(request, (version_id,))
    
    def delete(self, version_id):
        request = "DELETE FROM versions WHERE version_id = %s"
        self.write(request, (version_id,), True)

    def get_list(self, filters, page, limit, order_by, order):
        filter_request = ''
        values = []

        for api_field, data in Version.expected_fields.items():
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

    
        count_request = 'SELECT count(*) as count FROM versions WHERE version_id IS NOT NULL ' + filter_request
        totalResultCount = self.fetch_cursor(count_request, values)['count']

        page = int(page)
        limit = int(limit)

        page = 1 if page < 1 else page
        offset = (page * limit) - limit

        if order_by in Version.expected_fields:
            order_by = Version.expected_fields[order_by]['field']
        elif order_by in ['gameTitle', 'platformName']:
            order_by = order_by # Well, it's OK
        else:
            order_by = 'version_id'
        
        if order not in ['ASC', 'DESC']:
            order = 'ASC'

        request = self.get_select_request_start() + filter_request + f" ORDER BY {order_by} {order}"
        request += " LIMIT " + str(limit) + " OFFSET " + str(offset)
        result = self.fetch_multiple(request, values)

        totalPageCount = int(math.ceil(totalResultCount/limit));
        totalPageCount = 1 if totalResultCount == 0 else totalPageCount

        return {
            "resultCount": len(result),
            "totalResultCount": totalResultCount,
            "page": page,
            "totalPageCount": totalPageCount,
            "result": [entry.serialize() for entry in result]
        }


    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        values = []
        values.append(row['version_id'])

        for api_field, data in Version.expected_fields.items():
            values.append(row[data['field']])

        version = Version(*values)
        version.set_platform_name(row['platformName'])
        version.set_game_title(row['gameTitle'])

        return version
