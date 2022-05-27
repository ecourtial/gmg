from src.repository.game_repository import GameRepository
from src.entity.game import Game
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.helpers.json_helper import JsonHelper

class GameService:
    def __init__(self, mysql):
        self.game_repository = GameRepository(mysql)

    def validate_payload_for_creation_and_hydrate(self):
        values = []
        values.append(None)

        for api_field, data in Game.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)
                else:
                    values.append(data['default'])
            else:
                values.append(value)

        game = Game(*values)

        existing_version = self.game_repository.get_by_title(game.get_title())

        if existing_version is not None:
            raise ResourceAlreadyExistsException('game', game.get_title(), 'title')

        return game

    def validate_payload_for_update_and_hydrate(self, game_id):
        # Verification
        game = self.game_repository.get_by_id(game_id)

        if game is None:
            raise ResourceNotFoundException('game', game_id)

        title = JsonHelper.get_value_from_request('title', game.get_title())
        existing_version = self.game_repository.get_by_title(title)

        if existing_version is not None and existing_version.get_id() != game.get_id():
            raise ResourceAlreadyExistsException('game', game.get_title(), 'title')

        # Hydratation
        for api_field, data in Game.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)
        
            if value is not None:
                method_to_call = getattr(game, 'set' + data['method'])
                method_to_call(value)

        return game

    def delete(self, game_id):
        """Delete a game"""
        game = self.game_repository.get_by_id(game_id)

        if game is None:
            raise ResourceNotFoundException('game', game_id)

        count = self.game_repository.get_versions_count_for_game(game_id)['count']

        if count > 0:
            raise RessourceHasChildrenException('game', 'version')

        self.game_repository.delete(game_id)

        return True
