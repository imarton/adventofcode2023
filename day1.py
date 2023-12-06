
f = open("day1_input.txt", "r")
result = 0

digiMap = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
strDigits = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7',
              'eight', '8', 'nine', '9']


def getCalibrationValue2(line):
    firstPos = 255
    firstVal = ''
    lastPos = -1
    lastVal = ''
    for s in strDigits:
        idx = line.find(s)
        while idx != -1:
            if firstPos > idx:
                firstPos = idx
                firstVal = s
            if lastPos < idx:
                lastPos = idx
                lastVal = s
            idx = line.find(s, idx+1)

    if firstVal in digiMap.keys():
        firstVal = digiMap[firstVal]

    if lastVal in digiMap.keys():
        lastVal = digiMap[lastVal]

    return int(firstVal + lastVal)

while True:
    line = f.readline()
    if len(line) == 0:
        break

    x = getCalibrationValue2(line)
    # print(line, ' -- ', x)
    result += x

f.close()

print(result)
