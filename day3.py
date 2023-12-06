import logging
import re
import sys

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)


def getPartNumberSum(schema):
    result = 0
    width = len(schema[0])
    schema.insert(0, '.' * width)
    schema.append('.' * width)
    height = len(schema)
    patternNum = re.compile(r'\d+')  #összefüggő számjegyek
    patternSymbol = re.compile(r'[^\d\.\n]')  #szimbólum keresése

    y = 1   # a 0. és az utolsó sort kihagyjuk
    while y < height-1:
        logging.debug('\n%s %s', y, schema[y])
        matches = patternNum.finditer(schema[y])
        for match in matches:
            sp = match.start()  #start position
            ep = match.end()    #end position
            logging.debug('\n%s (%s-%s)', match.group(), sp, ep)
            area = schema[y - 1][sp - 1: ep + 1] + "\n" + schema[y][sp - 1: ep + 1] + "\n" + schema[y + 1][sp - 1: ep + 1]
            logging.debug('\n'+area)
            m =patternSymbol.search(area)
            if m is not None:
                result += int(match.group())
                logging.info('----> %s %s', match.group(), m.group())

        y += 1

    return result


def getGearRationSum(schema):
    result = 0
    width = len(schema[0])
    schema.insert(0, '.' * width)
    schema.append('.' * width)
    height = len(schema)
    patternStar = re.compile(r'\*')  # szimbólum keresése
    patternNum = re.compile(r'\d+')  # összefüggő számjegyek

    y = 1  # a 0. és az utolsó sort kihagyjuk
    while y < height - 1:
        logging.debug('\n%s %s', y, schema[y])
        matches = patternStar.finditer(schema[y])
        lineRatio = 0
        for match in matches:
            ratio = 1
            sp = match.start()  # start position
            logging.debug('\n%s (%s)', match.group(), sp)
            tmp = []
            matchesNums = patternNum.finditer(schema[y-1])
            for m in matchesNums:
                if m.start()-1 <= sp <= m.end():
                    tmp.append(m.group())
                    ratio *= int(m.group())

            matchesNums = patternNum.finditer(schema[y])
            for m in matchesNums:
                # logging.debug('%s (%s:%s)', m.group(), m.start(), m.end())
                if m.start() == sp+1 or sp == m.end():
                    tmp.append(m.group())
                    ratio *= int(m.group())

            matchesNums = patternNum.finditer(schema[y + 1])
            for m in matchesNums:
                if m.start() - 1 <= sp <= m.end():
                    tmp.append(m.group())
                    ratio *= int(m.group())
            if len(tmp) == 2:
                lineRatio += ratio
            logging.debug('* kapcsolatai: %s\nsor ratio: %s\nlineRatio: %s', tmp, ratio, lineRatio)
        result += lineRatio
        y += 1

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
    print('Part1:', result)

    result = getGearRationSum(schematic)
    print('Part2:', result)
