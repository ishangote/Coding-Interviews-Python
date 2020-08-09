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
[1, 2, 3, 4, 5] -> shift = 0

[5, 4, 3, 2, 1] -> shift = len(arr) - 1
"""

def shifted_search(nums, target):
    if not nums: return -1
    if len(nums) == 1: return 0 if nums[0] == target else -1
    
    pivot = get_pivot(nums, 0, len(nums) - 1)
    
    # if target is the smallest element
    if nums[pivot] == target: return pivot

    # if array is not rotated, search in the entire array
    if pivot == 0: return get_target(nums, 0, len(nums) - 1, target)

    # search on the right side
    if target < nums[0]: return get_target(nums, pivot, len(nums) - 1, target)
    
    # search on the left side
    return get_target(nums, 0, pivot, target)

def get_pivot(nums, left, right):
    if nums[left] < nums[right]:
        return 0
    
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[pivot + 1]: return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1
        
def get_target(nums, left, right, target):
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        else:
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
    return -1

import unittest
class TestShiftedArraySearch(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(shifted_search([], 0), -1)
        self.assertEqual(shifted_search([2], 2), 0)
        
        self.assertEqual(shifted_search([2, 4, 5, 9, 12, 17], 4), 1)
        self.assertEqual(shifted_search([17, 12, 9, 5, 4, 2], 4), 4)

    def test_generic(self):
        self.assertEqual(shifted_search([9, 12, 17, 2, 4, 5], 2), 3)

if __name__ == "__main__": unittest.main()