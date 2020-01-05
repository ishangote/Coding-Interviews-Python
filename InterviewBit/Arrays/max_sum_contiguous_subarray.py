"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:
Given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
For this problem, return the maximum sum.
"""

"""
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
[-2, max(1 + -2, 1), ...]
     ^
max_sum till pointer
"""
def max_sum(nums):
    if not nums: return 0
    ans = curr_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        ans = max(ans, curr_sum)

    return ans

import unittest
class TestKadanesAlgorithm(unittest.TestCase):
    def test_null_array(self):
        self.assertEqual(max_sum([]), 0)

    def test_all_negative_array(self):
        self.assertEqual(max_sum([-5, -3, -12, -5, -3]), -3)

    def test_one_element(self):
        self.assertEqual(max_sum([3]), 3)

    def test_mixed_array(self):
        self.assertEqual(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sum([-3, 1, 0, -2, 3, 4, -1, 4, -2]), 10)
        self.assertEqual(max_sum([9, 8, -1, -2, -3]), 17)

if __name__ == "__main__": unittest.main()