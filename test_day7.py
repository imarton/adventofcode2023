from unittest import TestCase

import day7


class Test(TestCase):

    def test_get_total_price(self):
        day7.game = []
        day7.loadDatas('day7_sample.txt')
        self.assertEqual(6440, day7.getTotalPrice())

    def test_get_type(self):
        self.assertEqual('Five of a kind', day7.handtypes[day7.getType('AAAAA')])
        self.assertEqual('Four of a kind', day7.handtypes[day7.getType('AA8AA')])
        self.assertEqual('Full house', day7.handtypes[day7.getType('23332')])
        self.assertEqual('Three of a kind', day7.handtypes[day7.getType('TTT98')])
        self.assertEqual('Two pair', day7.handtypes[day7.getType('23432')])
        self.assertEqual('One pair', day7.handtypes[day7.getType('A23A4')])
        self.assertEqual('High card', day7.handtypes[day7.getType('23456')])

    def test_load_datas(self):
        day7.game = []
        day7.loadDatas('day7_sample.txt')
        h = day7.Hand('32T3K', 765)
        self.assertIn(h, day7.game)
        h = day7.Hand('T55J5', 684)
        self.assertIn(h, day7.game)
        h = day7.Hand('KK677', 28)
        self.assertIn(h, day7.game)
        h = day7.Hand('KTJJT', 220)
        self.assertIn(h, day7.game)
        h = day7.Hand('QQQJA', 483)
        self.assertIn(h, day7.game)

    def test_compare_to(self):
        h1 = day7.Hand('AAAAQ', 765, day7.getType('AAAAQ'))
        h2 = day7.Hand('AAAAK', 765, day7.getType('AAAAT'))
        self.assertLess(h1, h2)

    def test_get_type_joker(self):
        self.assertEqual('Five of a kind', day7.handtypes[day7.getTypeJoker('AAAAA')])
        self.assertEqual('Five of a kind', day7.handtypes[day7.getTypeJoker('AAJAA')])
        self.assertEqual('Five of a kind', day7.handtypes[day7.getTypeJoker('AJJAA')])

        self.assertEqual('Four of a kind', day7.handtypes[day7.getTypeJoker('AA8AA')])
        self.assertEqual('Four of a kind', day7.handtypes[day7.getTypeJoker('AJ8AA')])

        self.assertEqual('Full house', day7.handtypes[day7.getTypeJoker('23332')])
        self.assertEqual('Full house', day7.handtypes[day7.getTypeJoker('23J32')])

        self.assertEqual('Three of a kind', day7.handtypes[day7.getTypeJoker('TTT98')])
        self.assertEqual('Three of a kind', day7.handtypes[day7.getTypeJoker('TJT98')])

        self.assertEqual('Two pair', day7.handtypes[day7.getTypeJoker('23432')])

        self.assertEqual('One pair', day7.handtypes[day7.getTypeJoker('A23A4')])
        self.assertEqual('One pair', day7.handtypes[day7.getTypeJoker('A23J4')])

        self.assertEqual('High card', day7.handtypes[day7.getTypeJoker('23456')])

    def test_get_total_price2(self):
        day7.game = []
        day7.loadDatas2('day7_sample.txt')
        self.assertEqual(5905, day7.getTotalPrice())
