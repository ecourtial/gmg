""" Trading controller for the GMG project """
from flask import jsonify, request, render_template, session
from src.repository.trade_repository import TradeRepository

class TradeController:
    """ Trading controller for the GMG project """
    @classmethod
    def get_list(cls, mysql):
        """Return the whole trading history."""
        trade_repo = TradeRepository(mysql)
        games_list = trade_repo.get_all()
        return jsonify(
            games=[game.serialize() for game in games_list]
        )

    @classmethod
    def add(cls, mysql):
        """Add a new trade."""
        if request.method == 'GET':
            form = render_template(
                'general/trading-history-form.html',
                token=session['csrfToken']
            )

            return jsonify(form=form, title="Ajouter une transaction")

        if request.form['_token'] != session['csrfToken']:
            return jsonify(), 400

        game_id = request.form['game_id']
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        operation = request.form['type']

        if game_id == '' or year == '' or month == '' or day == '' or operation == '':
            return "Form is incomplete"

        trade_repo = TradeRepository(mysql)
        trade_repo.insert(game_id, year, month, day, operation)

        return jsonify(), 200

    @classmethod
    def delete(cls, mysql, entry_id):
        """Delete a trading entry."""
        if request.form['_token'] != session['csrfToken']:
            return jsonify(), 400

        history_repo = TradeRepository(mysql)
        history_repo.delete(entry_id)

        return jsonify(), 204
