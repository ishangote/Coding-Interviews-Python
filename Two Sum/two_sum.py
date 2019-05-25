# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def two_sum(nums, target):
    if not nums or len(nums) == 0: return nums    
    hm = {}

    for idx in range(len(nums)):
        if target - nums[idx] not in hm:
            hm[nums[idx]] = idx
        else:
            return [hm[target - nums[idx]], idx]

    return []

import unittest
class TestTwoSumUnitTest(unittest.TestCase):
    def test_two_sum_null_input(self):
        self.assertEqual(two_sum([], 3), [])
        self.assertEqual(two_sum(None, 3), None)

    def two_sum_no_pair(self):
        self.assertEqual(two_sum([1, 3, 7, 5], 3), [])

    def two_sum_generic(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

if __name__ == "__main__": unittest.main()