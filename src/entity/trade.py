""" Trading entity for the GMG project """
import json

class Trade:
    """ This class represent a trading entry, for instance I sell or bought a game """
    def __init__(
            self,
            entity_id,
            game_id,
            title,
            platform,
            year,
            month,
            day,
            operation
    ):
        self.entity_id = entity_id
        self.game_id = game_id
        self.title = title
        self.platform = platform
        self.year = year
        self.month = month
        self.day = day
        self.type = operation

    def get_id(self):
        """Return the id entry."""

        return self.entity_id

    def get_game_id(self):
        """Return the id of the game, for instance "125"."""

        return self.game_id

    def get_title(self):
        """Return the title of the game, for instance "Fifa 98"."""

        return self.title

    def get_platform(self):
        """Platform?"""

        return self.platform

    def get_year(self):
        """Return the year"""

        return self.year

    def get_month(self):
        """Return the month."""

        return self.month

    def get_day(self):
        """Return the day."""

        return self.day

    def get_type(self):
        """0: sold, 1: bought"""

        return self.type

    def to_json(self):
        """Jsonify the object"""
        return json.dumps(self, default=lambda o: o.__dict__)

    def serialize(self):
        """serialize the object"""
        return {
            'id': self.entity_id,
            'game_id': self.game_id,
            'title': self.title,
            'platform': self.platform,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'type': self.type
        }
