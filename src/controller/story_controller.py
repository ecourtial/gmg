from src.controller.abstract_controller import AbstractController
from src.repository.story_repository import StoryRepository
from src.service.story_service import StoryService

class StoryController(AbstractController):
    repository = StoryRepository
    service = StoryService
