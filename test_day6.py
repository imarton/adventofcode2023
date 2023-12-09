from unittest import TestCase

import day6


class Test(TestCase):
    def test_load_data(self):
        self.assertEqual([(7, 9), (15, 40), (30, 200)], day6.loadData("day6_sample.txt"))

    def test_get_number_of_beating(self):
        r = day6.loadData("day6_sample.txt")
        self.assertEqual(288, day6.getNumberOfBeating(r))

    def test_num_of_win(self):
        inp = (7, 9)
        self.assertEqual(4, day6.numOfWin(inp))
