from typing import Any

from src.entity.abstract_entity import AbstractEntity


class GameVersionCategory(AbstractEntity):
    """ This class represent a category to associate game versions"""

    expected_fields: dict[str, Any] = {
        'name': {'field': 'name', 'method': '_name', 'required': True, 'type': 'text'},
        'description': {
            'field': 'description',
            'method': '_description',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'versionCount': {'field': 'versionCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'game_version_categories'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, name: str, description: str, version_count: int | None = None) -> None:
        self.entity_id = entity_id
        self.name = name
        self.description = description
        self.version_count = int(version_count or 0)

    def get_id(self) -> int | None:
        return self.entity_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_description(self) -> str:
        return self.description

    def set_description(self, description: str) -> None:
        self.description = description

    def get_version_count(self) -> int:
        return self.version_count

    def set_version_count(self, version_count: int | None) -> None:
        self.version_count = int(version_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['versionCount'] = self.get_version_count()
        return values
