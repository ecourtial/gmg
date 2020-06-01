from src.repository.user_repository import UserRepository
from flask import session
import hashlib
import random
import string

class UserService:

    def __init__(self, mysql):
        self.user_repository = UserRepository(mysql)

    def create(self, email, rawPassword, user_name):
        salt = self.get_random_salt(8)
        password = self.get_hashed_password(rawPassword, salt)
        self.user_repository.insert(email, password, salt, user_name)

    def update(self, user, rawPassword, new_email):
        password = self.get_hashed_password(rawPassword, user.get_salt())
        self.user_repository.update(user.get_email(), new_email, password)

    def get_hashed_password(self, password, salt):
        password = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(salt, 'utf-8'), 4)
        return password.hex()

    @classmethod
    def get_random_salt(cls, stringLength):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))    

    def add_token_to_session(self):
        session['csrfToken'] = self.get_random_salt(20)

    def get_authenticated_user(self, email, rawPassword):
        user = self.user_repository.get_by_email(email)
        if user is None:
            return False

        hashedPassword = self.get_hashed_password(rawPassword, user.get_salt())
        if (hashedPassword == user.get_password() and user.is_active()):
            self.add_token_to_session()
            #user.set_is_authenticated(True)
            return user

        return False