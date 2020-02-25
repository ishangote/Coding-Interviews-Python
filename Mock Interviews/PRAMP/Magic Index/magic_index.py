"""
Objective: Given a sorted array of distinct integers, Find the Magic index or Fixed point in the array.
Magic Index or Fixed Point: Magic index or a Fixed point in an array is an index i in the array such that A[i] = i.

Example :
int[] A = [-1, 0, 1, 2, 4, 10]
Magic index or fixed point is : 4

Binary Search

"""

def magic_index(arr):
    if not arr: return -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid = arr[mid_idx]
        
        if mid == mid_idx: return mid_idx
        elif mid_idx > mid: left = mid + 1
        else: right = mid - 1

    return -1

import unittest
class TestMagicIndex(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(magic_index([-1, 0, 1, 2, 4, 10]), 4)

if __name__ == "__main__": unittest.main()