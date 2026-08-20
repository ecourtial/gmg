from typing import Any

from src.entity.abstract_entity import AbstractEntity

class GameVersionCategoryAssociation(AbstractEntity):
    """ This class represent a category to associate game versions"""

    expected_fields: dict[str, Any] = {
        'categoryId': {
            'field': 'category_id',
            'method': '_category_id',
            'required': True,
            'type': 'int'
        },
        'versionId': {
            'field': 'version_id',
            'method': '_version_id',
            'required': True,
            'type': 'int'
        },
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
    }

    table_name = 'game_version_category_association'
    primary_key = 'id'

    def __init__(
        self, 
        entity_id: int | None,
        category_id: int,
        version_id: int,
        notes: str | None,
        category_name: str | None = None,
        version_platform_name: str | None = None,
        game_title: str | None = None,
    ) -> None:
        self.entity_id = entity_id
        self.category_id = category_id
        self.version_id = version_id
        self.notes = notes
        self.category_name = category_name
        self.version_platform_name = version_platform_name
        self.game_title = game_title

    def get_id(self) -> int | None:
        return self.entity_id

    def get_category_id(self) -> int:
        return self.category_id

    def set_category_id(self, category_id: int) -> None:
        self.category_id = category_id

    def get_version_id(self) -> int:
        return self.version_id

    def set_version_id(self, version_id: int) -> None:
        self.version_id = version_id

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def get_category_name(self) -> str | None:
        return self.category_name

    def set_category_name(self, category_name: str) -> None:
        self.category_name = category_name

    def get_version_platform_name(self) -> str | None:
        return self.version_platform_name

    def set_version_platform_name(self, version_platform_name: str) -> None:
        self.version_platform_name = version_platform_name

    def get_game_title(self) -> str | None:
        return self.game_title

    def set_game_title(self, title: str) -> None:
        self.game_title = title

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['categoryName'] = self.get_category_name()
        values['versionPlatformName'] = self.get_version_platform_name()
        values['gameTitle'] = self.get_game_title()
        return values
