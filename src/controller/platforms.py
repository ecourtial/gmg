""" Platforms controller for the GMG project """
from flask import jsonify
from src.repository.platform_repository import PlatformRepository

class PlatformController:
    """ Platforms controller for the GMG project """
    @classmethod
    def get_list(cls, mysql):
        """Return the platform list."""
        repo = PlatformRepository(mysql)
        platform_list = repo.get_list()
        return jsonify(platforms=[platform.serialize() for platform in platform_list])

    def __str__(self):
        """This method is here only to make Pylint stop complaining
        because I have only one method in my class"""
        return self.__class__.__name__
