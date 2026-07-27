""" Repository to handle the notes """
from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.note import Note


class NoteRepository(AbstractRepository):
    entity = Note

    def hydrate(self, row: dict[str, Any]) -> Note:
        """Hydrate an object from a row."""
        return super().hydrate(row)
