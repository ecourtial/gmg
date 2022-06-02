from src.entity.abstract_entity import AbstractEntity

class Platform(AbstractEntity):
    """ This class represent a platform (support), for instance "Playstation" """

    expected_fields = {
        'name': {'field': 'name', 'method': '_name', 'required': True, 'type': 'text'},
    }

    authorized_extra_fields_for_filtering = {
        'id': {'field': 'id'}
    }

    table_name = 'platforms'
    primary_key = 'id'

    def __init__(self, entity_id, name, version_count = None,):
        self.entity_id = entity_id
        self.name = name
        self.version_count = int(version_count or 0)

    def get_id(self):
        """Return the id of the platform, for instance "3"."""
        return self.entity_id

    def get_name(self):
        """Return the name of the platform, for instance "Playstation 2"."""
        return self.name

    def set_name(self, name):
        self.name = name

    def get_version_count(self):
        return self.version_count

    def set_version_count(self, version_count):
        self.version_count = int(version_count or 0)

    def serialize(self):
        values = super().serialize()

        values['versionCount'] = self.get_version_count()

        return values
