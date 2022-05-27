""" Repository to handle the users """
from src.repository.abstract_repository import AbstractRepository
from src.entity.user import User

class UserRepository(AbstractRepository):
    """ Another useless comment """

    def get_by_id(self, user_id):
        """Gets an user by id"""
        request = "SELECT * FROM users WHERE id = %s;"

        return self.fetch_one(request, (user_id,))

    def get_by_email(self, user_email):
        """Gets an user by email"""
        request = "SELECT * FROM users WHERE email = %s;"

        return self.fetch_one(request, (user_email,))

    def get_active_by_token(self, user_token):
        """Gets an user by its token"""
        request = "SELECT * FROM users WHERE token = %s AND status = 1 LIMIT 1;"

        return self.fetch_one(request, (user_token,))

    def get_by_user_name(self,  user_name):
        """Check if a user already exists"""
        request = "SELECT * FROM users WHERE user_name = %s LIMIT 1;"

        return self.fetch_one(request, (user_name,))

    def insert(self, user):
        """Inserts an user"""
        request = "INSERT INTO users (email, password, salt, status, user_name, token)"
        request += " VALUES (%s, %s, %s, 0, %s, %s);"
        self.write(request, (user.get_email(), user.get_password(), user.get_salt(), user.get_user_name(), user.get_token()))
        
        return self.get_by_email(user.get_email())

    def update(self, user):
        """Updates an user"""
        request = "UPDATE users SET email = %s, password = %s, status = %s, user_name = %s, token = %s WHERE id = %s;"
        self.write(request, (user.get_email(), user.get_password(), user.get_is_active(), user.get_user_name(), user.get_token(), user.get_id()))

        return self.get_by_id(user.get_id())

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        user = User(
            row['id'],
            row['email'],
            row['password'],
            row['status'],
            row['user_name'],
            row['salt'],
            row['token'],
        )

        return user
