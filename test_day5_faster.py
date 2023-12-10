from unittest import TestCase

import day5_faster
import day5_faster as d5


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        d5.loadData("day5_sample.txt")

    def test_load_data(self):
        # első sor tesztje
        self.assertEqual([(79, 92), (55, 67)], d5.seeds)

    def test_load_data2(self):
        # levels feltöltődött-e megfelelően
        self.assertEqual(7, len(d5.levels))

        self.assertEqual(2, len(d5.levels['seed']))
        self.assertEqual(4, len(d5.levels['fertilizer']))

        mapping = d5.Mapping('water', 18, 24, 'light', 70)
        self.assertIn(mapping, d5.levels['water'])

    def test_minimum_loc(self):
        self.assertEqual(56, d5.minimumLoc((56, 59), 'location'))
        self.assertEqual(56, d5.minimumLoc((93, 96), 'humidity'))
        self.assertEqual(56, d5.minimumLoc((83, 96), 'humidity'))
        self.assertEqual(56, d5.minimumLoc((46, 62), 'light'))
        self.assertEqual(56, d5.minimumLoc((55, 67), 'seed'))

    def test_get_perfect_seed(self):
        self.assertEqual(46, d5.getPerfectSeed())
