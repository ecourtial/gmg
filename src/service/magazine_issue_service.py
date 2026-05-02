from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.magazine_issue_repository import MagazineIssueRepository
from src.repository.magazine_repository import MagazineRepository
from src.entity.magazine_issue import MagazineIssue
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper


class MagazineIssueService(AbstractService):
    resource_type = 'magazine_issue'

    def __init__(self, mysql: Any) -> None:
        self.repository = MagazineIssueRepository(mysql)
        self.magazine_repository = MagazineRepository(mysql)

    def get_for_create(self) -> MagazineIssue:
        issue = super().validate_payload_for_creation_and_hydrate(MagazineIssue)

        if self.magazine_repository.get_by_id(issue.get_magazine_id()) is None:
            raise ResourceNotFoundException('magazine', issue.get_magazine_id())

        existing = self.repository.get_by_magazine_and_issue_number(issue.get_magazine_id(), issue.get_issue_number())
        if existing is not None:
            raise ResourceAlreadyExistsException('magazine_issue', str(issue.get_issue_number()), 'issue_number')

        return issue

    def get_for_update(self, issue_id: int) -> MagazineIssue:
        issue = self.repository.get_by_id(issue_id)

        if issue is None:
            raise ResourceNotFoundException('magazine_issue', issue_id)

        magazine_id = int(JsonHelper.get_value_from_request('magazineId', issue.get_magazine_id()))
        issue_number = int(JsonHelper.get_value_from_request('issueNumber', issue.get_issue_number()))

        existing = self.repository.get_by_magazine_and_issue_number(magazine_id, issue_number)
        if existing is not None and existing.get_id() != issue.get_id():
            raise ResourceAlreadyExistsException('magazine_issue', str(issue_number), 'issue_number')

        super().hydrate_for_update(issue)

        return issue

    def delete(self, issue_id: int) -> bool:
        issue = self.repository.get_by_id(issue_id)

        if issue is None:
            raise ResourceNotFoundException('magazine_issue', issue_id)

        if issue.get_copy_count() > 0:
            raise RessourceHasChildrenException('magazine_issue', 'copy')

        if issue.get_mention_count() > 0:
            raise RessourceHasChildrenException('magazine_issue', 'game_version_magazine_mention')

        self.repository.delete(issue_id)

        return True
