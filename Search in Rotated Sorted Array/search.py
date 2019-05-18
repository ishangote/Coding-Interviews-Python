# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

"""
 0 1 2 3 4 5 6
[4,5,6,7,0,1,2] target = 1
 ^       r      


 0 1 2 3 4 5 6
[4,5,6,7,0,1,2] target = 5
 ^       r 
   m
 l     r

"""

def get_rotation_index(arr): return arr.index(min(arr))

def binary_search(i, j, arr, target):
    while i <= j:
        mid = (i + j) // 2
        if target == arr[mid]: return mid
        if target > arr[mid]: i += 1
        else: j -= 1

    return -1

def search_rotated_arr(arr, target):

    if not arr or len(arr) == 0: return -1
    rotation_index = get_rotation_index(arr)
    #if rotation_index == 0 => the array is already sorted
    if rotation_index == 0: return binary_search(0, len(arr), arr, target)
    if target == arr[rotation_index]: return rotation_index 
    if target == arr[0]: return 0
    if target > arr[0]: return binary_search(0, rotation_index - 1, arr, target)
    else: return binary_search(rotation_index, len(arr) - 1, arr, target)

import unittest
class TestSearchRotatedSortedArray(unittest.TestCase):
    def test_generic_examples(self):
        self.assertEqual(search_rotated_arr([1, 3], 3), 1)

if __name__ == "__main__": unittest.main()