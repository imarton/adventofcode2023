from unittest import TestCase

import day10


class Test(TestCase):
    def test_farthest(self):
        start = day10.loaddata("day10_sample.txt")
        self.assertEqual(8, day10.farthest(start))

    def test_loaddata(self):
        start = day10.loaddata("day10_sample.txt")
        # print('Start at:', s)
        # for row in day10.pipemap:
        #     print(row)
        self.assertEqual((1, 3), start)

    def test_step(self):
        start = day10.loaddata("day10_sample.txt")
        node = day10.step(day10.Node((1, 4), '|', fromn=day10.Node(start, 'S')))
        self.assertEqual('L', node.type)

    def test_first_step(self):
        start = day10.loaddata("day10_sample.txt")
        node = day10.firstStep(day10.Node(start, 'S'))
        self.assertIn(node.type, '|J')
