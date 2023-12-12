def interpolate(seq):
    tmp = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if not any(tmp):
        return 0
    x = interpolate(tmp)
    ret = x + tmp[-1]
    return ret


def nextElem(seq):
    x = interpolate(seq)
    return x + seq[-1]


def prediction(filename):
    with open(filename, 'r') as f:
        x = 0
        for row in f:
            seq = [int(n) for n in row.split(' ')]
            x += nextElem(seq)
    return x


def interpolatePrev(seq):
    tmp = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if not any(tmp):
        return 0
    x = interpolatePrev(tmp)
    ret = tmp[0] - x
    return ret


def prevElem(seq):
    x = interpolatePrev(seq)
    return seq[0] - x


def prediction2(filename):
    with open(filename, 'r') as f:
        x = 0
        for row in f:
            seq = [int(n) for n in row.split(' ')]
            x += prevElem(seq)
    return x


if __name__ == "__main__":
    print('Part1:', prediction('day9_input.txt'))
    print('Part2:', prediction2('day9_input.txt'))
