"""Controller to handle user operations"""
from flask import request, jsonify
from src.entity.user import User
from src.helpers.json_helper import JsonHelper
from src.service.user_service import UserService
from src.repository.user_repository import UserRepository

class UserController:
    """Another useless comment"""

    @classmethod
    def authenticate(cls, mysql):
        email = JsonHelper.get_value_from_request('email', '')
        password = JsonHelper.get_value_from_request('password', '')

        if email == '' or password == '':
            return jsonify({'message': 'Incomplete payload. The request need the email and password fields to be filled.'}), 400

        user_service = UserService(mysql)
        user = user_service.get_authenticated_user(email, password)

        if user is False or user.is_active == 0:
            return jsonify({'message': 'User not found.'}), 403

        return jsonify({'id': user.get_id(), 'username': user.get_user_name(), 'token': user.get_token()}), 200

    @classmethod
    def get_by_filter(cls, mysql, filter, filter_value):
        repo = UserRepository(mysql)

        if filter == 'id':
            user = repo.get_by_id(filter_value)
        elif filter == 'email':
            user = repo.get_by_email(filter_value)
        elif filter == 'username':
            user = repo.get_by_user_name(filter_value)
        else:
            return jsonify({'message': 'Unknown filter. Allowed filters are: id, email, username.'}), 400

        if user is None:
            return jsonify({'message': 'No user found.'}), 404

        return jsonify({'id': user.get_id(), 'email': user.get_email(), 'userName': user.get_user_name(), 'active': user.is_active()}), 200

    @classmethod
    def create(cls, mysql):
        email = JsonHelper.get_value_from_request('email', '')
        password = JsonHelper.get_value_from_request('password', '')
        user_name = JsonHelper.get_value_from_request('username', '')

        if email == '' or password == '' or user_name == '':
            return jsonify({'message': 'Incomplete payload. The request need the email, password and username fields to be filled.'}), 400

        user_service = UserService(mysql)
        result = user_service.create(email, password, user_name)

        if isinstance(result, User) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_filter(mysql, 'id', result.get_id())

    @classmethod
    def update(cls, mysql, user_id):
        repo = UserRepository(mysql)
        user = repo.get_by_id(user_id)

        if user is None:
            return jsonify({'message': 'User not found.'}), 404

        email = JsonHelper.get_value_from_request('email', '')
        password = JsonHelper.get_value_from_request('password', '')
        status = JsonHelper.get_value_from_request('status', '')
        user_name = JsonHelper.get_value_from_request('username', '')

        user_service = UserService(mysql)
        result = user_service.update(user, email, password, user_name, status)

        if result is not True:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_filter(mysql, 'id', user.get_id())

    @classmethod
    def renew_token(cls, mysql, current_user):
        user_service = UserService(mysql)
        user_service.renew_token(current_user)

        return cls.get_by_filter(mysql, 'id', current_user.get_id())
