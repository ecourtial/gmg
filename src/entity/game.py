""" Game entity for the GMG project """

class Game:
    expected_fields = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
        'finished': {'field': 'finished', 'method': '_finished', 'required': True, 'type': 'int'},
    }

    authorized_extra_fields_for_filtering = {}

    table_name = 'games'
    primary_key = 'id'

    """ This class represent a game, for instance "The Secret Of Monkey Island" """
    def __init__(
            self,
            id,
            title,
            finished
    ):
        self.id = id
        self.title = title
        self.finished = bool(finished)

    def get_id(self):
        """Return the id of the game, for instance "125"."""

        return self.id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title

    def set_title(self, title):
        self.title = title

    def get_finished(self):
        return self.finished

    def set_finished(self, finished):
        self.finished = bool(finished)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'finished': self.finished
        }
