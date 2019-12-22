# Given a sorted array nums, 
# remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.
"""
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, 
with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, 
with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.

"""

def remove_duplicates_ii(arr):
    i = 0
    
    for j in range(len(arr)):
        if i < 2 or arr[j] != arr[i - 1] or arr[j] != arr[i - 2]:
            arr[i] = arr[j]
            i += 1
    
    arr = arr[:i]
    return len(arr)

import unittest
class TestRemoveDupliatesFromArrayII(unittest.TestCase):
    def test_empty_arr(self):
        self.assertEqual(remove_duplicates_ii([]), 0)
    
    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates_ii([1, 2, 3, 4]), 4)
    
    def test_generic(self):
        self.assertEqual(remove_duplicates_ii([1, 2, 3, 3, 3, 4]), 5)

if __name__ == "__main__": unittest.main()