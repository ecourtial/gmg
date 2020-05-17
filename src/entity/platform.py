""" Platform entity for the GMG project """
import json

class Platform:
    """ This class represent a platform (support), for instance "Playstation" """

    def __init__(self, platform_id, platform_name, game_count):
        self.platform_id = platform_id
        self.platform_name = platform_name
        self.game_count = game_count

    def get_platform_id(self):
        """Return the id of the platform, for instance "3"."""
        return self.platform_id

    def get_name(self):
        """Return the name of the platform, for instance "Playstation 2"."""
        return self.platform_name

    def get_game_count(self):
        """Return qty of games on this platform."""
        return self.game_count

    def to_json(self):
        """Jsonify the object"""
        return json.dumps(self, default=lambda o: o.__dict__)

    def serialize(self):
        """serialize the object"""
        return {
            'platform_id': self.platform_id,
            'platform_name': self.platform_name,
            'game_count': self.game_count,
        }
