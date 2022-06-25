""" Repository to handle the versions """
from src.repository.abstract_repository import AbstractRepository
from src.entity.version import Version
from src.entity.game import Game
from src.entity.platform import Platform
from src.entity.copy import Copy
from src.entity.story import Story

class VersionRepository(AbstractRepository):
    entity = Version

    def get_select_request_start(self):
        request = "SELECT versions.*, v.storyCount AS storyCount, c.copyCount AS copyCount, "
        request += f"{Game.table_name}.title AS gameTitle, {Platform.table_name}.name AS platformName "
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS storyCount, a.{Version.primary_key} "
        request += f"      FROM {Story.table_name}, {Version.table_name} a "
        request += f"      WHERE {Story.table_name}.version_id = a.{Version.primary_key} "
        request += f"      GROUP BY a.{Version.primary_key}) AS v "
        request += f"RIGHT JOIN {Version.table_name} v1 ON "
        request += f"v1.{Version.primary_key} = v.version_id, "
        request += f"     (SELECT COUNT(*) AS copyCount, b.{Version.primary_key} "
        request += f"      FROM {Copy.table_name}, {Version.table_name} b "
        request += f"      WHERE {Copy.table_name}.version_id = b.{Version.primary_key} "
        request += f"      GROUP BY b.{Version.primary_key}) AS c "
        request += f"RIGHT JOIN {Version.table_name} v2 ON "
        request += f"v2.{Version.primary_key} = c.version_id, "
        request += f"{Game.table_name}, {Platform.table_name}, {Version.table_name} "
        request += f"WHERE versions.game_id = {Game.table_name}.{Game.primary_key} "
        request += 'AND versions.version_id = v2.version_id '
        request += 'AND versions.version_id = v1.version_id '
        request += f"AND versions.platform_id = {Platform.table_name}.{Platform.primary_key} "

        return request

    def get_by_unique_index(self, platform_id, game_id):
        """Get one version by the unique combination of the platform and the game."""
        request = self.get_select_request_start()
        request += f"AND {Version.table_name}.platform_id = %s "
        request += f"AND {Version.table_name}.game_id = %s LIMIT 1;"

        return self.fetch_one(request, (platform_id, game_id,))

    def hydrate(self, row):
        """Hydrate an object from a row."""
        version = super().hydrate(row)
        version.set_platform_name(row['platformName'])
        version.set_game_title(row['gameTitle'])
        version.set_story_count(row['storyCount'])
        version.set_copy_count(row['copyCount'])

        return version
