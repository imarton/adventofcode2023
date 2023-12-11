from unittest import TestCase

import day8


class Test(TestCase):
    def test_steps(self):
        day8.loadData('day8_sample.txt')
        self.assertEqual(2, day8.steps())
        day8.loadData('day8_sample2.txt')
        self.assertEqual(6, day8.steps())

    def test_load_data(self):
        day8.loadData('day8_sample.txt')
        self.assertEqual('RL', day8.direction)

        self.assertEqual({'L': 'ZZZ', 'R': 'GGG'}, day8.map1['CCC'])
