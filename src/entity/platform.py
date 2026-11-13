from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Platform(AbstractEntity):
    """ This class represent a platform (support), for instance "Playstation" """

    expected_fields: dict[str, Any] = {
        'name': {'field': 'name', 'method': '_name', 'required': True, 'type': 'text'},
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'versionCount': {'field': 'versionCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'platforms'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, name: str, version_count: int | None = None) -> None:
        self.entity_id = entity_id
        self.name = name
        self.version_count = int(version_count or 0)

    def get_id(self) -> int | None:
        """Return the id of the platform, for instance "3"."""
        return self.entity_id

    def get_name(self) -> str:
        """Return the name of the platform, for instance "Playstation 2"."""
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_version_count(self) -> int:
        return self.version_count

    def set_version_count(self, version_count: int | None) -> None:
        self.version_count = int(version_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['versionCount'] = self.get_version_count()
        return values
