from src.controller.abstract_controller import AbstractController
from src.repository.magazine_repository import MagazineRepository
from src.service.magazine_service import MagazineService

class MagazineController(AbstractController):
    repository = MagazineRepository
    service = MagazineService
