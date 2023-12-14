from unittest import TestCase

import day12


class Test(TestCase):
    def test_loaddata(self):
        self.fail()

    def test_arrangements(self):
        rec = []
        self.assertEqual(21, day12.arrangements(rec))
