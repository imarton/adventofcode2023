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

        pattern, groups = day12.unfold('???????##?????#?#?', '9, 6', 5)
        groups = [int(i) for i in groups.split(',')]
        self.assertEqual(35982, day12.process(pattern, groups))

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

    def test_unfold(self):
        self.assertEqual(('.#?.#?.#?.#?.#', '1,1,1,1,1'), day12.unfold('.#', '1', 5))
        self.assertEqual(('???.###????.###????.###????.###????.###', '1,1,3,1,1,3,1,1,3,1,1,3,1,1,3'),
                         day12.unfold('???.###', '1,1,3', 5))

    def test_arrangements2(self):
        self.assertEqual(525152, day12.arrangements2('day12_sample.txt'))

    def test_arrangements3(self):
        self.assertEqual(525152, day12.arrangements3('day12_sample.txt'))
