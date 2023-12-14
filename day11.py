def loaddata(filename):
    with open(filename, 'r') as f:
        y = 1
        for row in f:
            for x in range(len(row)):
                pass
            y += 1


if __name__ == "__main__":
    loaddata("day11_input.txt")
    print("part1: ")
