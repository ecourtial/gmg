""" Games controller for the GMG project """
from flask import jsonify, request 
from src.repository.game_repository import GameRepository
from src.service.game_service import GameService
from src.entity.game import Game

class GameController:
    @classmethod
    def get_by_id(cls, mysql, id):
        repo = GameRepository(mysql)
        game = repo.get_by_id(id)

        if game is None:
            return jsonify({'message': 'Game not found.'}), 404

        return jsonify(game.serialize()), 200

    @classmethod
    def create(cls, mysql):
        title = request.form.get('title', '')

        if title == '':
            return jsonify({'message': 'Incomplete payload. The request need the title field to be filled.'}), 400

        service = GameService(mysql)
        result = service.create(title)

        if isinstance(result, Game) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_id(mysql, result.get_id())

    @classmethod
    def update(cls, mysql, game_id):
        repo = GameRepository(mysql)
        game = repo.get_by_id(game_id)

        if game is None:
            return jsonify({'message': 'Game not found.'}), 404

        title = request.form.get('title', '')
        
        if title == '':
            return jsonify({'message': 'Incomplete payload. The request need the title field to be filled.'}), 400

        game.set_title(title)
        service = GameService(mysql)
        result = service.update(game)

        if isinstance(result, Game) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_id(mysql, result.get_id())

    @classmethod
    def delete(cls, mysql, game_id):
        repo = GameRepository(mysql)
        game = repo.get_by_id(game_id)

        if game is None:
            return jsonify({'message': 'Game not found.'}), 404

        service = GameService(mysql)
        result = service.delete(game)

        if result is False:
            return jsonify({'message': 'Game has versions. Cannot delete it.'}), 400

        return jsonify({'message': 'Game successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        repo = GameRepository(mysql)
        
        return jsonify(repo.get_list(page, limit))
