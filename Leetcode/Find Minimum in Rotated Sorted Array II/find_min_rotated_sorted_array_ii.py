"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
def find_minimum_ii(nums):
   if not nums: return None
   lo, hi = 0, len(nums) - 1
   while lo < hi:
      mid = (lo + hi) // 2
      if nums[mid] > nums[hi]:
         lo = mid + 1
      else:
         hi = mid if nums[hi] != nums[mid] else hi - 1
   return nums[lo]

import unittest
class TestFindMinimumRotatedSortedArray(unittest.TestCase):
    def test_edge(self):
      self.assertEqual(find_minimum_ii([]), None)
      self.assertEqual(find_minimum_ii([1]), 1)

    def test_sorted(self):
      self.assertEqual(find_minimum_ii([1, 2, 2, 2, 3, 4]), 1)
      self.assertEqual(find_minimum_ii([1, 1, 1, 1, 2, 3, 4, 5, 6, 7]), 1)

    def test_generic(self):
      self.assertEqual(find_minimum_ii([2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2]), 0)
      self.assertEqual(find_minimum_ii([2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2]), 0)
      self.assertEqual(find_minimum_ii([3,4,5, 5, 5,1,2]), 1)
      self.assertEqual(find_minimum_ii([5, 6, 1, 2, 3, 4]), 1)
      self.assertEqual(find_minimum_ii([5, 6, 7, 7, 7, 1, 2, 3, 3, 3, 4]), 1)
      self.assertEqual(find_minimum_ii([2, 3, 3, 3, 4, 5, 6, 7, 8, 1, 1]), 1)
      self.assertEqual(find_minimum_ii([3, 4, 5, 1, 2]), 1)
      self.assertEqual(find_minimum_ii([2,1]), 1)
      
if __name__ == "__main__": unittest.main()