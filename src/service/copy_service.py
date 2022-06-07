from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.service.abstract_service import AbstractService
from src.repository.copy_repository import CopyRepository
from src.repository.version_repository import VersionRepository
from src.entity.copy import Copy
from src.exception.unknown_resource_exception import ResourceNotFoundException

class CopyService(AbstractService):
    resource_type = 'copy'

    def __init__(self, mysql):
        self.repository = CopyRepository(mysql)
        self.version_repository = VersionRepository(mysql)

    def get_for_create(self):

        copy = super().validate_payload_for_creation_and_hydrate(Copy)
        version = self.version_repository.get_by_id(copy.get_version_id())

        if version is None:
            raise ResourceNotFoundException('version', copy.get_version_id())

        return copy

    def get_for_update(self, copy_id):
        copy = self.repository.get_by_id(copy_id)

        if copy is None:
            raise ResourceNotFoundException('copy', copy_id)

        super().hydrate_for_update(copy)

        version = self.version_repository.get_by_id(copy.get_version_id())

        if version is None:
            raise ResourceNotFoundException('version', copy.get_version_id())

        return copy

    def delete(self, copy_id):
        copy = self.repository.get_by_id(copy_id)

        if copy is None:
            raise ResourceNotFoundException('copy', copy_id)

        if copy.get_transaction_count() > 0:
            raise RessourceHasChildrenException('copy', 'transaction')

        self.repository.delete(copy_id)

        return True
