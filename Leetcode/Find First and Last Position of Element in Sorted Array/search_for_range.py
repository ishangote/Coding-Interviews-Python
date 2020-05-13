# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].
"""
Very GOOD Explanation: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


 0  1  2  3  4  5           target = 8
[5, 7, 7, 8, 8, 10]
 ^     m        ^
 

Approach 1: Linear Scan
[5, 7, 7, 8, 8, 10], target = 8
          ^
             ^
Pointers two iterations one from forward one from back

Approach 2: Modified Binary Search

 0  1  2  3  4  5           target = 8
[5, 7, 7, 8, 8, 10]
 ^     m        ^

          ^  m  ^

          ^m ^

          ^m
          ^
          return left

 0  1  2  3  4  5           target = 8
[5, 7, 7, 8, 8, 10]
          ^     ^m      mid = [(i + j) // 2] + 1 *Make mid biased to right

          ^  ^m         mid = [(i + j) // 2] + 1 *Make mid biased to right

             ^
             ^m 
             return right
"""

def search_for_range(nums, target):
    if not nums: return [-1, -1]
    ans = [-1, -1]
    
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target: lo = mid + 1
        else: hi = mid
            
    if nums[lo] != target: return [-1, -1]
    ans[0] = lo
    
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            lo = mid + 1
        else: hi = mid - 1
            
    ans[1] = hi
    
    return ans

import unittest
class TestSearchForRange(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(search_for_range([], 0), [-1, -1])
    
    def test_generic(self):
        self.assertEqual(search_for_range([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(search_for_range([5, 7, 7, 8, 8, 10], 7), [1, 2])

if __name__ == "__main__": unittest.main()