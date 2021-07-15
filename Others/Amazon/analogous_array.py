import sys
def func (consecutiveDifference, lowerBound, upperBound):
    res = 0
    min_num = sys.maxsize
    max_num = -sys.maxsize
    tot = 0

    for i in consecutiveDifference:
        tot += i
        min_num = min(min_num, tot)
        max_num = max(max_num, tot)

    diff = max_num - min_num
    if max_num < 0 and min_num < 0: diff += 1

    lowerBound += 1

    res = upperBound - lowerBound + 1

    if res > 0: return res
    else: return 0