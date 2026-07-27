""" Repository to handle the magazine issue copies """
from src.repository.abstract_repository import AbstractRepository
from src.entity.magazine_issue_copy import MagazineIssueCopy


class MagazineIssueCopyRepository(AbstractRepository):
    entity = MagazineIssueCopy
