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


class Node:
    def __init__(self, point, type):
        self.point = point  # point (x, y)
        self.type = type  # type of pipe: |, L, F, J, 7, -

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
            return Node((xs + 1, ys), pipemap[ys][xs + 1])
        elif pipemap[ys][xs - 1] in '-FL':
            return Node((xs - 1, ys), pipemap[ys][xs - 1])
        if pipemap[ys + 1][xs] in '|LJ':
            return Node((xs, ys + 1), pipemap[ys + 1][xs])
        elif pipemap[ys - 1][xs] in '|F7':
            return Node((xs, ys - 1), pipemap[ys - 1][xs])


def step(node, prevnode):
    for shift in pipes[node.type]:
        tmp = (node.point[0] + shift[0], node.point[1] + shift[1])
        if prevnode is None or tmp != prevnode.point:
            return Node(tmp, pipemap[tmp[1]][tmp[0]])


def farthest(startp):
    startnode = Node(startp, 'S')
    path = []

    node = firstStep(startnode)
    prevnode = startnode
    while node != startnode:
        if path:  # list is not empty
            prevnode = path[-1]
        path.append(node)
        node = step(node, prevnode)

    # len(path) = 20 --> 10
    # len(path) = 21 --> 11
    return math.ceil(len(path) / 2)


def loaddata(filename):
    with open(filename, 'r') as f:
        y = 1
        for row in f:
            tmp = '.' + row.replace('\n', '') + '.'
            pipemap.append(tmp)
            x = tmp.find('S')
            if x != -1:
                startpoint = (x, y)
            y += 1
        pipemap.append('.' * len(pipemap[0]))
        pipemap.insert(0, '.' * len(pipemap[0]))
    return startpoint


if __name__ == "__main__":
    startPoint = loaddata("day10_input.txt")
    print("Part1:", farthest(startPoint))
