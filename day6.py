
def loadData(filename):
    races = []
    with open(filename) as f:
        d = f.readlines()
        print(d)
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


if __name__ == '__main__':
    races = loadData("day6_input.txt")
    print('Part1:', getNumberOfBeating(races))
    # print('Part2:')
