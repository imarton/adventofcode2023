import re


def getPartNumberSum(schema):
    result = 0
    width = len(schema[0])
    schema.insert(0, '.' * width)
    schema.append('.' * width)

    height = len(schema)
    y = 1   # a 0. és az utolsó sort kihagyjuk
    while y < height-1:
        partSum = 0
        print('\n', y, schema[y])
        p1 = re.findall(r"(\d+)", schema[y])
        p = set(p1)
        dupl = (len(p) == len(p1))
        for n in p:
            x = schema[y].find(n)
            while x != -1:
                area = schema[y-1][x-1: x+len(n)+1] + "\n" + schema[y][x-1: x+len(n)+1] + "\n" + schema[y+1][x-1: x+len(n)+1]
                if dupl:
                    print(area)
                p = re.search(r'[^\d\.\n]', area)
                if p is not None:
                    if dupl:
                        print('---------------> ', int(n), '-', n, p.group())
                    result += int(n)
                    partSum += int(n)
                x = schema[y].find(n, x+len(n)+1)
        # print(y, ". sor: ",partSum)
        y += 1

    # print(p)

    return result


if __name__ == '__main__':
    result = 0
    f = open("day3_input.txt", "r")
    schematic = []

    while True:
        line = f.readline().replace('\n', '').replace('\r', '')
        if len(line) == 0:
            break
        schematic.append('.' + line + '.')

    f.close()

    result = getPartNumberSum(schematic)
    print(result)
    # 546312 - jó
