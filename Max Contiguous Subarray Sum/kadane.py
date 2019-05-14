#Given an integer array nums, find the contiguous subarray (containing at least one number) 
#which has the largest sum and return its sum.

"""
max()

 0   1   2  3   4  5  6   7  8  
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

dp
[]

"""
import unittest
def kadane(nums):
    if len(nums) == 0: return 0
    result = nums[0] # For array with all negative integers
    prev_sum, curr_sum = 0, 0
    for idx in range(len(nums)):
        curr_sum = max(prev_sum + nums[idx], nums[idx])
        result = max(result, curr_sum)
        prev_sum = curr_sum

    return result

class TestKadanesAlgorithm(unittest.TestCase):
    def test_null_array(self):
        self.assertEqual(kadane([]), 0)

    def test_all_negative_array(self):
        self.assertEqual(kadane([-5, -3, -12, -5, -3]), -3)

    def test_one_element(self):
        self.assertEqual(kadane([3]), 3)

    def test_mixed_array(self):
        self.assertEqual(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(kadane([-3, 1, 0, -2, 3, 4, -1, 4, -2]), 10)


if __name__ == "__main__": unittest.main()