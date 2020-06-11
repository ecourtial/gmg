from flask import Flask, render_template
from mysql import connector
import json
from flask_login import login_required, login_manager
from src.controller.home import HomeController
from src.controller.platforms import PlatformController
from src.controller.games import GameController
from src.controller.user import UserController
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService

# The second parameter is optional. It allows to set the static folder accessible via the root URL instead of via /static/foo
app = Flask(__name__, static_folder='static', static_url_path='')

# Load config
with open('configuration.json') as json_file:
    configurationData = json.load(json_file)

# Init DB connection
mysql = connector.connect(
  host=configurationData['db_host'],
  user=configurationData['db_user'],
  passwd=configurationData['db_password'],
  database=configurationData['database']
)

# Session Manager
app.secret_key = configurationData['secret']
login_manager = login_manager.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user_repo = UserRepository(mysql)
    user = user_repo.get_by_id(user_id)

    if user is None or user.is_active() == False:
        return None

    return user

# Cache management
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Routes
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error/404.html', content_title="Oopsy"), 404

@app.errorhandler(500)
def error(e):
    # note that we set the 500 status explicitly
    return render_template('error/500.html', content_title="Ay No!"), 500

@app.route('/')
def home():    
    controller = HomeController
    return controller.get_app_content()

# Return the hall of fames displayed on the homepage
@app.route('/home-content')
def get_home_content():
    controller = HomeController
    return controller.get_home_content(mysql)

# Return the list of all the platforms
@app.route('/platforms')
def get_platforms():
    controller = PlatformController
    return controller.get_list(mysql)

# Return one given game
@app.route('/games/<int:game_id>')
def get_game(game_id):
    controller = GameController
    return controller.get_by_id(mysql, game_id)

# Return one random game
@app.route('/games/random/<string:filter>')
def get_random(filter):
    controller = GameController
    return controller.get_random(mysql, filter)         

# Return the list of all the games for a given platform
@app.route('/games/platform/<int:platform_id>')
def get_games_for_platform(platform_id):
    controller = GameController
    return controller.get_list_by_platform(mysql, platform_id) 

# Return the list of all the games for to be played often in solo
@app.route('/games/special/<string:filter>')
def get_special_list(filter):
    controller = GameController
    return controller.get_special_list(mysql, filter) 

# Add a new platform
@app.route('/platform/add', methods=['GET', 'POST'])
@login_required
def add_platform():
    controller = PlatformController
    return controller.add(mysql)

# Add a new game
@app.route('/games/add', methods=['GET', 'POST'])
@login_required
def add_game():
    controller = GameController
    return controller.add(mysql) 

# Edit a game
@app.route('/games/edit/<int:game_id>', methods=['GET', 'POST'])
@login_required
def edit_game(game_id):
    controller = GameController
    return controller.edit(mysql, game_id)

# Delete a game
@app.route('/games/delete/<int:game_id>', methods=['DELETE'])
@login_required
def delete_game(game_id):
    controller = GameController
    return controller.delete(mysql, game_id) 

# Routes for session management

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    controller = UserController()
    return controller.register(mysql)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = UserController()
    return controller.login(mysql)

# Edit user profile
@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    controller = UserController()
    return controller.edit(mysql)

# Logout
@app.route('/logout')
@login_required
def logout():
    controller = UserController()
    return controller.logout()
