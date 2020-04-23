"""
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. 
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.
Explain your solution and analyze its time and space complexities.

Example:
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3

[9, 12, 17, 2, 4, 5]
            p
Step 1: Find Pivot (Binary Search) -> O(logn)
        P property => arr[p - 1] > arr[p]
Step 2: Find target (Binary Search) -> O(logn)

Edge Cases to consider:
[2] t = 2

 0  1   2   3   4       target = 11
[8, 11, 15, 18, 21] -> shift = 0
 L      M       R
            L


[2]


 
 0  1  2  3  4  5  6
[8, 9, 2, 3, 4, 5, 6]
 l        m        r
 l  m  r
       lrm

 0  1  2  3  4  5  6
[5, 6, 8, 9, 2, 3, 4]
"""
def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target: right = mid - 1
        else: left = mid + 1
    
    return -1

def get_pivot(nums):
    if not nums: return None
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo

def shifted_search(nums, target):
    pivot = get_pivot(nums)

    if nums[pivot] <= target <= nums[-1]:
        return binary_search(nums, target, pivot, len(nums) - 1)
    
    else:
        return binary_search(nums, target, 0, pivot - 1)

import unittest
class TestShiftedArraySearch(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(shifted_search([2], 2), 0)
        self.assertEqual(shifted_search([2, 6, 8, 11], 6), 1)

    def test_generic(self):
        self.assertEqual(shifted_search([9, 12, 17, 2, 4, 5], 2), 3)

if __name__ == "__main__": unittest.main()