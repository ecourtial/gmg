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
        self.token = row['token']

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

    def get_token(self):
        """Returns the user's API token"""
        return self.token

    def set_token(self, new_token):
        self.token = new_token

    def set_status(self, new_status):
        self.status = int(new_status)

    def set_email(self, new_email):
        self.email = new_email

    def set_user_name(self, new_user_name):
        self.user_name = new_user_name

    def set_password(self, new_password):
        self.password = new_password
