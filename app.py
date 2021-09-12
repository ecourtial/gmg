"""Main file of the app. Loaded once on server startup!"""
import json
from flask import Flask, render_template
from flask_login import login_required, login_manager
from src.controller.home import HomeController
from src.controller.platforms import PlatformController
from src.controller.games import GameController
from src.controller.user import UserController
from src.controller.history import HistoryController
from src.controller.trading import TradeController
from src.repository.user_repository import UserRepository
from src.connection.mysql_factory import MySQLFactory

# The second parameter is optional.
# It allows to set the static folder accessible via the root URL instead of via /static/foo
app = Flask(__name__, static_folder='static', static_url_path='')

# Load config
with open('configuration.json') as json_file:
    configurationData = json.load(json_file)

# DB connection
MySQLFactory.init(
    configurationData['db_host'],
    configurationData['db_user'],
    configurationData['db_password'],
    configurationData['database']
)

# Session Manager
app.secret_key = configurationData['secret']
login_manager = login_manager.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """Callback to load user"""
    user_repo = UserRepository(MySQLFactory.get())
    user = user_repo.get_by_id(user_id)

    if user is None or user.is_active() is False:
        return None

    return user

# After request: cache management, close DB connection...
@app.after_request
def after_request(response):
    """Handle logic after each request"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"

    MySQLFactory.close()

    return response

# Routes
@app.errorhandler(404)
def page_not_found(exception):
    """Callback for 404"""
    # note that we set the 404 status explicitly
    del exception
    return render_template('error/404.html', content_title="Oopsy"), 404

@app.errorhandler(500)
def error(exception):
    """Callback for 500"""
    # note that we set the 500 status explicitly
    del exception
    return render_template('error/500.html', content_title="Ay No!"), 500

@app.route('/')
def home():
    """Homepage with layout"""
    controller = HomeController
    return controller.get_app_content()

@app.route('/home-content')
def get_home_content():
    """Return the hall of fames displayed on the homepage"""
    controller = HomeController
    return controller.get_home_content(MySQLFactory.get())

@app.route('/platforms')
def get_platforms():
    """Return the list of all the platforms"""
    controller = PlatformController
    return controller.get_list(MySQLFactory.get())

@app.route('/games/<int:game_id>')
def get_game(game_id):
    """Return one given game"""
    controller = GameController
    return controller.get_by_id(MySQLFactory.get(), game_id)

@app.route('/games/random/<string:selector>')
def get_random(selector):
    """Return one random game"""
    controller = GameController
    return controller.get_random(MySQLFactory.get(), selector)

@app.route('/games/platform/<int:platform_id>')
def get_games_for_platform(platform_id):
    """Return the list of all the games for a given platform"""
    controller = GameController
    return controller.get_list_by_platform(MySQLFactory.get(), platform_id)

@app.route('/games/special/<string:selector>')
def get_special_list(selector):
    """Special lists route"""
    controller = GameController
    return controller.get_special_list(MySQLFactory.get(), selector)

@app.route('/platform/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    """Add a new platform"""
    controller = PlatformController
    return controller.add(MySQLFactory.get())

@app.route('/games/add', methods=['GET', 'POST'])
@login_required
def add_game():
    """Adding a new game"""
    controller = GameController
    return controller.add(MySQLFactory.get())

# Edit a game
@app.route('/games/edit/<int:game_id>', methods=['GET', 'POST'])
@login_required
def edit_game(game_id):
    """Game edition"""
    controller = GameController
    return controller.edit(MySQLFactory.get(), game_id)

@app.route('/games/delete/<int:game_id>', methods=['DELETE'])
@login_required
def delete_game(game_id):
    """Game deletion"""
    controller = GameController
    return controller.delete(MySQLFactory.get(), game_id)

# Routes for session management

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route"""
    controller = UserController()
    return controller.register(MySQLFactory.get())

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route"""
    controller = UserController()
    return controller.login(MySQLFactory.get())

@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Profile edition"""
    controller = UserController()
    return controller.edit(MySQLFactory.get())

@app.route('/logout')
@login_required
def logout():
    """Logout"""
    controller = UserController()
    return controller.logout()

# History management
@app.route('/history', methods=['GET'])
def game_history():
    """Games history"""
    controller = HistoryController()
    return controller.get_list(MySQLFactory.get())

@app.route('/history/add', methods=['GET', 'POST'])
@login_required
def add_history():
    """Adding a new history entry"""
    controller = HistoryController
    return controller.add(MySQLFactory.get())

@app.route('/history/delete/<int:entity_id>', methods=['DELETE'])
@login_required
def delete_history(entity_id):
    """History deletion"""
    controller = HistoryController
    return controller.delete(MySQLFactory.get(), entity_id)

# Trading management
@app.route('/trading/history', methods=['GET'])
def trading_history():
    """Trading history"""
    controller = TradeController()
    return controller.get_list(MySQLFactory.get())

@app.route('/trading/add', methods=['GET', 'POST'])
@login_required
def add_trade():
    """Adding a new trading entry"""
    controller = TradeController
    return controller.add(MySQLFactory.get())

@app.route('/trading/delete/<int:entity_id>', methods=['DELETE'])
@login_required
def delete_trade(entity_id):
    """Trading deletion"""
    controller = TradeController
    return controller.delete(MySQLFactory.get(), entity_id)
