import logging
import re
from unittest import TestCase

import day3


class Test(TestCase):
    def test_get_numbers(self):
        f = open("day3_sample.txt", "r")
        schematic = []

        while True:
            line = f.readline().replace('\n', '').replace('\r', '')
            if len(line) == 0:
                break
            schematic.append('.' + line + '.')

        f.close()

        self.assertEqual(day3.getPartNumberSum(schematic), 4361)

    def test_get_numbers2(self):
        f = open("day3_sample2.txt", "r")
        schematic = []

        while True:
            line = f.readline().replace('\n', '').replace('\r', '')
            if len(line) == 0:
                break
            schematic.append('.' + line + '.')

        f.close()

        self.assertEqual(day3.getPartNumberSum(schematic), 934)

    def test_part2(self):
        f = open("day3_sample_part2.txt", "r")
        schematic = []

        while True:
            line = f.readline().replace('\n', '').replace('\r', '')
            if len(line) == 0:
                break
            schematic.append('.' + line + '.')

        f.close()

        self.assertEqual(day3.getGearRationSum(schematic), 467835, 'Expected: 467835')
