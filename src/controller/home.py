""" Home controller for the GMG project """

from flask import render_template, jsonify, session
from src.repository.platform_repository import PlatformRepository
from src.repository.game_repository import GameRepository

class HomeController:
    """ Contains two methods: one for serving the website, one for the homepage content (async) """
    @classmethod
    def get_app_content(cls):
        """Return the html content (layout)."""
        return render_template(
            'layout.html',
            token=session['csrfToken'],
            show_menu=True,
            title="Give me a game", content_title="Hall of fames"
        )

    @classmethod
    def get_home_content(cls, mysql):
        """Return The payload for the homepage."""
        game_repo = GameRepository(mysql)
        platform_repo = PlatformRepository(mysql)

        hall_of_fame_games = game_repo.get_hall_of_fame_data()

        return jsonify(
            gameCount=game_repo.get_total_count(),
            platformCount=platform_repo.get_total_count(),
            toDoSoloOrToWatch=game_repo.get_count_to_do_solo_or_to_watch(),
            hallOfFameGames=[game.serialize() for game in hall_of_fame_games]
        )
