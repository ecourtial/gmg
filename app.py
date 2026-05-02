"""Main file of the app. Loaded once on server startup!"""
from functools import wraps
import json
from typing import Any, Callable
from flask import Flask, jsonify, request, Response
from src.controller.platform_controller import PlatformController
from src.controller.game_controller import GameController
from src.controller.user_controller import UserController
from src.controller.version_controller import VersionController
from src.controller.copy_controller import CopyController
from src.controller.story_controller import StoryController
from src.controller.transaction_controller import TransactionController
from src.controller.note_controller import NoteController
from src.controller.magazine_controller import MagazineController
from src.controller.magazine_issue_controller import MagazineIssueController
from src.controller.magazine_issue_copy_controller import MagazineIssueCopyController
from src.controller.game_version_magazine_mention_controller import GameVersionMagazineMentionController
from src.repository.user_repository import UserRepository
from src.connection.mysql_factory import MySQLFactory

app = Flask(__name__)
app.json.sort_keys = False

##############
# Load config
##############

with open('configuration.json', encoding='UTF-8') as json_file:
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

def token_required(decorated_function: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(decorated_function)
    def decorator(*args: Any, **kwargs: Any) -> tuple[Response, int] | Any:

        token = None

        if 'Authorization' in request.headers:
            header_value = request.headers['Authorization']
            if header_value.find(' ') != -1:
                array = header_value.split(' ')
                if array[0] == 'token':
                    token = array[1]

        if not token:
            return jsonify({'message': 'Missing token', 'code': 12}), 403

        user_repo = UserRepository(MySQLFactory.get())
        current_user = user_repo.get_active_by_token(token)
        if None is current_user:
            return jsonify({'message': 'Token is invalid', 'code': 13}), 403

        # This method is the only one to need the current_user
        if 'renew_token' == decorated_function.__name__:
            return decorated_function(current_user, *args, **kwargs)

        return decorated_function(*args, **kwargs)
    return decorator

########################################################################
# After request: cache management, close DB connection...
########################################################################

@app.after_request
def after_request(response: Response) -> Response:
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
def home() -> tuple[Response, int]:
    """Homepage with layout"""
    return jsonify({'message': 'Hello!'}), 200

# Users

@app.route('/api/v1/user/authenticate', methods=['POST'])
def authenticate_user() -> tuple[Response, int]:
    """Returns the token of the given user"""
    controller = UserController
    return controller.authenticate(MySQLFactory.get())

@app.route('/api/v1/user', methods=['GET'])
@token_required
def get_user() -> tuple[Response, int]:
    """Returns the user according to one filter"""
    controller = UserController
    return controller.get_by_filter(
        MySQLFactory.get(),
        request.args.get('filter', ''),
        request.args.get('value', '')
    )

@app.route('/api/v1/user', methods=['POST'])
@token_required
def create_user() -> tuple[Response, int]:
    """Creates a user"""
    controller = UserController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/user/<int:entity_id>', methods=['PATCH'])
@token_required
def update_user(entity_id: int) -> tuple[Response, int]:
    """Updates a user"""
    controller = UserController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/user/renew-token', methods=['POST'])
@token_required
def renew_token(current_user: Any) -> tuple[Response, int]:
    """Renew the API token of the current user"""
    controller = UserController
    return controller.renew_token(MySQLFactory.get(), current_user)

# Platforms

@app.route('/api/v1/platform/<int:entity_id>', methods=['GET'])
def get_platform_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the platform according to its id"""
    controller = PlatformController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platform', methods=['POST'])
@token_required
def create_platform() -> tuple[Response, int]:
    """Create a platform"""
    controller = PlatformController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/platform/<int:entity_id>', methods=['PATCH'])
@token_required
def update_platform(entity_id: int) -> tuple[Response, int]:
    """Update the platform according to its id"""
    controller = PlatformController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platform/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_platform(entity_id: int) -> tuple[Response, int]:
    """Delete the platform according to its id"""
    controller = PlatformController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/platforms', methods=['GET'])
def get_platforms() -> Response:
    """Get the platforms"""
    controller = PlatformController
    return controller.get_list(MySQLFactory.get())

# Games

@app.route('/api/v1/game/<int:entity_id>', methods=['GET'])
def get_game_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the game according to its id"""
    controller = GameController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game', methods=['POST'])
@token_required
def create_game() -> tuple[Response, int]:
    """Create a game"""
    controller = GameController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/game/<int:entity_id>', methods=['PATCH'])
@token_required
def update_game(entity_id: int) -> tuple[Response, int]:
    """Update the game according to its id"""
    controller = GameController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_game(entity_id: int) -> tuple[Response, int]:
    """Delete the game according to its id"""
    controller = GameController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/games', methods=['GET'])
def get_games() -> Response:
    """Get the games"""
    controller = GameController
    return controller.get_list(MySQLFactory.get())

# Versions

@app.route('/api/v1/version/<int:entity_id>', methods=['GET'])
def get_version_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the version according to its id"""
    controller = VersionController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/version', methods=['POST'])
@token_required
def create_version() -> tuple[Response, int]:
    """Create a version"""
    controller = VersionController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/version/<int:entity_id>', methods=['PATCH'])
@token_required
def update_version(entity_id: int) -> tuple[Response, int]:
    """Update the version according to its id"""
    controller = VersionController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/version/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_version(entity_id: int) -> tuple[Response, int]:
    """Delete the version according to its id"""
    controller = VersionController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/versions', methods=['GET'])
def get_versions() -> Response:
    """Get the versions"""
    controller = VersionController
    return controller.get_list(MySQLFactory.get())

# Copies

@app.route('/api/v1/copy/<int:entity_id>', methods=['GET'])
def get_copy_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the copy according to its id"""
    controller = CopyController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/copy', methods=['POST'])
@token_required
def create_copy() -> tuple[Response, int]:
    """Create a copy"""
    controller = CopyController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/copy/<int:entity_id>', methods=['PATCH'])
@token_required
def update_copy(entity_id: int) -> tuple[Response, int]:
    """Update the copy according to its id"""
    controller = CopyController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/copy/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_copy(entity_id: int) -> tuple[Response, int]:
    """Delete the copy according to its id"""
    controller = CopyController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/copies', methods=['GET'])
def get_copies() -> Response:
    """Get the copies"""
    controller = CopyController
    return controller.get_list(MySQLFactory.get())

# Stories

@app.route('/api/v1/story/<int:entity_id>', methods=['GET'])
def get_story_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the story according to its id"""
    controller = StoryController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/story', methods=['POST'])
@token_required
def create_story() -> tuple[Response, int]:
    """Create a story"""
    controller = StoryController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/story/<int:entity_id>', methods=['PATCH'])
@token_required
def update_story(entity_id: int) -> tuple[Response, int]:
    """Update the story according to its id"""
    controller = StoryController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/story/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_story(entity_id: int) -> tuple[Response, int]:
    """Delete the story according to its id"""
    controller = StoryController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/stories', methods=['GET'])
def get_stories() -> Response:
    """Get the stories"""
    controller = StoryController
    return controller.get_list(MySQLFactory.get())

# Transactions

@app.route('/api/v1/transaction/<int:entity_id>', methods=['GET'])
def get_transaction_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the transaction according to its id"""
    controller = TransactionController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/transaction', methods=['POST'])
@token_required
def create_transaction() -> tuple[Response, int]:
    """Create a transaction"""
    controller = TransactionController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/transaction/<int:entity_id>', methods=['PATCH'])
@token_required
def update_transaction(entity_id: int) -> tuple[Response, int]:
    """Update the transaction according to its id"""
    controller = TransactionController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/transaction/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_transaction(entity_id: int) -> tuple[Response, int]:
    """Delete the transaction according to its id"""
    controller = TransactionController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/transactions', methods=['GET'])
def get_transactions() -> Response:
    """Get the transactions"""
    controller = TransactionController
    return controller.get_list(MySQLFactory.get())

# Notes

@app.route('/api/v1/note/<int:entity_id>', methods=['GET'])
def get_note_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the note according to its id"""
    controller = NoteController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/note', methods=['POST'])
@token_required
def create_note() -> tuple[Response, int]:
    """Create a note"""
    controller = NoteController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/note/<int:entity_id>', methods=['PATCH'])
@token_required
def update_note(entity_id: int) -> tuple[Response, int]:
    """Update the note according to its id"""
    controller = NoteController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/note/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_note(entity_id: int) -> tuple[Response, int]:
    """Delete the note according to its id"""
    controller = NoteController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/notes', methods=['GET'])
def get_notes() -> Response:
    """Get the notes"""
    controller = NoteController
    return controller.get_list(MySQLFactory.get())

# Magazines

@app.route('/api/v1/magazine/<int:entity_id>', methods=['GET'])
def get_magazine_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the magazine according to its id"""
    controller = MagazineController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine', methods=['POST'])
@token_required
def create_magazine() -> tuple[Response, int]:
    """Create a magazine"""
    controller = MagazineController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/magazine/<int:entity_id>', methods=['PATCH'])
@token_required
def update_magazine(entity_id: int) -> tuple[Response, int]:
    """Update the magazine according to its id"""
    controller = MagazineController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_magazine(entity_id: int) -> tuple[Response, int]:
    """Delete the magazine according to its id"""
    controller = MagazineController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazines', methods=['GET'])
def get_magazines() -> Response:
    """Get the magazines"""
    controller = MagazineController
    return controller.get_list(MySQLFactory.get())

# Magazine Issues

@app.route('/api/v1/magazine-issue/<int:entity_id>', methods=['GET'])
def get_magazine_issue_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the magazine issue according to its id"""
    controller = MagazineIssueController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issue', methods=['POST'])
@token_required
def create_magazine_issue() -> tuple[Response, int]:
    """Create a magazine issue"""
    controller = MagazineIssueController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/magazine-issue/<int:entity_id>', methods=['PATCH'])
@token_required
def update_magazine_issue(entity_id: int) -> tuple[Response, int]:
    """Update the magazine issue according to its id"""
    controller = MagazineIssueController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issue/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_magazine_issue(entity_id: int) -> tuple[Response, int]:
    """Delete the magazine issue according to its id"""
    controller = MagazineIssueController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issues', methods=['GET'])
def get_magazine_issues() -> Response:
    """Get the magazine issues"""
    controller = MagazineIssueController
    return controller.get_list(MySQLFactory.get())

# Magazine Issue Copies

@app.route('/api/v1/magazine-issue-copy/<int:entity_id>', methods=['GET'])
def get_magazine_issue_copy_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the magazine issue copy according to its id"""
    controller = MagazineIssueCopyController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issue-copy', methods=['POST'])
@token_required
def create_magazine_issue_copy() -> tuple[Response, int]:
    """Create a magazine issue copy"""
    controller = MagazineIssueCopyController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/magazine-issue-copy/<int:entity_id>', methods=['PATCH'])
@token_required
def update_magazine_issue_copy(entity_id: int) -> tuple[Response, int]:
    """Update the magazine issue copy according to its id"""
    controller = MagazineIssueCopyController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issue-copy/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_magazine_issue_copy(entity_id: int) -> tuple[Response, int]:
    """Delete the magazine issue copy according to its id"""
    controller = MagazineIssueCopyController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/magazine-issue-copies', methods=['GET'])
def get_magazine_issue_copies() -> Response:
    """Get the magazine issue copies"""
    controller = MagazineIssueCopyController
    return controller.get_list(MySQLFactory.get())

# Game Version Magazine Mentions

@app.route('/api/v1/game-version-magazine-mention/<int:entity_id>', methods=['GET'])
def get_game_version_magazine_mention_by_id(entity_id: int) -> tuple[Response, int]:
    """Returns the game version magazine mention according to its id"""
    controller = GameVersionMagazineMentionController
    return controller.get_by_id(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game-version-magazine-mention', methods=['POST'])
@token_required
def create_game_version_magazine_mention() -> tuple[Response, int]:
    """Create a game version magazine mention"""
    controller = GameVersionMagazineMentionController
    return controller.create(MySQLFactory.get())

@app.route('/api/v1/game-version-magazine-mention/<int:entity_id>', methods=['PATCH'])
@token_required
def update_game_version_magazine_mention(entity_id: int) -> tuple[Response, int]:
    """Update the game version magazine mention according to its id"""
    controller = GameVersionMagazineMentionController
    return controller.update(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game-version-magazine-mention/<int:entity_id>', methods=['DELETE'])
@token_required
def delete_game_version_magazine_mention(entity_id: int) -> tuple[Response, int]:
    """Delete the game version magazine mention according to its id"""
    controller = GameVersionMagazineMentionController
    return controller.delete(MySQLFactory.get(), entity_id)

@app.route('/api/v1/game-version-magazine-mentions', methods=['GET'])
def get_game_version_magazine_mentions() -> Response:
    """Get the game version magazine mentions"""
    controller = GameVersionMagazineMentionController
    return controller.get_list(MySQLFactory.get())
