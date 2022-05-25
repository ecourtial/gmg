from src.repository.platform_repository import PlatformRepository

class PlatformService:
    def __init__(self, mysql):
        self.platform_repository = PlatformRepository(mysql)

    def create(self, name):
        """Create a platform"""
        checkPlatform = self.platform_repository.get_by_name(name)
        if checkPlatform is not None:
            return 'name'

        return self.platform_repository.insert(name)

    def update(self, platform):
        """Update a platform"""
        checkPlatform = self.platform_repository.get_by_name(platform.get_name())
        if checkPlatform is not None:
            return 'name'

        return self.platform_repository.update(platform)

    def delete(self, platform):
        """Delete a platform"""
        count = self.platform_repository.get_versions_count_for_platform(platform.get_id())['count']

        if count > 0:
            return False

        self.platform_repository.delete(platform.get_id())

        return True
    