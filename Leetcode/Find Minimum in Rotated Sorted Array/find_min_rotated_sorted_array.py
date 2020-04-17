"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2] 
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""

def find_minimum(nums):
    if not nums: return None
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

import unittest
class TestFindMinimumRotatedSortedArray(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(find_minimum([]), None)
        self.assertEqual(find_minimum([1]), 1)

    def test_sorted(self):
        self.assertEqual(find_minimum([1, 2, 3, 4]), 1)
        self.assertEqual(find_minimum([1, 2, 3, 4, 5, 6, 7]), 1)

    def test_generic(self):
        self.assertEqual(find_minimum([3,4,5,1,2]), 1)
        self.assertEqual(find_minimum([5, 6, 1, 2, 3, 4]), 1)
        self.assertEqual(find_minimum([5, 6, 7, 1, 2, 3, 4]), 1)
        self.assertEqual(find_minimum([2, 3, 4, 5, 6, 7, 8, 1]), 1)
        self.assertEqual(find_minimum([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_minimum([2,1]), 1)

if __name__ == "__main__": unittest.main()