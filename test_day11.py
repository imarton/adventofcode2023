from unittest import TestCase

import day11


class Test(TestCase):

    def test_loaddata(self):
        day11.loaddata("day11_sample.txt")
        expect = [[4, 1], [8, 2], [1, 3], [7, 5], [2, 6], [10, 7], [8, 9], [1, 10], [5, 10]]
        self.assertEqual(expect, day11.galaxies)
        self.assertEqual([3, 6, 9], day11.spacex)
        self.assertEqual([4, 8], day11.spacey)

    def test_expand(self):
        gl = [[4, 1], [8, 2], [1, 3], [7, 5], [2, 6], [10, 7], [8, 9], [1, 10], [5, 10]]
        spacex = [3, 6, 9]
        spacey = [4, 8]
        expect = [[5, 1], [10, 2], [1, 3], [9, 6], [2, 7], [13, 8], [10, 11], [1, 12], [6, 12]]
        self.assertEqual(expect, day11.expand(gl, spacex, spacey))

    def test_distance(self):
        self.assertEqual(9, day11.distance([2, 7], [6, 12]))

    def test_sum_distance(self):
        day11.loaddata("day11_sample.txt")
        galList = day11.expand(day11.galaxies, day11.spacex, day11.spacey)
        self.assertEqual(374, day11.sumDistance(galList))

    def test_sum_distance2(self):
        day11.loaddata("day11_sample.txt")
        # galList = day11.expand(day11.galaxies, day11.spacex, day11.spacey, 10)
        # self.assertEqual(1030, day11.sumDistance(galList))
        galList = day11.expand(day11.galaxies, day11.spacex, day11.spacey, 100)
        self.assertEqual(8410, day11.sumDistance(galList))
