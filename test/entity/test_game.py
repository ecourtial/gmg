import unittest
from entity.game import Game

class GameTest(unittest.TestCase):
    def test_creation(self):
        myGame = Game(
            12,
            'The Secret of Monkey Island',
            1,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            0,
            1,
            0,
            1,
            1,
            2002,
            5,
            1,
            'Mon nom est Guybursh Threepwood et je veux devenir pirate!'
        )
        self.assertEqual('The Secret of Monkey Island', myGame.title)

if __name__ == '__main__':
    unittest.main()