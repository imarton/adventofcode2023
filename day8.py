from datetime import datetime

direction = ''
map1 = {}


def steps():
    st = 0
    loc = 'AAA'
    i = 0
    while 'ZZZ' != loc:
        loc = map1[loc][direction[i]]
        st += 1
        i += 1
        if i == len(direction):
            i = 0

    return st


def stepsSimultan():
    st = 0
    i = 0
    locs = list(filter(lambda m: m.endswith('A'), map1.keys()))
    lastz = [0 for l in locs]
    print('start points:', len(locs), locs)
    while not isAllZ(locs):
        s = ''
        for j in range(len(locs)):
            locs[j] = map1[locs[j]][direction[i]]
            if locs[j][-1] == 'Z':
                s += str(st - lastz[j])
                lastz[j] = st
            else:
                s += '\t\t'
        if len(s.strip()) != 0:
            print(st, '.', s)

        st += 1
        i += 1
        if i == len(direction):
            i = 0
        if st > 100_000:
            break

    return st


def isAllZ(locs):
    for loc in locs:
        if not loc.endswith('Z'):
            return False
    return True


def loadData(filename):
    global direction
    global map1

    direction = None
    map1 = {}
    with open(filename, 'r') as f:
        firts = True
        for row in f:
            if firts:
                direction = row.replace('\n', '')
                firts = False
                continue

            if row.strip() == '':
                continue

            key, v = row.replace('\n', '').split(' = ')
            vl, vr = v[1:-1].split(', ')
            map1[key] = {'L': vl, 'R': vr}


if __name__ == "__main__":
    loadData('day8_input.txt')
    print('Part1:', steps())
    t0 = datetime.now()
    print('start:', t0)
    print('Part2:', stepsSimultan())
    t1 = datetime.now()
    print('end:', t1, ' elapsed time:', t1 - t0)