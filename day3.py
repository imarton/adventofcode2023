import logging
import re
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


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
