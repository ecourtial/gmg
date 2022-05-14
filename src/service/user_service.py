"""UserService to manage most of the operation on users"""
import hashlib
import random
import string
from flask import session
from src.repository.user_repository import UserRepository

class UserService:
    """Useless comment"""
    def __init__(self, mysql):
        self.user_repository = UserRepository(mysql)

    def create(self, email, raw_password, user_name):
        """Create an user"""
        checkUser = self.user_repository.get_by_email(email)
        if checkUser is not None:
            return 'email'

        checkUser = self.user_repository.get_by_user_name(user_name)
        if checkUser is not None:
            return 'user_name'

        salt = self.get_new_salt()
        token = self.get_new_token()
        password = self.get_hashed_password(raw_password, salt)
        
        return self.user_repository.insert(email, password, salt, user_name, token)
    
    def update(self, user, email, password, user_name, status):
        if (email != ''):
            checkUser = self.user_repository.get_by_email(email)
            if checkUser is not None:
                return 'email'
            user.set_email(email)

        if (status != ''):
            user.set_status(status)

        if (user_name != ''):
            checkUser = self.user_repository.get_by_user_name(user_name)
            if checkUser is not None:
                return 'user_name'
            user.set_user_name(user_name)

        if (password != ''):
            user.set_password(self.get_hashed_password(password, user.get_salt()))

        self.user_repository.update(user)

        return True

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

    def get_authenticated_user(self, email, raw_password):
        """Load a user and check if the credentials are correct"""
        user = self.user_repository.get_by_email(email)
        if user is None:
            return False

        hashed_password = self.get_hashed_password(raw_password, user.get_salt())
        if (hashed_password == user.get_password() and user.is_active()):
            return user

        return False
