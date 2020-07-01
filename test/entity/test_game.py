import unittest
from entity.game import Game
from entity.platform import Platform

class GameTest(unittest.TestCase):
    def test_creation(self):
        my_game = Game(
            12,
            'The Secret of Monkey Island',
            1
        )
        self.assertEqual(12, my_game.get_game_id())
        self.assertEqual('The Secret of Monkey Island', my_game.get_title())
        self.assertEqual(1, my_game.get_platform())


        meta = {'a': 1}
        my_game.set_meta(meta)
        self.assertEqual({'a': 1}, my_game.get_meta())

        to_json = '{"game_id": 12, "title": "The Secret of Monkey Island", "platform": 1, "meta": {"a": 1}}'
        self.assertEqual(to_json, my_game.to_json())

        my_platform = Platform(2, 'PSX', 4)
        my_game = Game(
            5,
            'The Secret of Monkey Island',
            my_platform
        )

        to_json = '{"game_id": 5, "title": "The Secret of Monkey Island", "platform": {"platform_id": 2, "platform_name": "PSX", "game_count": 4}, "meta": []}'
        self.assertEqual(to_json, my_game.to_json())

if __name__ == '__main__':
    unittest.main()