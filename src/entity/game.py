""" Game entity for the GMG project """
class Game:
    """ This class represent a game, for instance "The Secret Of Monkey Island" """

    def __init__(self, game_id, title):
        self.game_id = game_id
        self.title = title

    def get_game_id(self):
        """Return the id of the game, for instance "125"."""

        return self.game_id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title
