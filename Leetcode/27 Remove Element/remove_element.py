"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.

Return k.

## Questions:
1. Numbers can be +ve/-ve/0
2. val can be +ve/-ve/0

Examples:
Input:
val = 2
nums = 
[2, 3, 4, 3, 2]
 i
 j

[3, 2, 4, 3, 2]
 i
    j

[3, 4, 2, 3, 2]
    i
       j

[3, 4, 3, 2, 2]
       i
          j

[3, 4, 3, 2, 2]
          i
                j

return i
"""

def remove_element(nums, val):
     swap_pointer = 0
     
     for idx in range(len(nums)):
          if nums[idx] == val: continue
          nums[swap_pointer], nums[idx] = nums[idx], nums[swap_pointer]
          swap_pointer += 1
     
     return swap_pointer

import unittest
class TestRemoveElement(unittest.TestCase):
     def test_remove_element(self):
          self.assertEqual(remove_element([2, 3, 4, 3, 2], 2), 3)
          self.assertEqual(remove_element([3,2,2,3], 3), 2)

if __name__ == "__main__": unittest.main()
