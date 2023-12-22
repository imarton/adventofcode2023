from unittest import TestCase

import day12


class Test(TestCase):

    def test_arrangements(self):
        self.assertEqual(21, day12.arrangements('day12_sample.txt'))

    def test_process(self):
        self.assertEqual(1, day12.process('###', [3]))
        self.assertEqual(1, day12.process('?###', [3]))
        self.assertEqual(1, day12.process('??###', [3]))
        self.assertEqual(1, day12.process('???###', [3]))
        self.assertEqual(1, day12.process('###?', [3]))
        self.assertEqual(1, day12.process('###???', [3]))
        self.assertEqual(1, day12.process('###?????????', [3]))

        self.assertEqual(2, day12.process('?#?', [2]))
        self.assertEqual(2, day12.process('.?#?.', [2]))
        self.assertEqual(2, day12.process('.?#?.??', [2]))

        self.assertEqual(1, day12.process('???.###', [1, 1, 3]))
        self.assertEqual(4, day12.process('.??..??...?##.', [1, 1, 3]))
        self.assertEqual(1, day12.process('?#?#?#?#?#?#?#?', [1, 3, 1, 6]))
        self.assertEqual(1, day12.process('????.#...#...', [4, 1, 1]))
        self.assertEqual(4, day12.process('????.######..#####.', [1, 6, 5]))
        self.assertEqual(10, day12.process('?###????????', [3, 2, 1]))
        self.assertEqual(1, day12.process('???#??#?#?#?..', [1, 7]))

    def test_check(self):
        self.assertEqual(2, day12.check('###', [3], True))
        self.assertEqual(2, day12.check('###.', [3], True))
        self.assertEqual(3, day12.check('.###', [3]))
        self.assertEqual(-1, day12.check('.###', [1]))
        self.assertEqual(3, day12.check('.###.', [3]))
        self.assertEqual(-1, day12.check('.##..', [3]))
        self.assertEqual(-1, day12.check('..#..##', [2]))

        self.assertEqual(-1, day12.check('.##..##', [2], False, 4))

        self.assertEqual(-1, day12.check('.#######?#?..', [7]))

    def test_merge(self):
        self.assertEqual('Error', day12.merge('?', 3, 0))
        self.assertEqual('Error', day12.merge('?', 1, 2))

        self.assertEqual('.###.??', day12.merge('.?#?.??', 3, 1))

        self.assertEqual('###', day12.merge('###', 3, 0))
        self.assertEqual('###', day12.merge('?#?', 3, 0))
        self.assertEqual('Error', day12.merge('.?#?.', 3, 0))
        self.assertEqual('.###.', day12.merge('.?#?.', 3, 1))
        self.assertEqual('Error', day12.merge('.?#?.', 3, 2))
