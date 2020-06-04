""" Repository to handle the games """
from src.repository.abstract_repository import AbstractRepository
from src.entity.game import Game
from src.exception.unknown_filter_exception import UnknownFilterException

class GameRepository(AbstractRepository):
    """ Another useless comment """

    authorized_fields = [
        'singleplayer_recurring',
        'multiplayer_recurring',
        'todo_solo_sometimes',
        'todo_multiplayer_sometimes',
        'to_do',
        'to_buy',
        'to_watch_background',
        'to_watch_serious',
        'to_rewatch',
        'to_buy',
        'original'
    ]

    random_cases = [
        'singleplayer_random',
        'multiplayer_random'
    ]

    @classmethod
    def get_main_request_start(cls, meta=False):
        """ Return the first part of the most used request """
        start = "SELECT games.*, platforms.name as platform"

        if meta:
            start += ", games_meta.*"

        start += " FROM games, platforms"

        if meta:
            start += ", games_meta"

        start += " WHERE "

        return start

    @classmethod
    def get_main_request_end(cls, meta=False):
        """ Return the last part of the most used request """
        end = " AND games.platform = platforms.id"
        if meta:
            end += " AND games.id = games_meta.game_id"

        end += " ORDER BY title;"

        return end

    def get_by_id(self, game_id):
        """Get one."""
        request = self.get_main_request_start(True)  + "games.id = %s"
        request += self.get_main_request_end(True)
        return self.fetch_one(request, (game_id,))

    def get_random(self, random_filter):
        """Get one random."""
        if random_filter not in self.random_cases:
            message = "Sorry, unauthorized random filter: " + random_filter
            raise UnknownFilterException(message)

        if random_filter == 'singleplayer_random':
            request_filter = "(todo_solo_sometimes = 1 OR to_do = 1 OR singleplayer_recurring = 1)"
        else:
            request_filter = "(todo_multiplayer_sometimes = 1 OR multiplayer_recurring = 1)"

        request = self.get_main_request_start(True) + request_filter
        request += ' AND games.platform = platforms.id '
        request += 'AND games.id = games_meta.game_id ORDER BY RAND() LIMIT 1;'

        return self.fetch_one(request, ())

    def get_list_by_platform(self, platform_id):
        """The list of games for a given plaform."""
        request = self.get_main_request_start(True)  + "platform = %s"
        request += self.get_main_request_end(True)

        return self.fetch_multiple(request, (platform_id,))

    def get_special_list(self, field):
        """The list of games to do."""
        if field not in self.authorized_fields:
            message = "Sorry, unauthorized field: " + field
            raise UnknownFilterException(message)
        request = self.get_main_request_start(True) + "games_meta."
        request += field + " = 1" + self.get_main_request_end(True)

        return self.fetch_multiple(request, ())

    def get_search(self, query):
        """The list of games for which the title is related to the request."""
        request = self.get_main_request_start(True) + "games.title LIKE %s"
        request += self.get_main_request_end(True)
        return self.fetch_multiple(request, ("%" + query + "%",))

    def get_total_count(self):
        """Get the total count of games registered in the app."""
        request = "SELECT COUNT(*) as total FROM games;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_count_to_do_solo_or_to_watch(self):
        """Get the total count of games to do solo or to watch."""
        request = "SELECT COUNT(*) as total FROM games, games_meta "
        request += "WHERE games_meta.todo_solo_sometimes = 1 "
        request += "OR games_meta.to_do = 1 OR games_meta.to_watch_background =1"
        request += " OR games_meta.to_watch_serious = 1;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_hall_of_fame_data(self):
        """Get the hall of fame data."""
        request = self.get_main_request_start(True)
        request += ' games_meta.game_id = games.id AND games_meta.hall_of_fame = 1'
        request += " AND games.platform = platforms.id"
        request += ' ORDER BY games_meta.hall_of_fame_year, games_meta.hall_of_fame_position'
        return self.fetch_multiple(request, ())

    def insert(self, title, platform, form_content):
        """Insert a new game"""
        request = "INSERT INTO games (title, platform) VALUES (%s, %s)"
        game_id = self.write(request, (title, platform), False)

        meta = (
            game_id,
            form_content['todo_solo_sometimes'],
            form_content['todo_multiplayer_sometimes'],
            form_content['singleplayer_recurring'],
            form_content['multiplayer_recurring'],
            form_content['to_do'],
            form_content['to_buy'],
            form_content['to_watch_background'],
            form_content['to_watch_serious'],
            form_content['to_rewatch'],
            form_content['original'],
            form_content['copy'],
            form_content['many'],
            form_content['top_game'],
            form_content['hall_of_fame'],
            form_content['hall_of_fame_year'],
            form_content['hall_of_fame_position'],
            form_content['played_it_often'],
            form_content['comments'],
        )

        request = "INSERT INTO games_meta (game_id,"
        request += "todo_solo_sometimes, todo_multiplayer_sometimes,"
        request += "singleplayer_recurring, multiplayer_recurring,"
        request += "to_do, to_buy, to_watch_background,"
        request += "to_watch_serious, to_rewatch,"
        request += "original, copy,"
        request += "many, top_game,"
        request += "hall_of_fame, hall_of_fame_year,"
        request += "hall_of_fame_position, played_it_often, comments) "
        request += "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.write(request, meta)

        return game_id

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        game = Game(
            row['id'],
            row['title'],
            row['platform']
        )

        row.pop('id', None)
        row.pop('title', None)
        row.pop('platform', None)

        game.set_meta(row)

        return game
