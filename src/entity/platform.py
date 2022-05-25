""" Platform entity for the GMG project """
import json

class Platform:
    """ This class represent a platform (support), for instance "Playstation" """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        """Return the id of the platform, for instance "3"."""
        return self.id

    def get_name(self):
        """Return the name of the platform, for instance "Playstation 2"."""
        return self.name

    def set_name(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
