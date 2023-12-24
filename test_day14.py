from unittest import TestCase

import day14


class Test(TestCase):
    def test_totalload(self):
        self.assertEqual(136, day14.totalload('day14_sample.txt'))
