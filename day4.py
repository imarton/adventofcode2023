def getCardScore(line):
    result = 0
    tmp = line.replace('\n', '').split(': ')[1]
    winner, yours = tmp.split(' | ')
    winner = list(filter(None, winner.split(' ')))
    yours = list(filter(None, yours.split(' ')))
    # print('w:', winner)
    # print('y:', yours)
    for y in yours:
        if y in winner:
            if result == 0:
                result = 1
            else:
                result *= 2
    return result


def getDeckScore(fileName):
    result = 0
    f = open(fileName, "r")

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        c = getCardScore(line)
        # print(line, ' -->', c)
        result += c
    f.close()

    return result


if __name__ == '__main__':
    print('Part1:', getDeckScore("day4_input.txt"))
