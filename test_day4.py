from unittest import TestCase

import day4


class Test(TestCase):
    def test_get_card_score(self):
        sample = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        self.assertEqual(day4.getCardScore(sample), 8)


    def test_get_deck_score(self):

        self.assertEqual(day4.getDeckScore("day4_sample.txt"), 13)
