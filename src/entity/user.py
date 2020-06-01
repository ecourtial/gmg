""" User entity for the GMG project """
import json

class User:
    """ This class represent a user"""
    def __init__(
            self,
            user_id,
            email,
            salt,
            password,
            status,
            user_name,
            is_authenticated
    ):
        self.user_id = user_id
        self.email = email
        self.salt = salt
        self.password = password
        self.status = status,
        self.user_name = user_name
        self.authenticated = is_authenticated

    def get_id(self):
        """Return the id of the user, for instance "125"."""

        return self.user_id

    def get_email(self):
        """Return the email of the user."""

        return self.email

    def get_salt(self):
        """Return the salt of the user's password."""

        return self.salt

    def get_password(self):
        """Return the user's password."""

        return self.password

    def is_active(self):
        """Return the user's status."""
        if self.status[0] == 1 or self.status == 1:
            return True
        return False

    def get_user_name(self):
        return self.user_name

    def is_authenticated(self):
        return self.authenticated

    def set_email(self, email):
        """Set the user's email"""
        self.email = email

    def set_password(self, password):
        """Set the user's password"""
        self.password = password
