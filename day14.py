from datetime import datetime


def totalload(param):
    pass


if __name__ == "__main__":
    t0 = datetime.now()
    print('start:', t0)
    print('Part1:', totalload('day14_input.txt'))  # 21272 is too low
    t1 = datetime.now()
    print('end1:', t1, ' elapsed time:', t1 - t0)
    # print('Part2:', totalload('day14_input.txt'))
    # t2 = datetime.now()
    # print('end2:', t2, ' elapsed time:', t2 - t1)
