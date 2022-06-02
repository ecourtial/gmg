""" User entity for the GMG project """

# NOTE: THIS ENTITY WORKS SLIGHTLY DIFFERENTLY THAN THE OTHERS, FOR SECURITY MATTERS.
# FOR INSTANCE, IT DOES NOT INHERIT FROM THE AbstractEntity, OR ITS REPOSITORY
# DOES NOT INHERIT FROM THE AbstractRepository.
# WE DON'T WANT TO EXPOSE SENSITIVE VALUES
class User:
    """ This class represent a user"""
    expected_fields = {
        'email': {'field': 'email', 'method': '_email', 'required': True, 'type': 'text'},
        'password': {'field': 'password', 'method': '_password', 'required': True, 'type': 'text'},
        'active': {
            'field': 'status',
            'method': '_is_active',
            'required': False,
            'type': 'int',
            'default': 0
        },
        'username': {
            'field': 'user_name',
            'method': '_user_name',
            'required': True,
            'type': 'text'
        },
    }

    authorized_extra_fields_for_filtering = {}

    table_name = 'users'
    primary_key = 'id'

    def __init__(self, entity_id, email, password, status, user_name, salt, token):
        self.user_id = entity_id
        self.email = email
        self.password = password
        self.status = int(status)
        self.user_name = user_name
        self.salt = salt
        self.token = token

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

    def get_is_active(self):
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

    def set_salt(self, salt):
        self.salt = salt

    def set_is_active(self, new_status):
        self.status = int(new_status)

    def set_email(self, new_email):
        self.email = new_email

    def set_user_name(self, new_user_name):
        self.user_name = new_user_name

    def set_password(self, new_password):
        self.password = new_password
