"""Main file of the app. Loaded once on server startup!"""
from functools import wraps
import json
from flask import Flask, jsonify, request
from src.controller.platform_controller import PlatformController
from src.controller.game_controller import GameController
from src.controller.user_controller import UserController
from src.controller.version_controller import VersionController
from src.repository.user_repository import UserRepository
from src.connection.mysql_factory import MySQLFactory

app = Flask(__name__)

##############
# Load config
##############

with open('configuration.json') as json_file:
    configurationData = json.load(json_file)

################
# DB connection
################

MySQLFactory.init(
    configurationData['db_host'],
    configurationData['db_user'],
    configurationData['db_password'],
    configurationData['database']
)

##################
# User management
##################

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

      token = None

      if 'x-access-tokens' in request.headers:
         token = request.headers['x-access-tokens']

      if not token:
         return jsonify({'message': 'Missing token'}), 403

      user_repo = UserRepository(MySQLFactory.get())
      current_user = user_repo.get_active_by_token(token)
      if None == current_user:
         return jsonify({'message': 'Token is invalid'}), 403

      return f(current_user, *args, **kwargs)
   return decorator

########################################################################
# After request: cache management, close DB connection...
########################################################################

@app.after_request
def after_request(response):
    """Handle logic after each request"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"

    MySQLFactory.close()

    return response

##########
# Routes
##########

# Home

@app.route('/')
def home():
    """Homepage with layout"""
    return jsonify({'message': 'Hello!'}), 200

# Users

@app.route('/api/v1/user/authenticate', methods=['POST'])
def authenticate_user():
    """Returns the token of the given user"""
    controller = UserController
    return controller.authenticate(MySQLFactory.get())

@app.route('/api/v1/user', methods=['GET'])
@token_required
def get_user(current_user):
    """Returns the user according to one filter"""
    controller = UserController
    return controller.get_by_filter(MySQLFactory.get(), request.args.get('filter', ''), request.args.get('value', ''))

@app.route('/api/v1/user', methods=['POST'])
@token_required
def create_user(current_user):
    """Creates a user"""
    controller = UserController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/user/<int:entity_id>', methods=['PATCH'])
@token_required
def update_user(current_user, entity_id):
    """Updates a user"""
    controller = UserController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/user/renew-token', methods=['POST'])
@token_required
def renew_token(current_user):
    """Renew the API token of the current user"""
    controller = UserController
    return controller.renew_token(MySQLFactory.get(), current_user)

# Platforms

@app.route('/api/v1/platform/<int:entity_id>', methods=['GET'])
@token_required
def get_platform_by_id(current_user, entity_id):
    """Returns the platform according to its id"""
    controller = PlatformController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platform', methods=['POST'])
@token_required
def create_platform(current_user):
    """Create a platform"""
    controller = PlatformController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/platform/<int:entity_id>', methods=['PATCH'])
@token_required
def update_platform(current_user, entity_id):
    """Update the platform according to its id"""
    controller = PlatformController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platform/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_platform(current_user, entity_id):
    """Delete the platform according to its id"""
    controller = PlatformController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platforms', methods=['GET'])
@token_required
def get_platforms(current_user):
    """Get the platforms"""
    controller = PlatformController
    return controller.get_list(MySQLFactory.get())

# Games

@app.route('/api/v1/game/<int:entity_id>', methods=['GET'])
@token_required
def get_game_by_id(current_user, entity_id):
    """Returns the game according to its id"""
    controller = GameController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game', methods=['POST'])
@token_required
def create_game(current_user):
    """Create a game"""
    controller = GameController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/game/<int:entity_id>', methods=['PATCH'])
@token_required
def update_game(current_user, entity_id):
    """Update the game according to its id"""
    controller = GameController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_game(current_user, entity_id):
    """Delete the game according to its id"""
    controller = GameController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/games', methods=['GET'])
@token_required
def get_games(current_user):
    """Get the games"""
    controller = GameController
    return controller.get_list(MySQLFactory.get())

# Versions

@app.route('/api/v1/version/<int:entity_id>', methods=['GET'])
@token_required
def get_version_by_id(current_user, entity_id):
    """Returns the version according to its id"""
    controller = VersionController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/version', methods=['POST'])
@token_required
def create_version(current_user):
    """Create a version"""
    controller = VersionController
    return controller.create(MySQLFactory.get())
