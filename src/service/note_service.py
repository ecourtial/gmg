from src.service.abstract_service import AbstractService
from src.repository.note_repository import NoteRepository
from src.entity.note import Note
from src.exception.unknown_resource_exception import ResourceNotFoundException

class NoteService(AbstractService):
    resource_type = 'note'

    def __init__(self, mysql):
        self.repository = NoteRepository(mysql)


    def get_for_create(self):
        note = super().validate_payload_for_creation_and_hydrate(Note)

        return note

    def get_for_update(self, note_id):
        # Verification
        note = self.repository.get_by_id(note_id)

        if note is None:
            raise ResourceNotFoundException('note', note_id)

        super().hydrate_for_update(note)

        return note

    def delete(self, note_id):
        note = self.repository.get_by_id(note_id)

        if note is None:
            raise ResourceNotFoundException('note', note_id)

        self.repository.delete(note_id)

        return True
