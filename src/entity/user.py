""" User entity for the GMG project """

class User:
    """ This class represent a user"""
    def __init__(self, row):
        self.user_id = row['id']
        self.email = row['email']
        self.salt = row['salt']
        self.password = row['password']
        self.status = int(row['status'])
        self.user_name = row['user_name']
        self.authenticated = False

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
        return self.status == 1

    def get_user_name(self):
        """Returns the username"""
        return self.user_name

    def is_authenticated(self):
        """Is the user authenticated"""
        return self.authenticated
