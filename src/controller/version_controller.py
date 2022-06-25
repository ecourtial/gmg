from src.controller.abstract_controller import AbstractController
from src.repository.version_repository import VersionRepository
from src.service.version_service import VersionService

class VersionController(AbstractController):
    repository = VersionRepository
    service = VersionService
