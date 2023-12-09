from datetime import datetime
import math


def loadData(filename):
    races = []
    with open(filename) as f:
        d = f.readlines()
        row1 = list(filter(None, d[0].split(' ')))
        row2 = list(filter(None, d[1].split(' ')))
        for i in range(len(row1)):
            if i == 0:
                continue
            races.append((int(row1[i]), int(row2[i])))

    return races


def numOfWin(race):
    res = 0
    time = race[0]
    lastRecord = race[1]
    for t in range(time+1):
        d = (time - t) * t
        if lastRecord < d:
            res += 1

    return res


def getNumberOfBeating(races):
    result = 1
    for r in races:
        result *= numOfWin(r)

    return result


def numOfWin2(race):
    b = race[0]
    c = race[1]
    # print(f'axˇ2 - bx + c = 0 --> xˇ2 - {b}x + {c} = 0')
    d = b * b - 4 * 1 * c
    x1 = (b - math.sqrt(d)) / (2 * 1)
    x2 = (b + math.sqrt(d)) / (2 * 1)

    return int(x2) - int(x1)

def loadData2(filename):
    with open(filename) as f:
        text = f.readlines()

        row1 = text[0].replace(' ', '').split(':')[1]
        row2 = text[1].replace(' ', '').split(':')[1]

    return int(row1), int(row2)


if __name__ == '__main__':
    races = loadData("day6_input.txt")
    print('   Part1:', getNumberOfBeating(races))
    t0 = datetime.now()

    print('start:', t0)
    race = loadData2("day6_input.txt")
    print('   Part2:', numOfWin(race))
    t1 = datetime.now()
    print('mid:', t1-t0, '(elapsed time)')
    print('   Part2 alternativ:', numOfWin2(race))
    print('end:', datetime.now() - t1, '(elapsed time)')