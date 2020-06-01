""" Repository to handle the users """
from src.repository.abstract_repository import AbstractRepository
from src.entity.user import User

class UserRepository(AbstractRepository):
    """ Another useless comment """

    def get_by_id(self, user_id):
        request = "SELECT * FROM users WHERE id = %s;"

        return self.fetch_one(request, (user_id,))

    def get_by_email(self, user_email):
        request = "SELECT * FROM users WHERE email = %s;"
        
        return self.fetch_one(request, (user_email,))

    def insert(self, email, password, salt, user_name):
        request = "INSERT INTO users (email, password, salt, status, user_name) VALUES (%s, %s, %s, 0, %s);"
        self.write(request, (email, password, salt, user_name))

    def update(self, email_ref, new_email, password):
        request = "UPDATE users SET email = %s, password = %s WHERE email = %s;"
        self.write(request, (new_email, password, email_ref))

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        user = User(
            row['id'],
            row['email'],
            row['salt'],
            row['password'],
            int(row['status']),
            row['user_name'],
            False
        )

        return user