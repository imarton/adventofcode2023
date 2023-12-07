from unittest import TestCase

import day5


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        day5.loadData("day5_sample.txt")

    def test_load_data(self):
        # day5.loadData("day5_sample.txt")
        self.assertEqual([79, 14, 55, 13], day5.seeds)

        self.assertIn((50, 52, 48), day5.seed_to_soil)
        self.assertIn((15, 0, 37), day5.soil_to_fertilizer)
        self.assertIn((11, 0, 42), day5.fertilizer_to_water)
        self.assertIn((18, 88, 7), day5.water_to_light)
        self.assertIn((45, 81, 19), day5.light_to_temperature)
        self.assertIn((69, 0, 1), day5.temperature_to_humidity)
        self.assertIn((56, 60, 37), day5.humidity_to_location)

    def test_get_lowest(self):
        # day5.loadData("day5_sample.txt")

        self.assertEqual(35, day5.getLowest())

    def test_get_mapped_value(self):
        # day5.loadData("day5_sample.txt")

        self.assertEqual(50, day5.getMappedValue(98, day5.seed_to_soil))
        self.assertEqual(51, day5.getMappedValue(99, day5.seed_to_soil))
        self.assertEqual(100, day5.getMappedValue(100, day5.seed_to_soil))
        self.assertEqual(53, day5.getMappedValue(51, day5.seed_to_soil))

    def test_get_location(self):
        # day5.loadData("day5_sample.txt")
        self.assertEqual(82, day5.getLocation(79))
        self.assertEqual(43, day5.getLocation(14))
        self.assertEqual(86, day5.getLocation(55))
        self.assertEqual(35, day5.getLocation(13))

    def test_get_lowest2(self):
        # day5.loadData("day5_sample.txt")
        self.assertEqual(46, day5.getLowest2())

