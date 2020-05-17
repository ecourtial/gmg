""" Repository to handle the games """
from src.entity.game import Game

class GameRepository:
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

    main_request_start = "SELECT games.*, platforms.name as platform FROM games, platforms WHERE "
    main_request_end = " AND games.platform = platforms.id ORDER BY title;"

    def __init__(self, mysql):
        self.mysql = mysql

    def get_by_id(self, game_id):
        """Get one."""
        request = self.main_request_start  + "games.id = %s" + self.main_request_end
        data_tuple = (game_id,)
        return self.fetch_one(request, data_tuple)

    def get_random(self, random_filter):
        """Get one random."""
        if random_filter not in self.random_cases:
            message = "Sorry, unauthorized random filter: " + random_filter
            raise Exception(message)

        if random_filter == 'singleplayer_random':
            request_filter = "(todo_solo_sometimes = 1 OR to_do = 1 OR singleplayer_recurring = 1)"
        else:
            request_filter = "(todo_multiplayer_sometimes = 1 OR multiplayer_recurring = 1)"

        request = self.main_request_start + request_filter + ' AND games.platform = platforms.id '
        request += 'ORDER BY RAND() LIMIT 1;'
        data_tuple = ()
        return self.fetch_one(request, data_tuple)

    def get_list_by_platform(self, platform_id):
        """The list of games for a given plaform."""
        request = "SELECT * FROM games WHERE platform = %s ORDER BY title;"
        data_tuple = (platform_id,)
        return self.fetch_multiple(request, data_tuple)

    def get_special_list(self, field):
        """The list of games to do."""
        if field not in self.authorized_fields:
            message = "Sorry, unauthorized field: " + field
            raise Exception(message)
        request = self.main_request_start + field + " = 1" + self.main_request_end
        data_tuple = ()
        return self.fetch_multiple(request, data_tuple)

    def get_search(self, query):
        """The list of games for which the title is related to the request."""
        request = self.main_request_start + "games.title LIKE %s" + self.main_request_end
        data_tuple = ("%" + query + "%",)
        return self.fetch_multiple(request, data_tuple)

    def get_total_count(self):
        """Get the total count of games registered in the app."""
        request = "SELECT COUNT(*) as total FROM games;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_count_to_do_solo_or_to_watch(self):
        """Get the total count of games to do solo or to watch."""
        request = "SELECT COUNT(*) as total FROM games WHERE todo_solo_sometimes = 1 "
        request += "OR to_do = 1 OR to_watch_background =1 OR to_watch_serious = 1;"
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request)
        row = cursor.fetchone()
        return row['total']

    def get_hall_of_fame_data(self):
        """Get the hall of fame data."""
        request = self.main_request_start
        request += ' hall_of_fame = 1 AND games.platform = platforms.id'
        request += ' ORDER BY hall_of_fame_year, hall_of_fame_position'
        data_tuple = ()
        return self.fetch_multiple(request, data_tuple)

    def fetch_one(self, request, data_tuple):
        """Fetch one result from a given request."""
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()

        if row is None:
            return None

        return self.hydrate(row)

    def fetch_multiple(self, request, data_tuple):
        """Fetch mutliple games and return a list of games."""
        games_list = []
        cursor = self.mysql.cursor(dictionary=True, buffered=True)
        cursor.execute(request, data_tuple)

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            games_list.append(self.hydrate(row))

        cursor.close()
        return games_list

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        return Game(
            row['id'],
            row['title'],
            row['platform'],
            row['todo_solo_sometimes'],
            row['todo_multiplayer_sometimes'],
            row['singleplayer_recurring'],
            row['multiplayer_recurring'],
            row['to_do'],
            row['to_buy'],
            row['to_watch_background'],
            row['to_watch_serious'],
            row['to_rewatch'],
            row['original'],
            row['copy'],
            row['many'],
            row['top_game'],
            row['hall_of_fame'],
            row['hall_of_fame_year'],
            row['hall_of_fame_position'],
            row['played_it_often'],
            row['comments']
        )
