# Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
# Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
# Return a list of ids of selected elements. If no pair is possible, return an empty list.

"""
Questions:
1. Are the values sorted? No
2. Multiple pairs? Return all

Examples:
Input:
a = [[1, 2], [2, 4], [3, 6]]
                i
b = [[1, 2]]
        j
target = 7

Output: [[2, 1]]

Brute Force:
For all the pairs check diff. and return idx
Time: O(n * m), n => len(a), m =. len(b)
Space: O(1)

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.


Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
                        i
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
                j
target = 10

res = [(-10, [2, 4]), (-10, [3, 2])]

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].


Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]


Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
"""
def optimal_utilization(a, b, target):
    a = sorted(a, key = lambda x: x[1])
    b = sorted(b, key = lambda x: x[1])

    res = []

    idx_a = 0
    idx_b = len(b) - 1
    
    while idx_a < len(a) and idx_b >= 0:
        cur_diff = target - (a[idx_a][1] + b[idx_b][1])
        if cur_diff < 0:
            idx_b -= 1
            continue
        elif not res or cur_diff == res[-1][0]: 
            res.append((cur_diff, [a[idx_a][0], b[idx_b][0]]))
        elif cur_diff < res[-1][0]:
            res.clear()
            res.append((cur_diff, [a[idx_a][0], b[idx_b][0]]))
        idx_a += 1

    return [idx[1] for idx in res]

import unittest
class TestOptimalUtilization(unittest.TestCase):
    def test_generic(self):
        self.assertEqual([[2, 4], [3, 2]], optimal_utilization([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10))
        self.assertEqual([[3, 1]], optimal_utilization([[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20))
        self.assertEqual([[1, 3], [3, 2]], optimal_utilization([[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20))

if __name__ == "__main__": unittest.main()