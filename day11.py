# coords of galaxies [(4, 1), (8, 2), ... (x, y)]   1 <= x,y <= len
galaxies = []

spacex = []
spacey = []

def loaddata(filename):
    with open(filename, 'r') as f:
        tmp = set()
        max = 0
        y = 1
        for row in f:
            row = row.replace('\n', '')
            if max == 0:
                max = len(row)

            if '#' not in row:
                spacey.append(y)
            else:
                for x in range(len(row)):
                    if row[x] == '#':
                        galaxies.append([x + 1, y])
                        tmp.add(x + 1)

            y += 1
        for x in range(1, max + 1):
            if x not in tmp:
                spacex.append(x)


def expand(galist, spacex, spacey, value=1):
    if value > 1:
        value -=1
    for x in reversed(spacex):
        for g in galist:
            if g[0] > x:
                g[0] += value

    for y in reversed(spacey):
        for g in galist:
            if g[1] > y:
                g[1] += value

    return galist


def distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def sumDistance(gallist):
    sum = 0
    for g1 in gallist:
        for g2 in gallist:
            sum += distance(g1, g2)
    return sum // 2


if __name__ == "__main__":
    loaddata("day11_input.txt")
    galaxies = expand(galaxies, spacex, spacey, 1_000_000)
    print("part1: ", sumDistance(galaxies))
