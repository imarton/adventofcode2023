import re
from datetime import datetime


def check(sample, groups, isFirst=False, startpos=0):
    """
    Check that the sample meets the requirements
    :param startpos:
    :param isFirst: True if it is the first group
    :param sample: char list, for example:  .###....
    :param groups: block wide e.g: 3 -> ###
    :return: if it doesn't then return -1
    if it does then return index of group end in the sample e.g: 3
    """
    if len(groups) == 1 and sample.count('#') != groups[0]:  # last elem
        return -1

    spring = '#' * groups[0]
    # if sample == spring:
    #     return group - 1

    if -1 < sample.find(spring) < startpos:
        return -1

    if isFirst:
        p = r'^\.*(#{' + str(groups[0]) + r'})([\.?]+#+)*[\.?]*$'
    else:
        p = r'^\.+(#{' + str(groups[0]) + r'})([\.?]+#+)*[\.?]*$'
    # e.g: ^\.*#{3}([\.?]+#+)*[\.?]*$
    m = re.search(p, sample)
    if m is None:
        return -1

    return m.end(1) - 1


def merge(pattern, groupsize, startposition):
    errormsg = 'Error'
    if len(pattern) < groupsize + startposition:
        return errormsg

    # build tmp string/array,
    # e.g:  groupsize = 3 and startpos = 3  => '...###'
    tmp = ['.' for i in range(groupsize + startposition)]
    for i in range(startposition, startposition + groupsize):
        tmp[i] = '#'

    p = list(pattern)
    # merge tmp string and pattern
    # e.g: '...###' + '..??##?????????' => '...###?????????'
    for i in range(len(tmp)):
        if p[i] == '?':
            p[i] = tmp[i]
        elif tmp[i] == '#' and p[i] != '#':
            return errormsg

    return ''.join(p)


def process(pattern, groups, dept=0):
    if len(pattern) < groups[0]:
        return 0

    spring = '#' * groups[0]
    if '?' not in pattern and spring not in pattern:
        return 0

    # if '?' not in pattern:
    #     if check(pattern, groups[0], dept == 0) > -1:
    #         return 1
    #     else:
    #         return 0

    # i = pattern.find(spring)  # '?###???' and group=3
    # if i > -1 and len(groups) == 1 and pattern[:i].count('?') < groups[0]:
    #     return 1

    cnt = 0
    for i in range(len(pattern) - groups[0] + 1):
        sample = merge(pattern, groups[0], i)
        endOfSegment = check(sample, groups, dept == 0, i)
        if endOfSegment == -1:
            continue
        elif len(groups) == 1:
            # visu(sample, '', '', dept)
            cnt += 1
        else:
            # visu(sample, '', '', dept)
            cnt += process(pattern[endOfSegment + 1:], groups[1:], dept + 1)
    # if cnt > 0: visu(pattern, groups, cnt, dept)
    return cnt


def visu(pattern, groups, result, dept):
    tab = '\t' * dept
    print(f"{pattern:>30} {str(groups):<15} --> {result}")
    # print(tab, pattern, groups, '-->', result)


def arrangements(filename):
    sum = 0
    with open(filename, 'r') as f:
        i = 1
        for row in f:
            pattern, groups = row.replace('\n', '').split(' ')
            groups = [int(i) for i in groups.split(',')]
            sum += process(pattern, groups)
            i += 1

    return sum


def unfold(pattern, groups):
    pattern = '?'.join([pattern for i in range(5)])
    groups = ','.join([groups for i in range(5)])
    return pattern, groups


def arrangements2(filename):
    sum = 0
    with open(filename, 'r') as f:
        i = 1
        for row in f:
            pattern, groups = row.replace('\n', '').split(' ')
            pattern, groups = unfold(pattern, groups)
            groups = [int(i) for i in groups.split(',')]
            t0 = datetime.now()
            x = process(pattern, groups)
            t1 = datetime.now()
            sum += x
            print(f"{i}. {x} elapsed time:{t1 - t0}")
            i += 1
    return sum


if __name__ == "__main__":
    t0 = datetime.now()
    print('start:', t0)
    print('Part1:', arrangements('day12_input.txt'))
    t1 = datetime.now()
    print('end1:', t1, ' elapsed time:', t1 - t0)
    print('Part2:', arrangements2('day12_input.txt'))
    t2 = datetime.now()
    print('end2:', t2, ' elapsed time:', t2 - t1)
