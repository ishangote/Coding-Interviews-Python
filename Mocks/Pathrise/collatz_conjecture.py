"""
Given a starting positive number n, we create a sequence of numbers as follows. If n is even, the next number in the sequence is n/2. If n is 1, the sequence ends. If n any other odd number, the next number in the sequence can be either 3n+1 or 3n-1.
Given a starting number ‘start’ and a number ‘target’, can the sequence start at start and reach target? Return the sequence if yes, return an empty list if not
"""
# Examples (solutions are not unique:
# start = 3, target = 7
# [3, 10, 5, 14, 7]   

# start = 4, target = 7
# []

# start = 5, target = 7
# [5, 14, 7]

# start = 11, target = 7
# [11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7]

# start = 15, target = 7
# [15, 44, 22, 11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7]

# VERY IMPORTANT NOTE:
# We don’t have a way to know how long the sequence could be, or how many numbers we could visit before finding it. 
# The numbers could grow very large. Thus, we add a maximum number of iterations. 
# If we reach this limit, it means we didn’t find a sequence, but maybe it really exists.

def get_path(start, target, prev_nums):
    #prev_nums -> prev_num[i] = parent of nbr
    ans = []
    cur = target

    while cur != start:
        ans.append(cur)
        cur = prev_nums[cur]
    
    ans.append(start)
    return ans[::-1]

def get_neighbors(num):
    if num == 1: return []
    if num % 2 == 0: return [num // 2]
    return [num * 3 - 1, num * 3 + 1]

# BFS
from collections import deque
def collatz_tree(start, target):
    max_iters = 0
    prev_nums = {}
    queue = deque([start])

    while queue:
        cur = queue.pop()
        if cur == target:
            return get_path(start, target, prev_nums)
        if max_iters == 10000: 
            print("didn't find a sequence but maybe it exists")
            return[]
        max_iters += 1
        for nbr in get_neighbors(cur):
            if not nbr in prev_nums:
                prev_nums[nbr] = cur
                queue.appendleft(nbr)

    return []

import unittest
class TestCollatzTree(unittest.TestCase):
    def test_all(self):
        self.assertEqual(collatz_tree(3, 7), [3, 10, 5, 14, 7])
        self.assertEqual(collatz_tree(11, 7), [11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7])
        self.assertEqual(collatz_tree(15, 7), [15, 44, 22, 11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7])

if __name__ == "__main__": unittest.main()