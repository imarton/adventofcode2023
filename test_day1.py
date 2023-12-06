from unittest import TestCase
import day1


class Test(TestCase):


    def test_phase2(self):
        list = [('two1nine', 29), ('eightwothree', 83), ('abcone2threexyz', 13), ('xtwone3four', 24),
                ('4nineeightseven2', 42), ('zoneight234', 14), ('7pqrstsixteen', 76)]

        for s, n in list:
            with self.subTest(s=s, n=n):
                print(day1.getCalibrationValue2(s)," -- ", n)
                self.assertEqual(day1.getCalibrationValue2(s), n)