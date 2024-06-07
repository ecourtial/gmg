""" Repository to handle the notes """
from src.repository.abstract_repository import AbstractRepository
from src.entity.note import Note

class NoteRepository(AbstractRepository):
    entity = Note

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)

        return version
