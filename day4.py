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


def processline(line):
    name, values = line.replace('\n', '').split(': ')
    id = int(list(filter(None, name.split(' ')))[1])

    winner, yours = values.split(' | ')
    winner = list(filter(None, winner.split(' ')))
    yours = list(filter(None, yours.split(' ')))
    # print('w:', winner)
    # print('y:', yours)
    cnt = 0
    for y in yours:
        if y in winner:
            cnt += 1

    return id, cnt


def getDeckSize(fileName):
    cardTypes = {} # azonosító : nyertes számok mennyisége
    cardQueue = {} # feldolgozásra váró kártyák (id : darabszam)
    result = 0
    f = open(fileName, "r")

    # kezdőpakli felolvasása, queue-ba helyezése
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        cid, cnum = processline(line)

        if cid not in cardTypes:
            cardTypes[cid] = cnum

        if cid in cardQueue:
            cardQueue[cid] += 1
        else:
            cardQueue[cid] = 1

    f.close()
    # print('types:', cardTypes, ' queue:', cardQueue)

    # queue feldolgozása
    i = 1
    while i <= len(cardTypes):
        if cardQueue[i] <= 0:
            i +=1
        else:
            result += 1
            cardQueue[i] -= 1
            cnt = cardTypes[i]
            for j in range(cnt):
                cardQueue[i+j+1] +=1

    return result


if __name__ == '__main__':
    print('Part1:', getDeckScore("day4_input.txt"))
    print('Part2:', getDeckSize("day4_input.txt"))
