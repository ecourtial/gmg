""" Repository to handle trading """
from src.repository.abstract_repository import AbstractRepository
from src.entity.trade import Trade

class TradeRepository(AbstractRepository):
    """ Another useless comment """

    def get_all(self):
        """Gets all the trading entries."""
        request = "SELECT trades.id as id, trades.game_id as game_id, trades.year as year,"
        request += " trades.month as month, trades.day as day, trades.type as type,"
        request += " games.title as title, platforms.name as platform"
        request += " FROM trades,games, platforms"
        request += " WHERE trades.game_id = games.id AND games.platform = platforms.id"
        request += " ORDER BY year, month, day"

        return self.fetch_multiple(request, ())

    def insert(self, game_id, year, month, day, operation):
        """Insert a new trading entry"""
        request = "INSERT INTO trades (game_id, year, month, day, type) "
        request += "VALUES (%s,%s,%s,%s,%s)"
        return self.write(request, (game_id, year, month, day, operation,))

    def delete(self, entity_id):
        """Delete a trade entry"""

        request = "DELETE FROM trades WHERE id=%s"
        self.write(request, (entity_id,))

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        print(row, flush=True)
        trade = Trade(
            row['id'],
            row['game_id'],
            row['title'],
            row['platform'],
            row['year'],
            row['month'],
            row['day'],
            row['type']
        )

        return trade
