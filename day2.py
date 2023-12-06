maxValues = {'red': 12, 'green': 13, 'blue': 14}

result = 0
f = open("day2_input.txt", 'r')


def getGameNumberIfPossible(line):
    minValues = {'red': 1, 'green': 1, 'blue': 1}
    try:
        gameNum, tmp = line.replace('\n','').split(': ')
        gameNum = int(gameNum.split(' ')[1])
        # result = True
        for st in tmp.split('; '):
            # print(st)
            for cube in st.split(', '):
                # print(cube)
                n, color = cube.split(' ')
                if minValues[color] < int(n):
                    minValues[color] = int(n)
    except Exception as ex:
        print("Hiba a sorban!", line, ex)
        raise ex

    # if result:
    #     return gameNum
    # else:
    #     return -1

    for key in minValues.keys():
        if minValues[key] == 1000:
            minValues[key] = 1
    # print('minValues:', minValues)
    return minValues['red'] * minValues['blue'] * minValues['green']

while True:
    line = f.readline()
    if len(line) == 0:
        break
    # print(line)
    x = getGameNumberIfPossible(line)
    result += x

f.close()

print(result)
