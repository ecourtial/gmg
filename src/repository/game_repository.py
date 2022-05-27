""" Repository to handle the games """
from itertools import count
from src.repository.abstract_repository import AbstractRepository
from src.entity.game import Game
from src.entity.version import Version

class GameRepository(AbstractRepository):
    entity = Game

    def get_by_title(self, title):
        """Get one support by its title."""
        request = self.get_select_request_start() + "AND title = %s LIMIT 1;"

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

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Game(row['id'], row['title'], row['finished'])
