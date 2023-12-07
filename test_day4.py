from unittest import TestCase

import day4


class Test(TestCase):
    def test_get_card_score(self):
        sample = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        self.assertEqual(day4.getCardScore(sample), 8)

    def test_get_deck_score(self):
        self.assertEqual(day4.getDeckScore("day4_sample.txt"), 13)

    def test_get_deck_size(self):
        self.assertEqual(30, day4.getDeckSize("day4_sample.txt"))

    def test_processline(self):
        self.assertEqual((1, 4), day4.processline('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'))
        self.assertEqual((2, 2), day4.processline('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'))
        self.assertEqual((6, 0), day4.processline('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'))

