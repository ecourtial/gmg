""" Platform entity for the GMG project """
import json

class Platform:
    """ This class represent a platform (support), for instance "Playstation" """

    def __init__(self, platform_id, platform_name):
        self.platform_id = platform_id
        self.platform_name = platform_name

    def get_id(self):
        """Return the id of the platform, for instance "3"."""
        return self.platform_id

    def get_name(self):
        """Return the name of the platform, for instance "Playstation 2"."""
        return self.platform_name

    def set_name(self, name):
        self.platform_name = name

    def serialize(self):
        return {
            'id': self.platform_id,
            'name': self.platform_name
        }
