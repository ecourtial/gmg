""" Games controller for the GMG project """
from flask import jsonify, request 
from src.repository.game_repository import GameRepository
from src.service.game_service import GameService
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException

class GameController:
    @classmethod
    def get_by_id(cls, mysql, game_id):
        service = GameService(mysql)

        try:
            game = service.get_by_id(game_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404

        return jsonify(game.serialize()), 200

    @classmethod
    def create(cls, mysql):
        service = GameService(mysql)

        try:
            game = service.validate_payload_for_creation_and_hydrate()
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        repo = GameRepository(mysql)
        game = repo.insert(game)

        return cls.get_by_id(mysql, game.get_id())

    @classmethod
    def update(cls, mysql, game_id):
        service = GameService(mysql)

        try:
            game = service.validate_payload_for_update_and_hydrate(game_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        repo = GameRepository(mysql)
        game = repo.update(game)

        return cls.get_by_id(mysql, game.get_id())

    @classmethod
    def delete(cls, mysql, game_id):
        service = GameService(mysql)

        try:
            service.delete(game_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except RessourceHasChildrenException as e:
            return jsonify({'message': str(e)}), 400

        return jsonify({'message': 'Game successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        repo = GameRepository(mysql)
        
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        order_by = request.args.get('order_by')
        order = request.args.get('order')

        return jsonify(repo.get_list(request.args, page, limit, order_by, order))
