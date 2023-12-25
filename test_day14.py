from unittest import TestCase

import day14
from day14 import Rock


class Test(TestCase):
    def test_countload(self):
        p = day14.loadData('day14_sample.txt')
        self.assertEqual(104, day14.countload(p))
        p = day14.tilt(p, 'North')
        self.assertEqual(136, day14.countload(p))

    def test_tilt(self):
        p = day14.loadData('day14_sample.txt')
        pt = day14.loadData('day14_sample_tilted.txt')
        result = day14.tilt(p, 'North')
        self.assertEqual(pt, result)

    def test_tilt_array(self):
        t = [ Rock(1, 1, 'O')
            , Rock(1, 2, 'O')
            , Rock(1, 4, 'O')
            , Rock(1, 6, 'O')
            , Rock(1, 9, '#')
            , Rock(1, 10, '#')]

        expected = [ Rock(1, 1, 'O')
            , Rock(1, 2, 'O')
            , Rock(1, 3, 'O')
            , Rock(1, 4, 'O')
            , Rock(1, 9, '#')
            , Rock(1, 10, '#')]

        self.assertEqual(expected, day14.tilt_array(t, 'North'))
