from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Version(AbstractEntity):
    """ This class represent a version of a game, e.g the PC version of Monkey Island IV """
    # If you change the order here, you need to also change it in the constructor!
    expected_fields: dict[str, Any] = {
        'platformId':
            {'field': 'platform_id',
            'method': '_platform_id',
            'required': True,
            'type': 'int'
        },
        'gameId': {
            'field': 'game_id',
            'method': '_game_id',
            'required': True,
            'type': 'int'
        },
        'releaseYear': {
            'field': 'release_year',
            'method': '_release_year',
            'required': True,
            'type': 'int'
        },
        'todoSoloSometimes': {
            'field': 'todo_solo_sometimes',
            'method': '_todo_solo_sometimes',
            'required': True,
            'type': 'int'
        },
        'todoMultiplayerSometimes': {
            'field': 'todo_multiplayer_sometimes',
            'method': '_todo_multiplayer_sometimes',
            'required': True,
            'type': 'int'
        },
        'singleplayerRecurring': {
            'field': 'singleplayer_recurring',
            'method': '_singleplayer_recurring',
            'required': True,
            'type': 'int'
        },
        'multiplayerRecurring': {
            'field': 'multiplayer_recurring',
            'method': '_multiplayer_recurring',
            'required': True,
            'type': 'int'
        },
        'toDo': {
            'field': 'to_do',
            'method': '_to_do',
            'required': True,
            'type': 'int'
        },
        'toBuy': {
            'field': 'to_buy',
            'method': '_to_buy',
            'required': True,
            'type': 'int'
        },
        'toWatchBackground': {
            'field': 'to_watch_background',
            'method': '_to_watch_background',
            'required': True,
            'type': 'int'
        },
        'toWatchSerious': {
            'field': 'to_watch_serious',
            'method': '_to_watch_serious',
            'required': True,
            'type': 'int'
        },
        'toRewatch': {
            'field': 'to_rewatch',
            'method': '_to_rewatch',
            'required': True,
            'type': 'int'
        },
        'topGame': {
            'field': 'top_game',
            'method': '_top_game',
            'required': True,
            'type': 'int'
        },
        'hallOfFame': {
            'field': 'hall_of_fame',
            'method': '_hall_of_fame',
            'required': True,
            'type': 'int'
        },
        'hallOfFameYear': {
            'field': 'hall_of_fame_year',
            'method': '_hall_of_fame_year',
            'required': False,
            'type': 'int',
            'default': 0
        },
        'hallOfFamePosition': {
            'field': 'hall_of_fame_position',
            'method': '_hall_of_fame_position',
            'required': False,
            'type': 'int',
            'default': 0
        },
        'playedItOften': {
            'field': 'played_it_often',
            'method': '_played_it_often',
            'required': True,
            'type': 'int'
        },
        'ongoing': {
            'field': 'ongoing',
            'method': '_ongoing',
            'required': True,
            'type': 'int'
        },
        'comments': {
            'field': 'comments',
            'method': '_comments',
            'required': False,
            'type': 'text',
            'default': ''
        },
        'todoWithHelp': {
            'field': 'todo_with_help',
            'method': '_todo_with_help',
            'required': True,
            'type': 'int'
        },
        'bestGameForever': {
            'field': 'bgf',
            'method': '_best_game_forever',
            'required': True,
            'type': 'int'
        },
        'toWatchPosition': {
            'field': 'to_watch_position',
            'method': '_to_watch_position',
            'required': False,
            'type': 'int',
            'default': 0
        },
        'toDoPosition': {
            'field': 'to_do_position',
            'method': '_to_do_position',
            'required': False,
            'type': 'int',
            'default': 0
        },
        'finished': {
            'field': 'finished',
            'method': '_finished',
            'required': False,
            'type': 'int',
            'default': 0
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'version_id', 'origin': 'native', 'type': 'int'},
        'storyCount': {'field': 'storyCount', 'origin': 'computed', 'type': 'int'},
        'copyCount': {'field': 'copyCount', 'origin': 'computed', 'type': 'int'},
        'platformName': {'field': 'platformName', 'origin': 'computed', 'type': 'string'},
        'gameTitle': {'field': 'gameTitle', 'origin': 'computed', 'type': 'string'},
    }

    table_name = 'versions'
    primary_key = 'version_id'

    # If you change the order here, you need to also change it in the array above!
    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
            self,
            entity_id: int | None,
            platform_id: int,
            game_id: int,
            release_year: int,
            todo_solo_sometimes: int,
            todo_multiplayer_sometimes: int,
            singleplayer_recurring: int,
            multiplayer_recurring: int,
            to_do: int,
            to_buy: int,
            to_watch_background: int,
            to_watch_serious: int,
            to_rewatch: int,
            top_game: int,
            hall_of_fame: int,
            hall_of_fame_year: int,
            hall_of_fame_position: int,
            played_it_often: int,
            ongoing: int,
            comments: str,
            todo_with_help: int,
            bgf: int,
            to_watch_position: int,
            to_do_position: int,
            finished: int,
            platform_name: str | None = None,
            game_title: str | None = None,
            story_count: int | None = None,
            copy_count: int | None = None,
    ) -> None:
        self.entity_id = entity_id
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
        self.platform_name = platform_name
        self.game_title = game_title
        self.story_count = story_count
        self.copy_count = copy_count

    def get_id(self) -> int | None:
        return self.entity_id

    def get_platform_id(self) -> int:
        return self.platform_id

    def set_platform_id(self, entity_id: int) -> None:
        self.platform_id = int(entity_id)

    def get_game_id(self) -> int:
        return self.game_id

    def set_game_id(self, entity_id: int) -> None:
        self.game_id = int(entity_id)

    def get_release_year(self) -> int:
        return self.release_year

    def set_release_year(self, year: int) -> None:
        self.release_year = int(year)

    def get_todo_solo_sometimes(self) -> bool:
        return self.todo_solo_sometimes

    def set_todo_solo_sometimes(self, status: int) -> None:
        self.todo_solo_sometimes = bool(status)

    def get_todo_multiplayer_sometimes(self) -> bool:
        return self.todo_multiplayer_sometimes

    def set_todo_multiplayer_sometimes(self, status: int) -> None:
        self.todo_multiplayer_sometimes = bool(status)

    def get_singleplayer_recurring(self) -> bool:
        return self.singleplayer_recurring

    def set_singleplayer_recurring(self, status: int) -> None:
        self.singleplayer_recurring = bool(status)

    def get_multiplayer_recurring(self) -> bool:
        return self.multiplayer_recurring

    def set_multiplayer_recurring(self, status: int) -> None:
        self.multiplayer_recurring = bool(status)

    def get_to_do(self) -> bool:
        return self.to_do

    def set_to_do(self, status: int) -> None:
        self.to_do = bool(status)

    def get_to_buy(self) -> bool:
        return self.to_buy

    def set_to_buy(self, status: int) -> None:
        self.to_buy = bool(status)

    def get_to_watch_background(self) -> bool:
        return self.to_watch_background

    def set_to_watch_background(self, status: int) -> None:
        self.to_watch_background = bool(status)

    def get_to_watch_serious(self) -> bool:
        return self.to_watch_serious

    def set_to_watch_serious(self, status: int) -> None:
        self.to_watch_serious = bool(status)

    def get_to_rewatch(self) -> bool:
        return self.to_rewatch

    def set_to_rewatch(self, status: int) -> None:
        self.to_rewatch = bool(status)

    def get_top_game(self) -> bool:
        return self.top_game

    def set_top_game(self, status: int) -> None:
        self.top_game = bool(status)

    def get_hall_of_fame(self) -> bool:
        return self.hall_of_fame

    def set_hall_of_fame(self, status: int) -> None:
        self.hall_of_fame = bool(status)

    def get_hall_of_fame_year(self) -> int:
        return self.hall_of_fame_year

    def set_hall_of_fame_year(self, year: int) -> None:
        self.hall_of_fame_year = int(year)

    def get_hall_of_fame_position(self) -> int:
        return self.hall_of_fame_position

    def set_hall_of_fame_position(self, position: int) -> None:
        self.hall_of_fame_position = int(position)

    def get_played_it_often(self) -> bool:
        return self.played_it_often

    def set_played_it_often(self, status: int) -> None:
        self.played_it_often = bool(status)

    def get_ongoing(self) -> bool:
        return self.ongoing

    def set_ongoing(self, status: int) -> None:
        self.ongoing = bool(status)

    def get_comments(self) -> str:
        return self.comments

    def set_comments(self, comments: str) -> None:
        self.comments = comments

    def get_todo_with_help(self) -> bool:
        return self.todo_with_help

    def set_todo_with_help(self, status: int) -> None:
        self.todo_with_help = bool(status)

    def get_best_game_forever(self) -> bool:
        return self.bgf

    def set_best_game_forever(self, status: int) -> None:
        self.bgf = bool(status)

    def get_to_watch_position(self) -> int:
        return self.to_watch_position

    def set_to_watch_position(self, position: int) -> None:
        self.to_watch_position = int(position)

    def get_to_do_position(self) -> int:
        return self.to_do_position

    def set_to_do_position(self, position: int) -> None:
        self.to_do_position = int(position)

    def get_platform_name(self) -> str | None:
        return self.platform_name

    def set_platform_name(self, name: str) -> None:
        self.platform_name = name

    def get_game_title(self) -> str | None:
        return self.game_title

    def set_game_title(self, title: str) -> None:
        self.game_title = title

    def get_finished(self) -> bool:
        return self.finished

    def set_finished(self, finished: int) -> None:
        self.finished = bool(finished)

    def get_story_count(self) -> int | None:
        return self.story_count

    def set_story_count(self, story_count: int | None) -> None:
        self.story_count = int(story_count or 0)

    def get_copy_count(self) -> int | None:
        return self.copy_count

    def set_copy_count(self, copy_count: int | None) -> None:
        self.copy_count = int(copy_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()
        values['storyCount'] = self.get_story_count()
        values['copyCount'] = self.get_copy_count()
        return values
