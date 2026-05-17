from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Note(AbstractEntity):
    """ This class represent a note entry """

    expected_fields: dict[str, Any] = {
        'title': {
            'field': 'title',
            'method': '_title',
            'required': True,
            'type': 'text',
            'default': ''
        },
        'content': {
            'field': 'content',
            'method': '_content',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    table_name = 'notes'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, title: str, content: str) -> None:
        self.entity_id = entity_id
        self.title = title
        self.content = content

    def get_id(self) -> int | None:
        return self.entity_id

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content

    def set_title(self, title: str) -> None:
        self.title = title

    def set_content(self, content: str) -> None:
        self.content = content
