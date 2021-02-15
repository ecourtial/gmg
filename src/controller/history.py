""" History controller for the GMG project """
from flask import jsonify, request, render_template, session
from src.repository.history_repository import HistoryRepository

class HistoryController:
    """ History controller for the GMG project """
    @classmethod
    def get_list(cls, mysql):
        """Return the whole history."""
        game_repo = HistoryRepository(mysql)
        games_list = game_repo.get_all()
        return jsonify(
            games=[game.serialize() for game in games_list]
        )

    @classmethod
    def add(cls, mysql):
        """Add a new history."""
        if request.method == 'GET':
            platform_repo = PlatformRepository(mysql)
            form = render_template(
                'general/histort-form.html',
                token=session['csrfToken']
            )

            return jsonify(form=form, title="Ajouter un jeu")

        if request.form['_token'] != session['csrfToken']:
            return jsonify(), 400

        title = request.form['title']
        platform_id = request.form['platform']
        if title == '' or platform_id == '':
            return "Form is incomplete"

        platform_repo = PlatformRepository(mysql)
        platform = platform_repo.get_by_id(platform_id)
        if platform is None:
            return "Invalid platform"

        game_repo = GameRepository(mysql)

        return jsonify(id=game_repo.insert(title, platform_id, request.form))