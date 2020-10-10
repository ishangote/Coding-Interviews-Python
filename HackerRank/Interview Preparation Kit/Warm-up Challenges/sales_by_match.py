# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
"""
Questions:
1. Is the input sorted? -> No
2. Can we sort the input? -> Yes

Examples:
[-1, 2, 3, 2, -1, -1]
Sort
[-1, -1, -1, 2, 2, 3]
                   i
count = 2

Brute Force:
Time: O(nlogn)
Space: O(n) for tim sort python

Set = {-1, 2, 3}
[-1, 2, 3, 2, -1, -1]
  
count_socks = {
    -1: 3
    2: 2
    3: 1
}
pairs += val // 2

"""
from collections import Counter
def sales_by_match(n, arr):
    count_socks = Counter(arr)
    pairs = 0
    for sock in count_socks:
        pairs += count_socks[sock] // 2
    return pairs

"""
Testcases:
In                  Expected            Actual
[]                  0                   0
[-2]                0                   0
[-2, -1]            0                   0
[1, 1, 3]           1                   1
"""

"""
Time: O(n)
Space: O(n)
"""