""" Repository to handle the games watched or played """
from src.repository.abstract_repository import AbstractRepository
from src.entity.history import History

class HistoryRepository(AbstractRepository):
    """ Another useless comment """

    def get_all(self):
        """Gets all the history."""
        request = "SELECT history.id as id, history.game_id as game_id, history.year as year"
        request += ", history.position as position, games.title as title, history.watched"
        request += ", history.played FROM history, games"
        request += " WHERE history.game_id = games.id ORDER BY year, position"

        return self.fetch_multiple(request, ())

    def insert(self, game_id, year, position, watched, played):
        """Insert a new history entry"""
        request = "INSERT INTO history (game_id, year, position, watched, played) "
        request += "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        return self.write(request, (game_id, year, position, watched, played,))

    def delete(self, entity_id):
        """Delete a history entry"""

        request = "DELETE FROM history WHERE id=%s"
        self.write(request, (entity_id,))

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        history = History(
            row['id'],
            row['game_id'],
            row['title'],
            row['year'],
            row['position'],
            row['watched'],
            row['played']
        )

        return history
