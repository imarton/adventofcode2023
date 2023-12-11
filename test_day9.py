from unittest import TestCase

import day9


class Test(TestCase):
    def test_prediction(self):
        self.assertEqual(114, day9.prediction("day9_sample.txt"))

    def test_interpolate(self):
        self.assertEqual(18, day9.nextElem([0, 3, 6, 9, 12, 15]))
        self.assertEqual(28, day9.nextElem([1, 3, 6, 10, 15, 21]))
        self.assertEqual(68, day9.nextElem([10, 13, 16, 21, 30, 45]))

