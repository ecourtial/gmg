from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.service.abstract_service import AbstractService
from src.repository.story_repository import StoryRepository
from src.repository.version_repository import VersionRepository
from src.entity.story import Story
from src.exception.unknown_resource_exception import ResourceNotFoundException

class StoryService(AbstractService):
    resource_type = 'story'
    
    def __init__(self, mysql):
        self.repository = StoryRepository(mysql)
        self.version_repository = VersionRepository(mysql)
    
    def validate_payload_for_creation_and_hydrate(self):
        
        story = super().validate_payload_for_creation_and_hydrate(Story)
        version = self.version_repository.get_by_id(story.get_version_id())

        if version is None:
            raise ResourceNotFoundException('version', story.get_version_id())

        return story

    def validate_payload_for_update_and_hydrate(self, story_id):
        story = self.repository.get_by_id(story_id)

        if story is None:
            raise ResourceNotFoundException('story', story_id)

        super().hydrate_for_update(story)

        version = self.version_repository.get_by_id(story.get_version_id())

        if version is None:
            raise ResourceNotFoundException('version', story.get_version_id())

        return story

    def delete(self, story_id):
        story = self.repository.get_by_id(story_id)

        if story is None:
            raise ResourceNotFoundException('story', story_id)

        self.repository.delete(story_id)

        return True
