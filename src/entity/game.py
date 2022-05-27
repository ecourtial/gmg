""" Game entity for the GMG project """
import json

class Game:
    expected_fields = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
    }

    """ This class represent a game, for instance "The Secret Of Monkey Island" """
    def __init__(
            self,
            id,
            title
    ):
        self.id = id
        self.title = title

    def get_id(self):
        """Return the id of the game, for instance "125"."""

        return self.id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title

    def set_title(self, title):
        self.title = title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title
        }
