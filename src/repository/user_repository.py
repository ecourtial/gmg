""" Repository to handle the users """
from src.repository.abstract_repository import AbstractRepository
from src.entity.user import User

class UserRepository(AbstractRepository):
    """ Another useless comment """
    entity = User

    def get_by_email(self, user_email):
        """Gets an user by email"""
        request = self.get_select_request_start() + "AND email = %s;"

        return self.fetch_one(request, (user_email,))

    def get_active_by_token(self, user_token):
        """Gets an user by its token"""
        request = self.get_select_request_start() + "AND token = %s AND status = 1 LIMIT 1;"

        return self.fetch_one(request, (user_token,))

    def get_by_user_name(self,  user_name):
        """Check if a user already exists"""
        request = self.get_select_request_start() + "AND user_name = %s LIMIT 1;"

        return self.fetch_one(request, (user_name,))

    def insert(self, object, commit=True):
        """Inserts an user"""
        request = "INSERT INTO users (email, password, salt, status, user_name, token)"
        request += " VALUES (%s, %s, %s, 0, %s, %s);"
        self.write(
            request,
            (
                object.get_email(),
                object.get_password(),
                object.get_salt(),
                object.get_user_name(),
                object.get_token()
            ),
            commit
        )

        return self.get_by_email(object.get_email())

    def update(self, object, commit=True):
        """Updates an user"""
        request = "UPDATE users SET email = %s, password = %s, status = %s, user_name = %s, token = %s "
        request += "WHERE id = %s;"
        self.write(
            request,
            (
                object.get_email(),
                object.get_password(),
                object.get_is_active(),
                object.get_user_name(),
                object.get_token(),
                object.get_id()
            ),
            commit
        )

        return self.get_by_id(object.get_id())

    def hydrate(self, row):
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
