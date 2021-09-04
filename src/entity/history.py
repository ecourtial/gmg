""" History entity for the GMG project """
import json

class History:
    """ This class represent a history entry, for instance I watched or played this game in 2021 """
    def __init__(
            self,
            entity_id,
            game_id,
            title,
            year,
            position,
            watched,
            played
    ):
        self.entity_id = entity_id
        self.game_id = game_id
        self.title = title
        self.year = year
        self.position = position
        self.watched = watched
        self.played = played

    def get_id(self):
        """Return the id entry."""

        return self.entity_id

    def get_game_id(self):
        """Return the id of the game, for instance "125"."""

        return self.game_id

    def get_title(self):
        """Return the title of the game, for instance "Fifa 98"."""

        return self.title

    def get_year(self):
        """Return the year."""

        return self.year

    def get_position(self):
        """Return the order for the given year."""

        return self.position

    def get_watched(self):
        """Did you watched a playthrough?"""

        return self.watched

    def get_played(self):
        """Did you played at it?"""

        return self.played

    def to_json(self):
        """Jsonify the object"""
        return json.dumps(self, default=lambda o: o.__dict__)

    def serialize(self):
        """serialize the object"""
        return {
            'id': self.entity_id,
            'game_id': self.game_id,
            'title': self.title,
            'year': self.year,
            'position': self.position,
            'watched': self.watched,
            'played': self.played
        }
