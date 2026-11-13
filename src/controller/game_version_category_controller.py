from src.controller.abstract_controller import AbstractController
from src.repository.game_version_category_repository import GameVersionCategoryRepository
from src.service.game_version_category_service import GameVersionCategoryService

class GameVersionCategoryController(AbstractController):
    repository = GameVersionCategoryRepository
    service = GameVersionCategoryService
