# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

"""
Questions:
1. len(nums) == 1? No
2. nums[i] -ve? Yes
3. target -ve? Yes
4. multiple pairs? No
5. Use same element twice? No
6. Are numbers sorted? No

Examples:
nums = 
-2 3 0 2
target = 
0

all pairs = 
[
-2, 3
-2, 0
-2, 2 -> 0 return (0, 3)
3, 0
3, 2
0, 2
]

Time: O(n^2)
Space: O(1) Optimization

----------------------

nums = 
-2, 3, 0, 2
target = 0

valid pair = (a, target - a)
ans = [idx(a), idx(target - a)]

  0  1  2  3
[-2, 3, 0, 2]
           i

hm => target - nums[i] : i
hm = {
    2: 0
    -3: 1
    0: 2
}

return [hm[nums[i]], i]

Time: O(n)
Space: O(n)

"""

def two_sum(nums, target):
    hash_map = {}
    for idx, val in enumerate(nums):
        if val in hash_map: return [hash_map[val], idx]
        hash_map[target - val] = idx
    return []

import unittest
class TestTwoSumUnitTest(unittest.TestCase):
    # def test_two_sum_null_input(self):
    #     self.assertEqual(two_sum([], 3), [])
    #     # self.assertEqual(two_sum(None, 3), None)

    def test_two_sum_no_pair(self):
        self.assertEqual(two_sum([1, 3, 7, 5], 3), [])

    def test_two_sum_negative_nums(self):
        self.assertEqual(two_sum([-2, 4, 1, -3, 3], 1), [1, 3])

    def two_sum_generic(self):    
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

if __name__ == "__main__": unittest.main()