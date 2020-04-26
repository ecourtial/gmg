""" Platform entity for the GMG project """
class Platform:
    """ This class represent a platform (support), for instance "Playstation" """

    def __init__(self):
        self.support_id = 1
        self.name = 'Playstation'

    def get_support_id(self):
        """Return the id of the support, for instance "4"."""
        return self.support_id

    def get_name(self):
        """Return the name of the support, for instance "Playstation 2"."""
        return self.name
