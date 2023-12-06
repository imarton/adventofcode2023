from unittest import TestCase
import day2

class Test(TestCase):
    def test_get_game_number_if_possible(self):
        res = day2.getGameNumberIfPossible("Game 1: 1 blue, 2 green, 3 red; 7 red, 8 green; 1 green, 2 red, 1 blue; 2 "
                                     "green, 3 red, 1 blue; 8 green, 1 blue")
        self.assertEqual(res, 56)
