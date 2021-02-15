""" Repository to handle the games watched or played """
from src.repository.abstract_repository import AbstractRepository
from src.entity.history import History

class HistoryRepository(AbstractRepository):
    """ Another useless comment """

    def get_all(self):
        """Gets all the history"""
        request = "SELECT history.game_id as game_id, history.year as year, games.title as title FROM history, games WHERE history.game_id = games.id ORDER BY year, title;"

        return self.fetch_multiple(request, ())

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        history = History (
            row['game_id'],
            row['title'],
            row['year']
        )

        return history
