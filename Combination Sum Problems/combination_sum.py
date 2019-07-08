# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
"""
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
def combination_sum(nums, target):
    if target < 0 or not nums: return [[]]
    
    def backtrack(target, path, start):
        if target == 0:
            result.append(path)
            return
        for idx in range(start, len(nums)):
            if target < nums[idx]: return
            backtrack(target - nums[idx], path + [nums[idx]], idx)

    nums.sort()
    result = []
    backtrack(target, [], 0)
    return result

import unittest
class TestCombinationSum(unittest.TestCase):
    def test_combination_sum_invalid_input(self):
        self.assertEqual(combination_sum([], 3), [[]])
        self.assertEqual(combination_sum([2, 3, 6, 7], -3), [[]])

    def test_combination_sum(self):
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(combination_sum([2,3,5], 8), [[2,2,2,2], [2,3,3], [3,5]])

if __name__ == "__main__": unittest.main()
