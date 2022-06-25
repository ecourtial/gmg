from src.entity.abstract_entity import AbstractEntity

class Game(AbstractEntity):
    expected_fields = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'versionCount': {'field': 'versionCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'games'
    primary_key = 'id'

    """ This class represent a game, for instance "The Secret Of Monkey Island" """
    def __init__(
            self,
            entity_id,
            title,
            notes,
            version_count = None,
    ):
        self.entity_id = entity_id
        self.title = title
        self.notes = notes
        self.version_count = int(version_count or 0)

    def get_id(self):
        """Return the id of the game, for instance "125"."""

        return self.entity_id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title

    def set_title(self, title):
        self.title = title

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_version_count(self):
        return self.version_count

    def set_version_count(self, version_count):
        self.version_count = int(version_count or 0)

    def serialize(self):
        values = super().serialize()

        values['versionCount'] = self.get_version_count()

        return values
