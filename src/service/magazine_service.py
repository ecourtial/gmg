from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.magazine_repository import MagazineRepository
from src.entity.magazine import Magazine
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper


class MagazineService(AbstractService):
    resource_type = 'magazine'

    def __init__(self, mysql: Any) -> None:
        self.repository = MagazineRepository(mysql)

    def get_for_create(self) -> Magazine:
        magazine = super().validate_payload_for_creation_and_hydrate(Magazine)

        existing = self.repository.get_by_title(magazine.get_title())

        if existing is not None:
            raise ResourceAlreadyExistsException('magazine', magazine.get_title(), 'title')

        return magazine

    def get_for_update(self, magazine_id: int) -> Magazine:
        magazine = self.repository.get_by_id(magazine_id)

        if magazine is None:
            raise ResourceNotFoundException('magazine', magazine_id)

        title = JsonHelper.get_value_from_request('title', magazine.get_title())
        existing = self.repository.get_by_title(title)

        if existing is not None and existing.get_id() != magazine.get_id():
            raise ResourceAlreadyExistsException('magazine', magazine.get_title(), 'title')

        super().hydrate_for_update(magazine)

        return magazine

    def delete(self, magazine_id: int) -> bool:
        magazine = self.repository.get_by_id(magazine_id)

        if magazine is None:
            raise ResourceNotFoundException('magazine', magazine_id)

        if magazine.get_issue_count() > 0:
            raise RessourceHasChildrenException('magazine', 'issue')

        self.repository.delete(magazine_id)

        return True
