# Given an array of integers A of size N and an integer B.
# array A is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
# You are given a target value B to search. If found in the array, return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# NOTE:- Array A was sorted in non-decreasing order before rotation.
"""
Input Format:
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format: Return index of B in array A, otherwise return -1

Constraints:
1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.

For Example
Input 1:
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
Output 1: 0
Explanation 1: Target 4 is found at index 0 in A.

Input 2:
    A = [5, 17, 100, 3]
    B = 6
Output 2: -1
"""
def binary_search(nums, target, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[mid] > target: hi = mid - 1
        else: lo = mid + 1
    return -1
    
def get_pivot(nums):
    if not nums: return -1
    lo, hi = 0, len(nums) - 1
    
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]: lo = mid + 1
        else: hi = mid
        
    return lo
    
def search(A, B):
    pivot = get_pivot(A)
    if A[pivot] <= B <= A[-1]: return binary_search(A, B, pivot, len(A) - 1)
    else: return binary_search(A, B, 0, pivot - 1)

import unittest
class TestShiftedArraySearch(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(search([2], 2), 0)
        self.assertEqual(search([2, 6, 8, 11], 6), 1)

    def test_generic(self):
        self.assertEqual(search([9, 12, 17, 2, 4, 5], 2), 3)

if __name__ == "__main__": unittest.main()