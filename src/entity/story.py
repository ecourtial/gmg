from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Story(AbstractEntity):
    """ This class represent a history entry, for instance I watched or played this game in 2021 """

    expected_fields: dict[str, Any] = {
        'versionId': {
            'field': 'version_id',
            'method': '_version_id',
            'required': True,
            'type': 'int'
        },
        'year': {'field': 'year', 'method': '_year', 'required': True, 'type': 'int'},
        'position': {'field': 'position', 'method': '_position', 'required': True, 'type': 'int'},
        'watched': {'field': 'watched', 'method': '_watched', 'required': True, 'type': 'int'},
        'played': {'field': 'played', 'method': '_played', 'required': True, 'type': 'int'},
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'platformName': {'field': 'platformName', 'origin': 'computed', 'type': 'string'},
        'gameTitle': {'field': 'gameTitle', 'origin': 'computed', 'type': 'string'},
    }

    table_name = 'stories'
    primary_key = 'id'

    def __init__(
            self,
            entity_id: int | None,
            version_id: int,
            year: int,
            position: int,
            watched: int,
            played: int,
            platform_name: str | None = None,
            game_title: str | None = None,
    ) -> None:
        self.entity_id = entity_id
        self.version_id = version_id
        self.year = year
        self.position = position
        self.watched = bool(watched)
        self.played = bool(played)
        self.platform_name = platform_name
        self.game_title = game_title

    def get_id(self) -> int | None:
        return self.entity_id

    def get_version_id(self) -> int:
        return self.version_id

    def get_year(self) -> int:
        return self.year

    def get_position(self) -> int:
        return self.position

    def get_watched(self) -> bool:
        return self.watched

    def get_played(self) -> bool:
        return self.played

    def set_version_id(self, version_id: int) -> None:
        self.version_id = version_id

    def set_year(self, year: int) -> None:
        self.year = year

    def set_position(self, position: int) -> None:
        self.position = position

    def set_watched(self, status: int) -> None:
        self.watched = bool(status)

    def set_played(self, status: int) -> None:
        self.played = bool(status)

    def get_game_title(self) -> str | None:
        return self.game_title

    def set_game_title(self, title: str) -> None:
        self.game_title = title

    def get_platform_name(self) -> str | None:
        return self.platform_name

    def set_platform_name(self, platform_name: str) -> None:
        self.platform_name = platform_name

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()
        return values
