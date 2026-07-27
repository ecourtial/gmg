from src.controller.abstract_controller import AbstractController
from src.repository.magazine_issue_repository import MagazineIssueRepository
from src.service.magazine_issue_service import MagazineIssueService

class MagazineIssueController(AbstractController):
    repository = MagazineIssueRepository
    service = MagazineIssueService
