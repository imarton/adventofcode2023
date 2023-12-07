seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def loadData(filename):
    f = open(filename, 'r')
    i = 0
    flag = '-'
    for line in f:
        line = line.replace('\n', '')
        i += 1
        if i == 1:
            for v in line.split(' '):
                if v == 'seeds:':
                    continue
                seeds.append(int(v))
            continue

        if line.endswith('map:'):
            flag = line
        else:
            if (line is None) or (line.strip() == ""):
                continue
            d, s, r = line.split(' ')  # destination, source, range
            if flag == 'seed-to-soil map:':
                seed_to_soil.append((int(s), int(d), int(r)))
            elif flag == 'soil-to-fertilizer map:':
                soil_to_fertilizer.append((int(s), int(d), int(r)))
            elif flag == 'fertilizer-to-water map:':
                fertilizer_to_water.append((int(s), int(d), int(r)))
            elif flag == 'water-to-light map:':
                water_to_light.append((int(s), int(d), int(r)))
            elif flag == 'light-to-temperature map:':
                light_to_temperature.append((int(s), int(d), int(r)))
            elif flag == 'temperature-to-humidity map:':
                temperature_to_humidity.append((int(s), int(d), int(r)))
            elif flag == 'humidity-to-location map:':
                humidity_to_location.append((int(s), int(d), int(r)))
            else:
                print('azonosítatlan,', i, '. sor: ', line)

    f.close()


def getMappedValue(value, map):
    ret = value
    for m in map:
        if m[0] <= value < m[0]+m[2]:
            ret = m[1] + (value - m[0])

    return ret


def getLocation(seed):
    v = getMappedValue(seed, seed_to_soil)
    v = getMappedValue(v, soil_to_fertilizer)
    v = getMappedValue(v, fertilizer_to_water)
    v = getMappedValue(v, water_to_light)
    v = getMappedValue(v, light_to_temperature)
    v = getMappedValue(v, temperature_to_humidity)
    return getMappedValue(v, humidity_to_location)


def getLowest():
    result = 'N/A'
    for seed in seeds:
        v = getLocation(seed)
        if 'N/A' == result:
            result = v
        elif result > v:
            result = v

    return result


if __name__ == '__main__':
    loadData("day5_input.txt")
    print('Part1:', getLowest())
    # print('Part2:', getDeckSize("day4_input.txt"))
