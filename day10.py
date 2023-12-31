import math

pipemap = []
startPoint = None
# Remark: Coordinate system starts at the top-left corner (0,0)
# first elem postition: (1,1)

# pipe type + shifting koords
pipes = {'|': [(0, 1), (0, -1)],
         'L': [(0, -1), (1, 0)],
         '-': [(1, 0), (-1, 0)],
         'J': [(-1, 0), (0, -1)],
         'F': [(1, 0), (0, 1)],
         '7': [(-1, 0), (0, 1)]}

nicepipes = {'|': chr(0x2503),
             'L': chr(0x2517),
             '-': chr(0x2501),
             'J': chr(0x251B),
             'F': chr(0x250F),
             '7': chr(0x2513)}


class Node:
    def __init__(self, point, type, to=None, fromn=None):
        self.point = point  # point (x, y)
        self.type = type  # type of pipe: |, L, F, J, 7, -
        self.to = to
        self.fromn = fromn

    def __str__(self):
        return f"{self.type} {self.point}"

    __repr__ = __str__

    def __eq__(self, other):
        return self.point == other.point and self.type == other.type

    def __hash__(self):
        return hash((self.point, self.type))


def firstStep(startnode):
    """
    search the proper direction out of 'S'
    :param startnode:
    :return: nextnode
    """
    if startnode.type == 'S':
        xs = startnode.point[0]
        ys = startnode.point[1]
        if pipemap[ys][xs + 1] in '-J7':
            return Node((xs + 1, ys), pipemap[ys][xs + 1], fromn=startnode)
        elif pipemap[ys][xs - 1] in '-FL':
            return Node((xs - 1, ys), pipemap[ys][xs - 1], fromn=startnode)
        if pipemap[ys + 1][xs] in '|LJ':
            return Node((xs, ys + 1), pipemap[ys + 1][xs], fromn=startnode)
        elif pipemap[ys - 1][xs] in '|F7':
            return Node((xs, ys - 1), pipemap[ys - 1][xs], fromn=startnode)


def step(node):
    for shift in pipes[node.type]:
        tmp = (node.point[0] + shift[0], node.point[1] + shift[1])
        if node.fromn is None or tmp != node.fromn.point:
            n = Node(tmp, pipemap[tmp[1]][tmp[0]])
            # create link between actual and next element:
            n.fromn = node
            node.to = n
            return n


def farthest(startp):
    startnode = Node(startp, 'S')
    path = []

    node = firstStep(startnode)
    while node != startnode:
        path.append(node)
        node = step(node)
    else:
        startnode.fromn = node.fromn  # close the pipe loop

    # len(path) = 20 --> 10
    # len(path) = 21 --> 11
    return math.ceil(len(path) / 2)


def loaddata(filename):
    with open(filename, 'r') as f:
        y = 1
        for row in f:
            tmp = '.' + row.replace('\n', '') + '.'
            pipemap.append(list(tmp))
            x = tmp.find('S')
            if x != -1:
                startpoint = (x, y)
            y += 1
        pipemap.append(['.' for i in range(len(pipemap[0]))])
        pipemap.insert(0, ['.' for i in range(len(pipemap[0]))])
    return startpoint


def nest(startp):
    startnode = Node(startp, 'S')
    count = 0

    # --- build the path ---
    path = {}
    node = firstStep(startnode)
    while node != startnode:
        path[node.point] = node
        node = step(node)
    else:
        startnode.fromn = node.fromn  # close the pipe loop

    # --- check the tiles
    y = 0

    for row in pipemap:
        inside = False
        pair = ''
        for x in range(1, len(row)):
            tmp = (x, y)
            if (x, y) in path:
                if pair == '' and path[(x, y)].type in ('L', 'F', '7', 'J'):
                    pair = path[(x, y)].type
                if pair != '' and path[(x, y)].type == '|':
                    pair = ''
                if (pair == 'F' and path[(x, y)].type == '7') or (pair == 'L' and path[(x, y)].type == 'J'):
                    pair = ''

                if path[(x, y)].type == '|':
                    inside = not inside
                elif path[(x, y)].type in ('L', 'F'):
                    if (pair == '7' and path[(x, y)].type == 'L') or (pair == 'J' and path[(x, y)].type == 'F'):
                        pair = ''
                    else:
                        inside = not inside
                elif path[(x, y)].type in ('7', 'J'):
                    if (pair == 'L' and path[(x, y)].type == '7') or (pair == 'F' and path[(x, y)].type == 'J'):
                        pair = ''
                    else:
                        inside = not inside

            if inside and (x, y) not in path:
                count += 1
                pipemap[y][x] = 'X'
        y += 1

    visualise(path)

    return count


def visualise(path):
    for p in path.keys():
        pipemap[p[1]][p[0]] = nicepipes[path[p].type]

    for row in pipemap:
        for tile in row:
            print(tile, end='')
        print()


if __name__ == "__main__":
    startPoint = loaddata("advent10.txt")
    print("Part1:", farthest(startPoint))
    print("Part2:", nest(startPoint))
