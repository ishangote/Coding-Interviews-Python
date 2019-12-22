# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
# Note that even though we want you to return the new length, make sure to change the original array as well in place
# Do not allocate extra space for another array, you must do this in place with constant memory.
"""
Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]

[1, 2, 3, 3, 4, 5] -> [1, 2, 3, 4, 5]
       i
             j

[1, 2, 3, 4, 4, 5] -> [1, 2, 3, 4, 5]
          i
                j
 
[1, 2, 3, 4, 5, 5] -> [1, 2, 3, 4, 5]
             i
                   j
"""

def remove_duplicates_i(arr):
    i, j = 0, 0
    
    while j < len(arr):
        if arr[i] == arr[j]: j += 1
        else:
            arr[i + 1] = arr[j]
            i += 1
    
    arr = arr[: i + 1]
    return len(arr)

import unittest
class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_empty_arr(self):
        self.assertEqual(remove_duplicates_i([]), 0)
    
    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates_i([1, 2, 3, 4]), 4)
    
    def test_generic(self):
        self.assertEqual(remove_duplicates_i([1, 2, 3, 3, 4]), 4)

if __name__ == "__main__": unittest.main()