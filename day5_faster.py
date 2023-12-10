from datetime import datetime

seeds = []
levels = {}  # {'seed':[Mapping, ... ] }


class Mapping:
    def __init__(self, name, start, end, childname, toop=0):
        """

        :param name: jelenlegi szint neve pl: 'seed'
        :param start: intervallum kezdete
        :param end: intervallum vége
        :param childname: következő szint neve pl 'soil'
        :param toop: mapping művelet, ami a jelenlegi intervallumot átviszi a következőbe. Pl: +4 vagy -4 -> néggyel eltolja a ranget
        """
        self.name = name
        self.childname = childname
        self.start = start
        self.end = end
        self.toop = toop

    def __str__(self):
        return f"Mapping(name={self.name}, start={self.start}, end={self.end}, childname={self.childname}, toop={self.toop})"

    __repr__ = __str__

    def __eq__(self, other):
        return self.__str__() == other.__str__()


def loadData(filename):
    with open(filename) as f:
        for row in f:
            if row.rstrip() == '':  # skip empty row
                continue

            if row.startswith('seeds:'):
                tmp = row.split(' ')
                for i in range(len(tmp)):
                    if i == 0:
                        continue
                    if i % 2 == 1:
                        seeds.append((int(tmp[i]), int(tmp[i]) + int(tmp[i + 1]) - 1))
            elif 'map:' in row:
                current, nextto = row.split(' ')[0].split('-to-')
                # print(current, nextto)
            else:
                target, source, count = row.split(' ')
                clist = levels.setdefault(current, [])
                clist.append(Mapping(current, int(source), int(source) + int(count) - 1, childname=nextto, toop=int(target) - int(source)))


def minimumLoc(range, levelname, dept=0):
    """

    :param dept:
    :param range: (start1, end1)
    :param levelname:
    :return:
    """
    tabs = ' ' * dept
    # print(f"{tabs}{levelname}: {range[0]} -> {range[1]}")
    if 'location' == levelname:
        return range[0]
    else:
        minloc = 100000000000
        nextlevelname = levels[levelname][0].childname
        found = False
        for m in levels[levelname]:
            if range[0] >= m.start and range[1] <= m.end:  # ha a range teljes egészében benne van a mappingban
                tmp = minimumLoc(shift(range, m), nextlevelname, dept + 1)
                if minloc > tmp:
                    minloc = tmp
                found = True
                break
            elif m.start <= range[0] < m.end:  # ha a range eleje van benne a mappingban
                part1 = (range[0], m.end)
                tmp = minimumLoc(shift(part1, m), nextlevelname, dept + 1)
                if minloc > tmp:
                    minloc = tmp

                part2 = (m.end + 1, range[1])
                tmp = minimumLoc(part2, levelname, dept)
                if minloc > tmp:
                    minloc = tmp
                found = True
                break
            elif range[0] < m.start and m.start <= range[1] <= m.end: # ha a range vége van benne a mappingban
                part1 = (range[0], m.start-1)
                tmp = minimumLoc(part1, levelname, dept)
                if minloc > tmp:
                    minloc = tmp

                part2 = (m.start, range[1])
                tmp = minimumLoc(shift(part2, m), nextlevelname, dept + 1)
                if minloc > tmp:
                    minloc = tmp
                found = True
                break
            elif range[0] < m.start and m.end < range[1]: # ha a range nagyobb mint a mapping, azaz a közepe van benne
                part1 = (range[0], m.start - 1)
                tmp = minimumLoc(part1, levelname, dept)
                if minloc > tmp:
                    minloc = tmp

                part2 = (m.start, m.end)
                tmp = minimumLoc(shift(part2, m), nextlevelname, dept + 1)
                if minloc > tmp:
                    minloc = tmp

                part3 = (m.end + 1, range[1])
                tmp = minimumLoc(part3, levelname, dept)
                if minloc > tmp:
                    minloc = tmp

                found = True
                break

        if not found:
            tmp = minimumLoc(range, nextlevelname, dept + 1)
            if minloc > tmp:
                minloc = tmp

        return minloc


def shift(range, mapping):
    return range[0] + mapping.toop, range[1] + mapping.toop


def getPerfectSeed():
    minloc = 100000000000
    for range in seeds:
        tmp = minimumLoc(range, 'seed', 0)
        if minloc > tmp:
            minloc = tmp

    return minloc


if __name__ == "__main__":
    loadData("day5_input.txt")
    t0 = datetime.now()
    print('start:', t0)
    print("part2:", getPerfectSeed())
    # 4917124
    t1 = datetime.now()
    print('end:', t1, ' elapsed time:', t1 - t0)

