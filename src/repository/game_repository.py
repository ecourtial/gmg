""" Repository to handle the games """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.game import Game
from src.entity.version import Version

class GameRepository(AbstractRepository):
    def get_by_id(self, game_id):
        """Get one game by its id."""
        request = f"SELECT * FROM {Game.table_name} "
        request += f"WHERE {Game.primary_key} = %s LIMIT 1;"

        return self.fetch_one(request, (game_id,))

    def get_by_title(self, title):
        """Get one support by its title."""
        request = f"SELECT * FROM {Game.table_name} "
        request += "WHERE title = %s LIMIT 1;"

        return self.fetch_one(request, (title,))

    def insert(self, game):
        super().insert(game)

        return self.get_by_title(game.get_title())

    def update(self, game):
        super().update(game)

        return self.get_by_id(game.get_id())

    def get_versions_count_for_game(self, game_id):
        request = f"SELECT COUNT(*) as count FROM {Version.table_name} WHERE game_id = %s"
        
        return self.fetch_cursor(request, (game_id,))
    
    def delete(self, game_id):
        request = f"DELETE FROM {Game.table_name} WHERE id = %s"
        self.write(request, (game_id,), True)

    def get_list(self, page, limit):
        return self.get_object_list('games', page, limit)

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Game(row['id'], row['title'], row['finished'])
