""" Game entity for the GMG project """
import json

class Game:
    """ This class represent a game, for instance "The Secret Of Monkey Island" """
    def __init__(
            self,
            game_id,
            title,
            platform
    ):
        self.game_id = game_id
        self.title = title
        self.platform = platform
        self.meta = []

    def get_game_id(self):
        """Return the id of the game, for instance "125"."""

        return self.game_id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title

    def get_platform(self):
        """Platform?"""

        return self.platform

    def get_meta(self):
        """Return metadata"""

        return self.meta

    def set_meta(self, meta):
        """Set the metadata"""
        self.meta = meta

    def to_json(self):
        """Jsonify the object"""
        return json.dumps(self, default=lambda o: o.__dict__)

    def serialize(self):
        """serialize the object"""
        return {
            'game_id': self.game_id,
            'title': self.title,
            'platform': self.platform.get_platform_id(),
            'platform_name': self.platform.get_name(),
            'meta' : self.meta
        }
