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
        salt = self.get_random_salt(8)
        password = self.get_hashed_password(raw_password, salt)
        self.user_repository.insert(email, password, salt, user_name)

    def update(self, user, raw_password, new_email):
        """Update an user"""
        password = self.get_hashed_password(raw_password, user.get_salt())
        self.user_repository.update(user.get_email(), new_email, password)

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

    def add_token_to_session(self):
        """Add a CSRF toke to the session"""
        session['csrfToken'] = self.get_random_salt(20)

    def get_authenticated_user(self, email, raw_password):
        """Load a user and check if the credentials are correct"""
        user = self.user_repository.get_by_email(email)
        if user is None:
            return False

        hashed_password = self.get_hashed_password(raw_password, user.get_salt())
        if (hashed_password == user.get_password() and user.is_active()):
            self.add_token_to_session()
            return user

        return False
