"""Controller to handle user operations"""
from flask import jsonify
from src.exception.inactive_user_exception import InactiveUserException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.unsupported_filter_exception import UnsupportedFilterException
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService

class UserController:
    @classmethod
    def authenticate(cls, mysql):
        userService = UserService(mysql)
        
        try:
            user = userService.authenticate()
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 403
        except InactiveUserException as e:
            return jsonify({'message': str(e)}), 403     

        return jsonify({'id': user.get_id(), 'username': user.get_user_name(), 'token': user.get_token()}), 200

    @classmethod
    def get_by_filter(cls, mysql, filter, filter_value):
        userService = UserService(mysql)
        
        try:
            user = userService.get_by_filter(filter, filter_value)
        except UnsupportedFilterException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404  

        return jsonify({'id': user.get_id(), 'email': user.get_email(), 'userName': user.get_user_name(), 'active': user.get_is_active()}), 200

    @classmethod
    def create(cls, mysql):
        service = UserService(mysql)

        try:
            user = service.validate_payload_for_creation_and_hydrate()
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400
        
        user = service.create(user)

        return cls.get_by_filter(mysql, 'id', user.get_id())

    @classmethod
    def update(cls, mysql, user_id):
        service = UserService(mysql)

        try:
            user = service.update(user_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        repo = UserRepository(mysql)
        user = repo.update(user)

        return cls.get_by_filter(mysql, 'id', user.get_id())

    @classmethod
    def renew_token(cls, mysql, current_user):
        user_service = UserService(mysql)
        user_service.renew_token(current_user)

        return cls.get_by_filter(mysql, 'id', current_user.get_id())
