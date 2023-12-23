from datetime import datetime

cnt = 1


def is_reflect(array, position):
    max = len(array) - position
    if max > position:
        max = position
    for i in range(max):
        if array[position - 1 - i] != array[position + i]:
            return False
    return True


def reflectPositions(array):
    tmp = set()
    for i in range(1, len(array)):
        if is_reflect(array, i):
            tmp.add(i)
    return tmp


def visualizer(table, x, y):
    global cnt
    width = len(table[0])
    print(f"{cnt}.  x={x}, y={y}")
    cnt += 1
    for j in range(len(table)):

        if j == y and y != 0:
            print('-' * width)

        for i in range(width):
            c = table[j][i]
            if c == '.':
                c = '_'  # chr(0xFF3F)
            if i == x and x != 0:
                print('|' + c, end='')
            else:
                print(c, end='')

        print('')
    print('\n\n')


def process(table):
    mirrors_x = None
    mirrors_y = None
    for row in table:
        tmp = reflectPositions(row)
        if mirrors_x is None:
            mirrors_x = tmp
        else:
            mirrors_x = mirrors_x.intersection(tmp)

    for i in range(len(table[0])):
        col = ''.join(table[j][i] for j in range(len(table)))
        tmp = reflectPositions(col)
        if mirrors_y is None:
            mirrors_y = tmp
        else:
            mirrors_y = mirrors_y.intersection(tmp)

    x, y = 0, 0
    if mirrors_x:
        x = mirrors_x.pop()
    if mirrors_y:
        y = mirrors_y.pop()

    # visualizer(table, x, y)

    return x + 100 * y


def findMirrors(filename):
    table = []
    value = 0
    with open(filename, 'r') as f:
        for row in f:
            row = row.replace('\n', '')
            if not row:  # if the row is empty -> process the table and create a new
                value += process(table)
                table = []
            else:
                table.append(row)

        if table:  # process the last table (there is no empty line at the end of the file)
            value += process(table)
            table = []

    return value


if __name__ == "__main__":
    t0 = datetime.now()
    print('start:', t0)
    print('Part1:', findMirrors('day13_input.txt'))  # 21272 is too low
    t1 = datetime.now()
    print('end1:', t1, ' elapsed time:', t1 - t0)
    # print('Part2:', findMirrors('day13_input.txt'))
    # t2 = datetime.now()
    # print('end2:', t2, ' elapsed time:', t2 - t1)
