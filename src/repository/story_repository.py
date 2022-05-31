from src.repository.abstract_repository import AbstractRepository
from src.entity.story import Story
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform

class StoryRepository(AbstractRepository):
    entity = Story

    def get_select_request_start(self):
        request = f"SELECT {Story.table_name}.*, "
        request += f"{Game.table_name}.title AS gameTitle, "
        request += f"{Platform.table_name}.name AS platformName "
        request += f"FROM {Story.table_name}, {Version.table_name}, {Game.table_name}, {Platform.table_name} "
        request += f"WHERE {Story.table_name}.version_id = {Version.table_name}.{Version.primary_key} "
        request += f"AND {Version.table_name}.game_id = {Game.table_name}.{Game.primary_key} "
        request += f"AND {Version.table_name}.platform_id = {Platform.table_name}.{Platform.primary_key} "

        return request

    @classmethod
    def hydrate(cls, row):
        """Hydrate an object from a row."""
        story = super().hydrate(row)
        story.set_platform_name(row['platformName'])
        story.set_game_title(row['gameTitle'])

        return story
    