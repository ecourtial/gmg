from src.entity.abstract_entity import AbstractEntity

class Version(AbstractEntity):
    """ This class represent a version of a game, for instance, the PC version of Monkey Island IV """
    # If you change the order here, you need to also change it in the constructor!
    expected_fields = {
        'platformId': {'field': 'platform_id', 'method': '_platform_id', 'required': True, 'type': 'int'},
        'gameId': {'field': 'game_id', 'method': '_game_id', 'required': True, 'type': 'int'},
        'releaseYear': {'field': 'release_year', 'method': '_release_year', 'required': True, 'type': 'int'},
        'todoSoloSometimes': {'field': 'todo_solo_sometimes', 'method': '_todo_solo_sometimes', 'required': True, 'type': 'int'},
        'todoMultiplayerSometimes': {'field': 'todo_multiplayer_sometimes', 'method': '_todo_multiplayer_sometimes', 'required': True, 'type': 'int'},
        'singleplayerRecurring': {'field': 'singleplayer_recurring', 'method': '_singleplayer_recurring', 'required': True, 'type': 'int'},
        'multiplayerRecurring': {'field': 'multiplayer_recurring', 'method': '_multiplayer_recurring', 'required': True, 'type': 'int'},
        'toDo': {'field': 'to_do', 'method': '_to_do', 'required': True, 'type': 'int'},
        'toBuy': {'field': 'to_buy', 'method': '_to_buy', 'required': True, 'type': 'int'},
        'toWatchBackground': {'field': 'to_watch_background', 'method': '_to_watch_background', 'required': True, 'type': 'int'},
        'toWatchSerious': {'field': 'to_watch_serious', 'method': '_to_watch_serious', 'required': True, 'type': 'int'},
        'toRewatch': {'field': 'to_rewatch', 'method': '_to_rewatch', 'required': True, 'type': 'int'},
        'topGame': {'field': 'top_game', 'method': '_top_game', 'required': True, 'type': 'int'},
        'hallOfFame': {'field': 'hall_of_fame', 'method': '_hall_of_fame', 'required': True, 'type': 'int'},
        'hallOfFameYear': {'field': 'hall_of_fame_year', 'method': '_hall_of_fame_year', 'required': False, 'type': 'int', 'default': 0},
        'hallOfFamePosition': {'field': 'hall_of_fame_position', 'method': '_hall_of_fame_position', 'required': False, 'type': 'int', 'default': 0},
        'playedItOften': {'field': 'played_it_often', 'method': '_played_it_often', 'required': True, 'type': 'int'},
        'ongoing': {'field': 'ongoing', 'method': '_ongoing', 'required': True, 'type': 'int'},
        'comments': {'field': 'comments', 'method': '_comments', 'required': False, 'type': 'text', 'default': ''},
        'todoWithHelp': {'field': 'todo_with_help', 'method': '_todo_with_help', 'required': True, 'type': 'int'},
        'bestGameForever': {'field': 'bgf', 'method': '_best_game_forever', 'required': True, 'type': 'int'},
        'toWatchPosition': {'field': 'to_watch_position', 'method': '_to_watch_position', 'required': False, 'type': 'int', 'default': 0},
        'toDoPosition': {'field': 'to_do_position', 'method': '_to_do_position', 'required': False, 'type': 'int', 'default': 0},
        'finished': {'field': 'finished', 'method': '_finished', 'required': False, 'type': 'int', 'default': 0},
    }

    authorized_extra_fields_for_filtering = {
        'gameTitle',
        'platformName',
        'version_id',
    }

    table_name = 'versions'
    primary_key = 'version_id'

    # If you change the order here, you need to also change it in the array above!
    def __init__(
            self,
            id,
            platform_id,
            game_id,
            release_year,
            todo_solo_sometimes,
            todo_multiplayer_sometimes,
            singleplayer_recurring,
            multiplayer_recurring,
            to_do,
            to_buy,
            to_watch_background,
            to_watch_serious,
            to_rewatch,
            top_game,
            hall_of_fame,
            hall_of_fame_year,
            hall_of_fame_position,
            played_it_often,
            ongoing,
            comments,
            todo_with_help,
            bgf,
            to_watch_position,
            to_do_position,
            finished
    ):
        self.id = id
        self.platform_id = int(platform_id)
        self.game_id = int(game_id)
        self.release_year = int(release_year)
        self.todo_solo_sometimes = bool(todo_solo_sometimes)
        self.todo_multiplayer_sometimes = bool(todo_multiplayer_sometimes)
        self.singleplayer_recurring = bool(singleplayer_recurring)
        self.multiplayer_recurring = bool(multiplayer_recurring)
        self.to_do = bool(to_do)
        self.to_buy = bool(to_buy)
        self.to_watch_background = bool(to_watch_background)
        self.to_watch_serious = bool(to_watch_serious)
        self.to_rewatch = bool(to_rewatch)
        self.top_game = bool(top_game)
        self.hall_of_fame = bool(hall_of_fame)
        self.hall_of_fame_year = int(hall_of_fame_year)
        self.hall_of_fame_position = int(hall_of_fame_position)
        self.played_it_often = bool(played_it_often)
        self.ongoing = bool(ongoing)
        self.comments = comments
        self.todo_with_help = bool(todo_with_help)
        self.bgf = bool(bgf)
        self.to_watch_position = int(to_watch_position)
        self.to_do_position = int(to_do_position)
        self.finished = bool(finished)

    def get_id(self):
        return self.id

    def get_platform_id(self):
        return self.platform_id

    def set_platform_id(self, id):
        self.platform_id = int(id)

    def get_game_id(self):
        return self.game_id

    def set_game_id(self, id):
        self.game_id = int(id)

    def get_release_year(self):
        return self.release_year

    def set_release_year(self, year):
        self.release_year = int(year)

    def get_todo_solo_sometimes(self):
        return self.todo_solo_sometimes

    def set_todo_solo_sometimes(self, status):
        self.todo_solo_sometimes = bool(status)

    def get_todo_multiplayer_sometimes(self):
        return self.todo_multiplayer_sometimes

    def set_todo_multiplayer_sometimes(self, status):
        self.todo_multiplayer_sometimes = bool(status)

    def get_singleplayer_recurring(self):
        return self.singleplayer_recurring

    def set_singleplayer_recurring(self, status):
        self.singleplayer_recurring = bool(status)

    def get_multiplayer_recurring(self):
        return self.multiplayer_recurring

    def set_multiplayer_recurring(self, status):
        self.multiplayer_recurring = bool(status)

    def get_to_do(self):
        return self.to_do

    def set_to_do(self, status):
        self.to_do = bool(status)

    def get_to_buy(self):
        return self.to_buy

    def set_to_buy(self, status):
        self.to_buy = bool(status)

    def get_to_watch_background(self):
        return self.to_watch_background

    def set_to_watch_background(self, status):
        self.to_watch_background = bool(status)

    def get_to_watch_serious(self):
        return self.to_watch_serious

    def set_to_watch_serious(self, status):
        self.to_watch_serious = bool(status)

    def get_to_rewatch(self):
        return self.to_rewatch

    def set_to_rewatch(self, status):
        self.to_rewatch = bool(status)

    def get_top_game(self):
        return self.top_game

    def set_top_game(self, status):
        self.top_game = bool(status)

    def get_hall_of_fame(self):
        return self.hall_of_fame

    def set_hall_of_fame(self, status):
        self.hall_of_fame = bool(status)

    def get_hall_of_fame_year(self):
        return self.hall_of_fame_year

    def set_hall_of_fame_year(self, year):
        self.hall_of_fame_year = int(year)

    def get_hall_of_fame_position(self):
        return self.hall_of_fame_position

    def set_hall_of_fame_position(self, position):
        self.hall_of_fame_position = int(position)

    def get_played_it_often(self):
        return self.played_it_often

    def set_played_it_often(self, status):
        self.played_it_often = bool(status)

    def get_ongoing(self):
        return self.ongoing

    def set_ongoing(self, status):
        self.ongoing = bool(status)

    def get_comments(self):
        return self.comments

    def set_comments(self, comments):
        self.comments = comments

    def get_todo_with_help(self):
        return self.todo_with_help

    def set_todo_with_help(self, status):
        self.todo_with_help = bool(status)

    def get_best_game_forever(self):
        return self.bgf

    def set_best_game_forever(self, status):
        self.bgf = bool(status)

    def get_to_watch_position(self):
        return self.to_watch_position

    def set_to_watch_position(self, position):
        self.to_watch_position = int(position)

    def get_to_do_position(self):
        return self.to_do_position

    def set_to_do_position(self, position):
        self.to_do_position = int(position)

    def get_platform_name(self):
        return self.platform_name

    def set_platform_name(self, name):
        self.platform_name = name

    def get_game_title(self):
        return self.game_title

    def set_game_title(self, title):
        self.game_title = title

    def get_finished(self):
        return self.finished

    def set_finished(self, finished):
        self.finished = bool(finished)

    def serialize(self):
        values = super().serialize()

        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()

        return values
