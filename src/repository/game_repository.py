""" Repository to handle the games """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.game import Game

class GameRepository(AbstractRepository):
    def get_by_id(self, platform_id):
        """Get one support by its id."""
        request = "SELECT * FROM games "
        request += "WHERE id = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id,))

    def get_by_title(self, title):
        """Get one support by its title."""
        request = "SELECT * FROM games "
        request += "WHERE title = %s LIMIT 1;"

        return self.fetch_one(request, (title,))

    def insert(self, game):
        """Insert a new game"""
        request = "INSERT INTO games (title, finished) VALUES (%s, %s)"
        self.write(request, (game.get_title(), game.get_finished(),))

        return self.get_by_title(game.get_title())

    def update(self, game):
        """Update a game"""
        request = "UPDATE games SET title = %s, finished = %s WHERE id = %s;"
        self.write(request, (game.get_title(), game.get_finished(), game.get_id()))

        return self.get_by_id(game.get_id())

    def get_versions_count_for_game(self, game_id):
        request = "SELECT COUNT(*) as count FROM versions WHERE game_id = %s"
        
        return self.fetch_cursor(request, (game_id,))
    
    def delete(self, game_id):
        request = "DELETE FROM games WHERE id = %s"
        self.write(request, (game_id,), True)

    def get_list(self, page, limit):
        return self.get_object_list('games', page, limit)

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Game(row['id'], row['title'], row['finished'])
