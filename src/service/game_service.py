from src.service.abstract_service import AbstractService
from src.repository.game_repository import GameRepository
from src.entity.game import Game
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class GameService(AbstractService):
    resource_type = 'game'

    def __init__(self, mysql):
        self.repository = GameRepository(mysql)

    def get_for_create(self):
        game = super().validate_payload_for_creation_and_hydrate(Game)

        existing_version = self.repository.get_by_title(game.get_title())

        if existing_version is not None:
            raise ResourceAlreadyExistsException('game', game.get_title(), 'title')

        return game

    def get_for_update(self, game_id):
        # Verification
        game = self.repository.get_by_id(game_id)

        if game is None:
            raise ResourceNotFoundException('game', game_id)

        title = JsonHelper.get_value_from_request('title', game.get_title())
        existing_version = self.repository.get_by_title(title)

        if existing_version is not None and existing_version.get_id() != game.get_id():
            raise ResourceAlreadyExistsException('game', game.get_title(), 'title')

        super().hydrate_for_update(game)

        return game

    def delete(self, game_id):
        """Delete a game"""
        game = self.repository.get_by_id(game_id)

        if game is None:
            raise ResourceNotFoundException('game', game_id)

        if game.get_version_count() > 0:
            raise RessourceHasChildrenException('game', 'version')

        self.repository.delete(game_id)

        return True
