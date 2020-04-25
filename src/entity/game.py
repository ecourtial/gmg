class Game:
    """This class represents a game entity"""
    
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def _get_id(self):
        return self.id

    def _get_title(self):
        return self.title    

    def _set_id(self, id):
        self.id = id

    def _set_title(self, title):
        self.title = title    


# id
# title
# platform
# to_buy
# to_do
# to_watch
# singleplayer_recurring
# multiplayer_recurring
# copy
# many
# top_game
# comments
# all_of_fame
# all_of_fame_year
# all_of_fame_position