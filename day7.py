# Camel Cards

# Hand list
game = []
handtypes = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']
cardvalues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cardvalues2 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}


class Hand:
    def __init__(self, cards, bid, type=-1):
        self.card = cards
        self.bid = bid
        self.type = type

    def __str__(self):
        return f"Hand(card={self.card}, bid={self.bid})"

    __repr__ = __str__

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        return self.card, self.bid

    def __lt__(self, other):
        if self.type < other.type or self.__str__() == other.__str__():
            return False

        if self.type > other.type:
            return True

        # self.type == other.type
        for i in range(len(self.card)):
            if self.card[i] == other.card[i]:
                continue
            if cardvalues[self.card[i]] < cardvalues[other.card[i]]:
                return True
            else:
                return False


def getType(cards):
    charCount = [cards.count(c) for c in set(cards)]

    if len(charCount) == 1:
        return 0
    elif len(charCount) == 2:

        if charCount[0] == 4 or charCount[0] == 1:
            return 1
        else:
            return 2

    elif len(charCount) == 3:
        if charCount[0] == 3 or charCount[1] == 3 or charCount[2] == 3:
            return 3
        else:
            return 4

    elif len(charCount) == 4:
        return 5
    elif len(charCount) == 5:
        return 6


def getTypeJoker(cards):
    """
    Típus meghatározása az új Joker szabály figyelembe vétele mellett
    :param cards:
    :return:
    """
    if 'J' not in cards or 'JJJJJ' == cards:
        return getType(cards)

    charCount = {c: cards.count(c) for c in set(cards)}
    max = None
    for c in charCount:
        if 'J' == c:
            continue

        if max is None or charCount[c] > charCount[max]:
            max = c

    tmp = cards.replace('J', max)

    return getType(tmp)


def getTotalPrice():
    tmp = []
    for h in game:
        if len(tmp) == 0:
            tmp.append(h)
            continue

        inserted = False
        for i in range(len(tmp)):
            if h < tmp[i]:
                tmp.insert(i, h)
                inserted = True
                break

        if not inserted:
            tmp.append(h)

    sum = 0
    for i, h in enumerate(tmp):
        sum += (i + 1) * h.bid

    return sum


def loadDatas(filename):
    with open(filename, 'r') as f:
        for row in f:
            cards, bid = row.split(' ')
            game.append(Hand(cards, int(bid), getType(cards)))


def loadDatas2(filename):
    with open(filename, 'r') as f:
        for row in f:
            cards, bid = row.split(' ')
            game.append(Hand(cards, int(bid), getTypeJoker(cards)))


if __name__ == '__main__':
    loadDatas('day7_input.txt')
    print('part1: ', getTotalPrice())

    game = []
    loadDatas2('day7_input.txt')
    print('part2: ', getTotalPrice())
