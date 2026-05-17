from typing import Any

from src.entity.abstract_entity import AbstractEntity

class MagazineIssueCopy(AbstractEntity):
    """ This class represent a copy of the issue of a magazine. """
    # If you change the order here, you need to also change it in the constructor!
    expected_fields: dict[str, Any] = {
        'magazineIssueId':
        {
            'field': 'magazine_issue_id',
            'method': '_magazine_issue_id',
            'required': True,
            'type': 'int'
        },
        'type': {
            'field': 'type',
            'method': '_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {'Digital', 'Paper'}
        },
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'issue_copy_id', 'origin': 'native', 'type': 'int'},
        'magazineIssueId': {'field': 'magazine_issue_id', 'origin': 'native', 'type': 'int'},
        'type': {'field': 'type', 'origin': 'native', 'type': 'string'},
    }

    table_name = 'magazine_issue_copies'
    primary_key = 'issue_copy_id'

    # If you change the order here, you need to also change it in the array above!
    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
            self,
            entity_id: int | None,
            magazine_issue_id: int,
            type: str,
            notes: str
    ) -> None:
        self.entity_id = entity_id
        self.magazine_issue_id = int(magazine_issue_id)
        self.type = type
        self.notes = notes

    def get_id(self) -> int | None:
        return self.entity_id

    def get_magazine_issue_id(self) -> int:
        return self.magazine_issue_id

    def set_magazine_issue_id(self, magazine_issue_id: int) -> None:
        self.magazine_issue_id = int(magazine_issue_id)

    def get_type(self) -> str:
        return self.type

    def set_type(self, type: str) -> None:
        self.type = type

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        return values
