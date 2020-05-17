""" Game entity for the GMG project """
import json

class Game:
    """ This class represent a game, for instance "The Secret Of Monkey Island" """
    # This class is too big. This is a test project, so we disabled the specific linter rules
    def __init__(
            self,
            game_id,
            title,
            platform,
            todo_solo_sometimes,
            todo_multiplayer_sometimes,
            singleplayer_recurring,
            multiplayer_recurring,
            to_do,
            to_buy,
            to_watch_background,
            to_watch_serious,
            to_rewatch,
            original,
            copy,
            many,
            top_game,
            hall_of_fame,
            hall_of_fame_year,
            hall_of_fame_position,
            played_it_often,
            comments
    ):
        self.game_id = game_id
        self.title = title
        self.platform = platform
        self.todo_solo_sometimes = todo_solo_sometimes
        self.todo_multiplayer_sometimes = todo_multiplayer_sometimes
        self.singleplayer_recurring = singleplayer_recurring
        self.multiplayer_recurring = multiplayer_recurring
        self.to_do = to_do
        self.to_buy = to_buy
        self.to_watch_background = to_watch_background
        self.to_watch_serious = to_watch_serious
        self.to_rewatch = to_rewatch
        self.original = original
        self.copy = copy
        self.many = many
        self.top_game = top_game
        self.hall_of_fame = hall_of_fame
        self.hall_of_fame_year = hall_of_fame_year
        self.hall_of_fame_position = hall_of_fame_position
        self.played_it_often = played_it_often
        self.comments = comments

    def get_game_id(self):
        """Return the id of the game, for instance "125"."""

        return self.game_id

    def get_title(self):
        """Return the title of the game, for instance "Woodruff and the Schnibble of Azimuth"."""

        return self.title

    def get_platform(self):
        """Platform?"""

        return self.platform

    def get_todo_solo_sometimes(self):
        """Is the game to be played sometime in solo?"""

        return self.todo_solo_sometimes

    def get_todo_multiplayer_sometimes(self):
        """Is the game to be played sometime in multi?"""

        return self.todo_multiplayer_sometimes

    def get_singleplayer_recurring(self):
        """Is the game to be played in solo often?."""

        return self.singleplayer_recurring

    def get_multiplayer_recurring(self):
        """Is the game to be played in multiplayer often?"""

        return self.multiplayer_recurring

    def get_to_do(self):
        """Is the game to be done at least once?"""

        return self.to_do

    def get_to_buy(self):
        """Is the game to be bought?"""

        return self.to_buy

    def get_to_watch_background(self):
        """Is the game to be watched in background?"""

        return self.to_watch_background

    def get_to_watch_serious(self):
        """Is the game to be watched seriously?"""

        return self.to_watch_serious

    def get_to_rewatch(self):
        """Is the game to be watched again sometimes?"""

        return self.to_rewatch

    def get_original(self):
        """Is the game on our version of the game an original?"""

        return self.original

    def get_copy(self):
        """Is the game on our version of the game a copy?"""

        return self.copy

    def get_many(self):
        """Do we have many versions of the game?"""

        return self.many

    def get_top_game(self):
        """Is this a top game?"""

        return self.top_game

    def get_hall_of_fame(self):
        """Is this a hall of fame game?"""

        return self.hall_of_fame

    def get_hall_of_fame_year(self):
        """The year when the game was discovered/played"""

        return self.hall_of_fame_year

    def get_hall_of_fame_position(self):
        """The position in the hall of fame of the year"""

        return self.hall_of_fame_position

    def get_played_it_often(self):
        """Did we played this game a lot?"""

        return self.played_it_often

    def get_comments(self):
        """Comments"""

        return self.comments

    def to_json(self):
        """Jsonify the object"""
        return json.dumps(self, default=lambda o: o.__dict__)

    def serialize(self):
        """serialize the object"""
        return {
            'game_id': self.game_id,
            'title': self.title,
            'platform': self.platform,
            'todo_solo_sometimes': self.todo_solo_sometimes,
            'todo_multiplayer_sometimes': self.todo_multiplayer_sometimes,
            'singleplayer_recurring': self.singleplayer_recurring,
            'multiplayer_recurring': self.multiplayer_recurring,
            'to_do': self.to_do,
            'to_buy': self.to_buy,
            'to_watch_background': self.to_watch_background,
            'to_watch_serious': self.to_watch_serious,
            'to_rewatch': self.to_rewatch,
            'original': self.original,
            'copy': self.copy,
            'many': self.many,
            'top_game': self.top_game,
            'hall_of_fame': self.hall_of_fame,
            'hall_of_fame_year': self.hall_of_fame_year,
            'hall_of_fame_position': self.hall_of_fame_position,
            'played_it_often': self.played_it_often,
            'comments': self.comments
        }
