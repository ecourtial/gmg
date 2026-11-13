from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Game(AbstractEntity):
    """ This class represent a game, for instance "The Secret Of Monkey Island" """

    expected_fields: dict[str, Any] = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'versionCount': {'field': 'versionCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'games'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, title: str, notes: str, version_count: int | None = None) -> None:
        self.entity_id = entity_id
        self.title = title
        self.notes = notes
        self.version_count = int(version_count or 0)

    def get_id(self) -> int | None:
        """Return the id of the game, for instance "125"."""
        return self.entity_id

    def get_title(self) -> str:
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def get_version_count(self) -> int:
        return self.version_count

    def set_version_count(self, version_count: int | None) -> None:
        self.version_count = int(version_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['versionCount'] = self.get_version_count()
        return values
