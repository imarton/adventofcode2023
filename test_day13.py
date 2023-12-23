from unittest import TestCase

import day13


class Test(TestCase):
    def test_find_mirrors(self):
        self.assertEqual(405, day13.findMirrors('day13_sample.txt'))
        self.assertEqual(0, day13.findMirrors('day13_sample2.txt'))

    def test_is_reflect(self):
        self.assertTrue(day13.is_reflect('#.##..##.', 5))
        self.assertFalse(day13.is_reflect('#.##..##.', 1))
        self.assertTrue(day13.is_reflect('#.##..##.', 7))

    def test_reflect_positions(self):
        self.assertEqual({5, 7}, day13.reflectPositions('#.##..##.'))

    def test_process(self):
        t = ['#.##..##.'
            , '..#.##.#.'
            , '##......#'
            , '##......#'
            , '..#.##.#.'
            , '..##..##.'
            , '#.#.##.#.']
        self.assertEqual(5, day13.process(t))

        t = ['#...##..#'
            , '#....#..#'
            , '..##..###'
            , '#####.##.'
            , '#####.##.'
            , '..##..###'
            , '#....#..#']
        self.assertEqual(400, day13.process(t))
