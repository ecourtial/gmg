from typing import Any

from src.service.abstract_service import AbstractService
from src.repository.game_version_magazine_mention_repository import GameVersionMagazineMentionRepository
from src.repository.magazine_issue_repository import MagazineIssueRepository
from src.repository.version_repository import VersionRepository
from src.entity.game_version_magazine_mention import GameVersionMagazineMention
from src.exception.unknown_resource_exception import ResourceNotFoundException


class GameVersionMagazineMentionService(AbstractService):
    resource_type = 'game_version_magazine_mention'

    def __init__(self, mysql: Any) -> None:
        self.repository = GameVersionMagazineMentionRepository(mysql)
        self.magazine_issue_repository = MagazineIssueRepository(mysql)
        self.version_repository = VersionRepository(mysql)

    def get_for_create(self) -> GameVersionMagazineMention:
        mention = super().validate_payload_for_creation_and_hydrate(GameVersionMagazineMention)

        if self.magazine_issue_repository.get_by_id(mention.get_magazine_issue_id()) is None:
            raise ResourceNotFoundException('magazine_issue', mention.get_magazine_issue_id())

        if self.version_repository.get_by_id(mention.get_game_version_id()) is None:
            raise ResourceNotFoundException('version', mention.get_game_version_id())

        return mention

    def get_for_update(self, mention_id: int) -> GameVersionMagazineMention:
        mention = self.repository.get_by_id(mention_id)

        if mention is None:
            raise ResourceNotFoundException('game_version_magazine_mention', mention_id)

        super().hydrate_for_update(mention)

        return mention

    def delete(self, mention_id: int) -> bool:
        mention = self.repository.get_by_id(mention_id)

        if mention is None:
            raise ResourceNotFoundException('game_version_magazine_mention', mention_id)

        self.repository.delete(mention_id)

        return True
