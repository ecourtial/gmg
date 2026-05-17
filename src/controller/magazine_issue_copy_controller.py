from src.controller.abstract_controller import AbstractController
from src.repository.magazine_issue_copy_repository import MagazineIssueCopyRepository
from src.service.magazine_issue_copy_service import MagazineIssueCopyService

class MagazineIssueCopyController(AbstractController):
    repository = MagazineIssueCopyRepository
    service = MagazineIssueCopyService
