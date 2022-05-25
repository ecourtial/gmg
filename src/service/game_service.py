from src.repository.game_repository import GameRepository

class GameService:
    def __init__(self, mysql):
        self.game_repository = GameRepository(mysql)

    def create(self, title):
        """Create a game"""
        checkGame = self.game_repository.get_by_title(title)
        if checkGame is not None:
            return 'title'

        return self.game_repository.insert(title)

    def update(self, game):
        """Update a game"""
        checkGame = self.game_repository.get_by_title(game.get_title())
        if checkGame is not None:
            return 'title'

        return self.game_repository.update(game)

    def delete(self, game):
        """Delete a game"""
        count = self.game_repository.get_versions_count_for_game(game.get_id())['count']

        if count > 0:
            return False

        self.game_repository.delete(game.get_id())

        return True
