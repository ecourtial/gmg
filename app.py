from flask import Flask, render_template
from mysql import connector
import json
from src.controller.home import HomeController
from src.controller.platforms import PlatformController
from src.controller.games import GameController

# The secon parameter is optional. It allows to set the static folder accessible via the root URL instead of via /static/foo
app = Flask(__name__, static_folder='static', static_url_path='')

# Load config
with open('configuration.json') as json_file:
    configurationData = json.load(json_file)

mysql = connector.connect(
  host=configurationData['db_host'],
  user=configurationData['db_user'],
  passwd=configurationData['db_password'],
  database=configurationData['database']
)

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
