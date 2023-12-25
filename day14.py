from datetime import datetime


class Rock:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        # self.top = None
        # self.bottom = None
        # self.left = None
        # self.right = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.shape == other.shape

    def __str__(self):
        return f"Rock(x={self.x}, y={self.y} => {self.shape})"

    __repr__ = __str__


class Platform:
    def __init__(self):
        self.rocks = []
        self.width = 0
        self.height = 0

    def getRockAt(self, x, y):
        for r in self.rocks:
            if r.x == x and r.y == y:
                return r
        return None

    def getColAt(self, x):
        col = []
        for y in range(self.height + 1):
            if r := self.getRockAt(x, y):
                col.append(r)
        return col

    def getRowAt(self, y):
        row = []
        for x in range(self.width + 1):
            if r := self.getRockAt(x, y):
                row.append(r)
        return row

    def __eq__(self, other):
        # return self.rocks == other.rocks and self.width == other.width and self.height == other.height
        return self.__str__() == other.__str__()

    def __str__(self):
        table = [['.' for x in range(self.width)] for y in range(self.height)]
        for r in self.rocks:
            table[r.y - 1][r.x - 1] = r.shape

        s = ''
        for row in table:
            s += ('\n' + ''.join(row))

        return s

    __repr__ = __str__


def loadData(filename):
    platform = Platform()
    with open(filename, 'r') as f:
        for y, row in enumerate(f, start=1):
            for x, c in enumerate(row.strip(), start=1):
                if c != '.':
                    platform.rocks.append(Rock(x, y, c))
        else:
            platform.width = len(row)
            platform.height = y

    return platform


def countload(platform):
    sum = 0
    for r in platform.rocks:
        if r.shape == 'O':
            sum += (platform.height - (r.y - 1))
    return sum


def tilt(platform, direction):
    if direction in ('North', 'South'):
        for x in range(1, platform.width + 1):
            tilt_array(platform.getColAt(x), direction)
    else:
        pass
    return platform


def tilt_array(array, direction):
    if direction == 'North':
        array.sort(key=lambda r: r.y)

        if array[0].shape == 'O' and array[0].y > 1:
            array[0].y = 1

        for i in range(1, len(array)):
            if array[i].shape == '#':
                continue
            array[i].y = array[i - 1].y + 1

    elif direction == 'South':
        pass
    elif direction == 'East':
        pass
    elif direction == 'West':
        pass

    return array


if __name__ == "__main__":
    p = loadData('day14_input.txt')
    p = tilt(p, 'North')  # platform megdöntése északi irányba
    # with open('day14_output.txt', 'w') as f:
    #     print(p, file=f)

    print('Part1:', countload(p))  # 102620 is too low
