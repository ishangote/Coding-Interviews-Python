# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""
nums = 
[1, 2, 3, 4]
    ^
[1, 1, 2, 6] <= forward pass
[24, 12, 8, 6] <= backward pass

[A1, A2, A3]
forward pass =>
prev = 1
[1, ]

prev = 1 * A1
[1, A1, ]

prev = 1 * A1 * A2
[1, A1, A1A2]

backward pass =>
prev = 1
[1,A1,A1A2]

prev = 1 * A3
[1,A1A3,A1A2]

prev = 1 * A3 * A2
[A2A3,A1A3,A1A2]

"""

def product_except_self(nums):
    if not nums or len(nums) == 1: return None
    # Forward Pass
    prev = 1
    forward = []
    for idx in range(len(nums)):
        forward.append(prev)
        prev *= nums[idx]

    # Backward pass
    prev = 1
    for idx in range(len(nums) - 1, -1, -1):
        forward[idx] *= prev
        prev *= nums[idx]
    
    return forward

import unittest
class TestProductExceptSelf(unittest.TestCase):
    def test_pramp(self):
        self.assertEqual(product_except_self([]), None)
        self.assertEqual(product_except_self([1]), None)
        self.assertEqual(product_except_self([2, 2]), [2, 2])
        self.assertEqual(product_except_self([2, 7, 3, 4]), [84, 24, 56, 42])
        self.assertEqual(product_except_self([2, 3, 0, 982, 10]), [0, 0, 58920, 0, 0])

if __name__ == "__main__": unittest.main()