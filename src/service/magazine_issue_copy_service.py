from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.magazine_issue_copy_repository import MagazineIssueCopyRepository
from src.repository.magazine_issue_repository import MagazineIssueRepository
from src.entity.magazine_issue_copy import MagazineIssueCopy
from src.exception.unknown_resource_exception import ResourceNotFoundException


class MagazineIssueCopyService(AbstractService):
    resource_type = 'magazine_issue_copy'

    def __init__(self, mysql: Any) -> None:
        self.repository = MagazineIssueCopyRepository(mysql)
        self.magazine_issue_repository = MagazineIssueRepository(mysql)

    def get_for_create(self) -> MagazineIssueCopy:
        copy = super().validate_payload_for_creation_and_hydrate(MagazineIssueCopy)

        if self.magazine_issue_repository.get_by_id(copy.get_magazine_issue_id()) is None:
            raise ResourceNotFoundException('magazine_issue', copy.get_magazine_issue_id())

        return copy

    def get_for_update(self, copy_id: int) -> MagazineIssueCopy:
        copy = self.repository.get_by_id(copy_id)

        if copy is None:
            raise ResourceNotFoundException('magazine_issue_copy', copy_id)

        super().hydrate_for_update(copy)

        return copy

    def delete(self, copy_id: int) -> bool:
        copy = self.repository.get_by_id(copy_id)

        if copy is None:
            raise ResourceNotFoundException('magazine_issue_copy', copy_id)

        self.repository.delete(copy_id)

        return True
