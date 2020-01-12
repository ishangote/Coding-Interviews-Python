"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""

#Gauss' Formula
def missing_number(nums):
    n = len(nums) 
    return n * (n+1) / 2 - sum(nums)

#Bit Manipulation
#We can harness the fact that XOR is its own inverse to find the missing element in linear time.
#XOR => true (1 or HIGH) output when the number of true inputs is odd.
def missing_number_bit(nums):
    ans = len(nums)
    for i, v in enumerate(nums):
        ans ^= i ^ v
    return ans

import unittest
class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        self.assertEqual(missing_number([1, 0, 3, 4, 5]), 2)
        self.assertEqual(missing_number_bit([1, 0, 3, 4, 5]), 2)

if __name__ == "__main__": unittest.main()
        