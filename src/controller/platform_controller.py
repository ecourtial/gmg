from src.controller.abstract_controller import AbstractController
from src.repository.platform_repository import PlatformRepository
from src.service.platform_service import PlatformService

class PlatformController(AbstractController):
    repository = PlatformRepository
    service = PlatformService
