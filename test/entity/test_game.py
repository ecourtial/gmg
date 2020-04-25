import unittest
from entity.game import Game

class GameTest(unittest.TestCase):
    def test_creation(self):
        myGame = Game(12, 'The Secret of Monkey Island')
        self.assertEqual('The Secret of Monkey Island', myGame.title)

if __name__ == '__main__':
    unittest.main()