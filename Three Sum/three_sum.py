# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

import unittest
def three_sum(nums):
    nums = sorted(nums)
    solutions = []
    for idx in range(0, len(nums) - 3):
        if nums[idx] > 0: break
        if idx > 0 and nums[idx] == nums[idx - 1]: continue
        left, right = idx + 1, len(nums) - 1

        while left < right:
            sum = nums[idx] + nums[left] + nums[right]
            if sum == 0:
                solutions.append([nums[idx], nums[left], nums[right]])

                left_value = nums[left]
                while left < len(nums) and nums[left] == left_value: left += 1

                right_value = nums[right]
                while right > left and nums[right] == right_value: right -= 1

            elif sum < 0: left += 1
            else: right -= 1

    return solutions

class TestThreeSum(unittest.TestCase):
    def test_generic_example(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([0, -1, 2, -3, 1]), [[-3, 1, 2], [-1, 0, 1]])

    def test_all_zero_input(self):
        self.assertEqual(three_sum([0, 0, 0, 0, 0]), [[0, 0, 0]])

    def test_only_two_values_input(self):
        self.assertEqual(three_sum([-1 , 1]), [])

    def test_no_three_pairs_input(self):
        self.assertEqual(three_sum([2, 3, 4, 5, 6, 7]), [])

if __name__ == "__main__": unittest.main()