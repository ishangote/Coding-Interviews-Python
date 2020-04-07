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

nums[mid - 1] > nums[mid]: return nums[mid]
nums[l] > nums[r]: l = m + 1

 0  1  2  3  4
[3, 4, 5, 1, 2]
          l          
             r
          m

 0  1  2  3  4
[4, 6, 7, 9, 10]
 l           
       r
       m

"""

def find_minimum(nums):
    if not nums: return None
    if nums[0] < nums[-1]: return nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid - 1]: return nums[mid]

        if nums[mid] < nums[0]: right = mid - 1
        else: left = mid + 1

    return nums[0]

import unittest
class TestFindMinimumRotatedSortedArray(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(find_minimum([]), None)
        self.assertEqual(find_minimum([1]), 1)
    def test_sorted(self):
        self.assertEqual(find_minimum([1, 2, 3]), 1)

    def test_generic(self):
        self.assertEqual(find_minimum([3,4,5,1,2]), 1)
        self.assertEqual(find_minimum([2,1]), 1)

if __name__ == "__main__": unittest.main()