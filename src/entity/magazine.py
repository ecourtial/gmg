from typing import Any

from src.entity.abstract_entity import AbstractEntity

class Magazine(AbstractEntity):
    """ This class represent a magazine, for instance "PC Gamer" """

    expected_fields: dict[str, Any] = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'issueCount': {'field': 'issueCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'magazines'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, title: str, notes: str, issue_count: int | None = None) -> None:
        self.entity_id = entity_id
        self.title = title
        self.notes = notes
        self.issue_count = int(issue_count or 0)

    def get_id(self) -> int | None:
        """Return the id of the magazine, for instance "125"."""
        return self.entity_id

    def get_title(self) -> str:
        """Return the title of the magazine, for instance "PC Gamer"."""
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def get_issue_count(self) -> int:
        return self.issue_count

    def set_issue_count(self, issue_count: int | None) -> None:
        self.issue_count = int(issue_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['issueCount'] = self.get_issue_count()
        return values
