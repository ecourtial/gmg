from src.controller.abstract_controller import AbstractController
from src.repository.copy_repository import CopyRepository
from src.service.copy_service import CopyService

class CopyController(AbstractController):
    repository = CopyRepository
    service = CopyService
