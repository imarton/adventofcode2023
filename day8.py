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
