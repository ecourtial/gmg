""" Platform entity for the GMG project """

class Platform:
    """ This class represent a platform (support), for instance "Playstation" """

    expected_fields = {
        'name': {'field': 'name', 'method': '_name', 'required': True, 'type': 'text'},
    }

    authorized_extra_fields_for_filtering = {}

    table_name = 'platforms'
    primary_key = 'id'

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
