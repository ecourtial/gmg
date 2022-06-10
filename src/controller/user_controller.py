"""Controller to handle user operations"""
from flask import jsonify
from src.exception.inactive_user_exception import InactiveUserException
from src.exception.invalid_input import InvalidInput
from src.exception.missing_field_exception import MissingFieldException
from src.exception.missing_header_exception import MissingHeaderException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.unsupported_filter_exception import UnsupportedFilterException
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService

class UserController:
    @classmethod
    def authenticate(cls, mysql):
        user_service = UserService(mysql)

        try:
            user = user_service.authenticate()
        except MissingFieldException as error:
            return jsonify({'message': str(error)}), 400
        except InvalidInput as error:
            return jsonify({'message': str(error)}), 400
        except MissingHeaderException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 403
        except InactiveUserException as error:
            return jsonify({'message': str(error)}), 403

        return jsonify(
            {'id': user.get_id(), 'username': user.get_user_name(), 'token': user.get_token()}
        ), 200

    @classmethod
    def get_by_filter(cls, mysql, filter, filter_value):
        user_service = UserService(mysql)

        try:
            user = user_service.get_by_filter(filter, filter_value)
        except UnsupportedFilterException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404

        return jsonify(
            {
                'id': user.get_id(),
                'email': user.get_email(),
                'username': user.get_user_name(),
                'active': user.get_is_active()
            }
        ), 200

    @classmethod
    def create(cls, mysql):
        service = UserService(mysql)

        try:
            user = service.validate_payload_for_creation_and_hydrate()
        except MissingFieldException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceAlreadyExistsException as error:
            return jsonify({'message': str(error)}), 400

        user = service.create(user)

        return cls.get_by_filter(mysql, 'id', user.get_id())

    @classmethod
    def update(cls, mysql, user_id):
        service = UserService(mysql)

        try:
            user = service.update(user_id)
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404
        except MissingFieldException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceAlreadyExistsException as error:
            return jsonify({'message': str(error)}), 400

        repo = UserRepository(mysql)
        user = repo.update(user)

        return cls.get_by_filter(mysql, 'id', user.get_id())

    @classmethod
    def renew_token(cls, mysql, current_user):
        user_service = UserService(mysql)
        user_service.renew_token(current_user)

        return cls.get_by_filter(mysql, 'id', current_user.get_id())
