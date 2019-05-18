# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

"""
Input: [0,1,0,3,12] Output: [1,3,12,0,0]
     c
[1,3,12,3,12]
     ^
add zeroes
"""
def move_zeroes(arr):
    if not arr or len(arr) == 0: return None
    cur = 0
    for num in arr:
        if num != 0:
            arr[cur] = num
            cur += 1
        
    while cur < len(arr):
        arr[cur] = 0
        cur += 1

    return arr

import unittest
class TestMoveZeroes(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(move_zeroes([]), None)
        self.assertEqual(move_zeroes(None), None)
    
    def all_zeroes_input(self):
        self.assertEqual(move_zeroes([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_no_zero_input(self):
        self.assertEqual(move_zeroes([3, 4, 6, 1]), [3, 4, 6, 1])

if __name__ == "__main__": unittest.main()