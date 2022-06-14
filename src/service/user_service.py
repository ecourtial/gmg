"""UserService to manage most of the operation on users"""
import hashlib
import random
import string
import base64
from flask import request
from src.exception.inactive_user_exception import InactiveUserException
from src.exception.missing_field_exception import MissingFieldException
from src.exception.missing_header_exception import MissingHeaderException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.unsupported_filter_exception import UnsupportedFilterException
from src.exception.invalid_credentials_exception import InvalidCredentialsException
from src.exception.invalid_input import InvalidInput
from src.repository.user_repository import UserRepository
from src.helpers.json_helper import JsonHelper
from src.entity.user import User

class UserService:
    """Useless comment"""
    def __init__(self, mysql):
        self.user_repository = UserRepository(mysql)

    def authenticate(self):
        if 'Authorization' in request.headers:
            header_value = request.headers['Authorization']
            if header_value.find(' ') != -1:
                array = header_value.split(' ')
                if array[0] == 'Basic':
                    try:
                        decoded_value  = base64.b64decode(array[1])
                        decoded_value = decoded_value.decode('utf-8')
                    except UnicodeDecodeError:
                        raise InvalidInput(
                            'Impossible to decode the value of the authentication header.'
                        )

                    if decoded_value.find(':') != -1:
                        array = decoded_value.split(':')

                        return self.get_authenticated_user(array[0], array[1])

        raise MissingHeaderException('Authorization')

    def get_by_filter(self, filter, filter_value):
        if filter == 'id':
            user = self.user_repository.get_by_id(filter_value)
        elif filter == 'email':
            user = self.user_repository.get_by_email(filter_value)
        elif filter == 'username':
            user = self.user_repository.get_by_user_name(filter_value)
        else:
            raise UnsupportedFilterException(filter, ['id', 'email', 'username'])

        if user is None:
            raise ResourceNotFoundException('user', filter_value, filter)

        return user

    def validate_payload_for_creation_and_hydrate(self):
        values = []
        values.append(None)

        for api_field, data in User.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is None:
                if data['required'] is True:
                    raise MissingFieldException(api_field)
                values.append(data['default'])
            else:
                values.append(value)

        values.append(None)
        values.append(None)

        user = User(*values) # pylint: disable=E1120

        check_user = self.user_repository.get_by_email(user.get_email())
        if check_user is not None:
            raise ResourceAlreadyExistsException('user', user.get_email(), 'email')

        check_user = self.user_repository.get_by_user_name(user.get_user_name())
        if check_user is not None:
            raise ResourceAlreadyExistsException('user', user.get_user_name(), 'username')

        return user

    def create(self, user):
        salt = self.get_new_salt()
        user.set_salt(salt)
        user.set_password(self.get_hashed_password(user.get_password(), salt))
        user.set_token(self.get_new_token())

        return self.user_repository.insert(user)

    def update(self, user_id):
        # Verification
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise ResourceNotFoundException('user', user_id)

        # Hydratation
        for api_field, data in User.expected_fields.items():
            value = JsonHelper.get_value_from_request(api_field, None)

            if value is not None:
                method_to_call = getattr(user, 'set' + data['method'])
                method_to_call(value)

        password = JsonHelper.get_value_from_request('password', None)
        if password is not None:
            user.set_password(self.get_hashed_password(password, user.get_salt()))

        check_user = self.user_repository.get_by_email(user.get_email())
        if check_user is not None and check_user.get_id() != user_id:
            raise ResourceAlreadyExistsException('user', user.get_email(), 'email')

        check_user = self.user_repository.get_by_user_name(user.get_user_name())
        if check_user is not None and check_user.get_id() != user_id:
            raise ResourceAlreadyExistsException('user', user.get_user_name(), 'username')

        return user

    def get_new_salt(self):
        return self.get_random_salt(8)

    def get_new_token(self):
        return self.get_random_salt(32)

    def renew_token(self, current_user):
        current_user.set_token(self.get_new_token())
        self.user_repository.update(current_user)

    @classmethod
    def get_hashed_password(cls, password, salt):
        """Generates a hash from a given password and salt"""
        password = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(salt, 'utf-8'), 4)
        return password.hex()

    @classmethod
    def get_random_salt(cls, string_length):
        """Genereates a salt"""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(string_length))

    def get_authenticated_user(self, username, raw_password):
        """Load a user and check if the credentials are correct"""
        user = self.user_repository.get_by_user_name(username)
        if user is None:
            raise ResourceNotFoundException('user', username, 'username')

        hashed_password = self.get_hashed_password(raw_password, user.get_salt())
        if hashed_password != user.get_password():
            raise InvalidCredentialsException()
            
        if user.get_is_active() == False:
            raise InactiveUserException('username', username)

        return user
