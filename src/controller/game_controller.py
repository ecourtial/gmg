from src.controller.abstract_controller import AbstractController
from src.repository.game_repository import GameRepository
from src.service.game_service import GameService

class GameController(AbstractController):
    repository = GameRepository
    service = GameService
