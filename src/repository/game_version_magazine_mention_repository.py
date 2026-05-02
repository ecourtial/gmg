""" Repository to handle the game version magazine mentions """
from src.repository.abstract_repository import AbstractRepository
from src.entity.game_version_magazine_mention import GameVersionMagazineMention


class GameVersionMagazineMentionRepository(AbstractRepository):
    entity = GameVersionMagazineMention
