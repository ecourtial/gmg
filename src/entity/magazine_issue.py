from typing import Any

from src.entity.abstract_entity import AbstractEntity

class MagazineIssue(AbstractEntity):
    """ This class represent a magazine issue, for instance "Issue #39" """

    expected_fields: dict[str, Any] = {
        'magazineId': {
            'field': 'magazine_id',
            'method': '_magazine_id',
            'required': True,
            'type': 'int'
        },
        'issueNumber': {'field': 'issue_number', 'method': '_issue_number', 'required': True, 'type': 'int'},
        'year': {'field': 'year', 'method': '_year', 'required': True, 'type': 'int'},
        'month': {'field': 'month', 'method': '_month', 'required': True, 'type': 'int'},
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'magazineId': {'field': 'magazine_id', 'origin': 'native', 'type': 'int'},
        'year': {'field': 'year', 'origin': 'native', 'type': 'int'},
        'month': {'field': 'month', 'origin': 'native', 'type': 'int'},
    }

    table_name = 'magazine_issues'
    primary_key = 'id'

    def __init__(self, entity_id: int | None, magazine_id: int, issue_number:int, year: int, month: int, notes: str, copy_count: int | None = None, mention_count: int | None = None) -> None:
        self.entity_id = entity_id
        self.issue_number = issue_number
        self.notes = notes
        self.magazine_id = magazine_id
        self.year = year
        self.month = month
        self.copy_count = int(copy_count or 0)
        self.mention_count = int(mention_count or 0)

    def get_id(self) -> int | None:
        """Return the id of the issue, for instance "125"."""
        return self.entity_id

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def get_magazine_id(self)-> int:
        return self.magazine_id

    def set_magazine_id(self, magazine_id: int)-> None:
        self.magazine_id = magazine_id

    def get_issue_number(self)-> int:
        return self.issue_number

    def set_issue_number(self, issue_number:int )-> None:
        self.issue_number = issue_number

    def get_month(self)-> int:
        return self.month

    def set_month(self, month: int)-> None:
        self.month = month

    def get_year(self)-> int:
        return self.year

    def set_year(self, year: int)-> None:
        self.year = year

    def get_copy_count(self) -> int:
        return self.copy_count

    def set_copy_count(self, copy_count: int | None) -> None:
        self.copy_count = int(copy_count or 0)

    def get_mention_count(self) -> int:
        return self.mention_count

    def set_mention_count(self, mention_count: int | None) -> None:
        self.mention_count = int(mention_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        return values
