""" Repository to handle the platforms """
from src.repository.abstract_repository import AbstractRepository
from src.entity.platform import Platform
from src.entity.version import Version

class PlatformRepository(AbstractRepository):
    entity = Platform

    def get_select_request_start(self):
        request = f"SELECT {Platform.table_name}.*, v.versionCount AS versionCount "
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS versionCount, {Platform.table_name}.id AS platform_id "
        request += f"      FROM {Version.table_name}, {Platform.table_name}  "
        request += f"      WHERE {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} "
        request += f"      GROUP BY {Platform.table_name}.{Platform.primary_key}) AS v "
        request += f"RIGHT JOIN {Platform.table_name} ON "
        request += f"{Platform.table_name}.{Platform.primary_key} = v.platform_id WHERE TRUE "

        return request

    def get_by_name(self, name):
        """Get one support by its name."""
        request = self.get_select_request_start() + f"AND {Platform.table_name}.name = %s LIMIT 1;"

        return self.fetch_one(request, (name,))

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_version_count(row['versionCount'])

        return version
