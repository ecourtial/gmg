""" Games controller for the GMG project """
from flask import jsonify, request
from src.repository.game_repository import GameRepository
from src.repository.platform_repository import PlatformRepository

class GameController:
    """ Games controller for the GMG project """
    @classmethod
    def get_list_by_platform(cls, mysql, platform_id):
        """Return the platform list."""
        game_repo = GameRepository(mysql)
        games_list = game_repo.get_list_by_platform(platform_id)
        platform_repo = PlatformRepository(mysql)
        platform = platform_repo.get_by_id(platform_id)
        return jsonify(
            platform=platform.serialize(), games=[game.serialize() for game in games_list]
        )

    @classmethod
    def get_by_id(cls, mysql, game_id):
        """Return the platform list."""
        game_repo = GameRepository(mysql)
        game = game_repo.get_by_id(game_id)

        if game is None:
            return jsonify(message='Unknown game with id: #' + str(game_id)), 404

        return jsonify(game=game.serialize())

    @classmethod
    def get_random(cls, mysql, random_filter):
        """Return a random game."""
        if random_filter not in GameRepository.random_cases:
            return jsonify(message='Unknown random filter: ' + random_filter), 404

        game_repo = GameRepository(mysql)
        game = game_repo.get_random(random_filter)

        if game is None:
            return jsonify(message='No result with filter ' + random_filter)

        return jsonify(game=game.serialize())

    @classmethod
    def get_special_list(cls, mysql, special_filter):
        """Various lists of games"""
        game_repo = GameRepository(mysql)

        if special_filter == 'search':
            query = request.args.get('query')
            games_list = game_repo.get_search(query)
        elif special_filter not in GameRepository.authorized_fields:
            return jsonify('Unknown filter: ' + special_filter), 404
        else:
            games_list = game_repo.get_special_list(special_filter)

        return jsonify(games=[game.serialize() for game in games_list])