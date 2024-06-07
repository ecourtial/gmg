from src.controller.abstract_controller import AbstractController
from src.repository.note_repository import NoteRepository
from src.service.note_service import NoteService

class NoteController(AbstractController):
    repository = NoteRepository
    service = NoteService
