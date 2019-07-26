# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

"""
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

def combination_sum_ii(nums, target):
  result = []
  nums.sort()
  backtrack(result, [], nums, target, 0)
  return result

import copy
def backtrack(result, combination, nums, remain, start):
  if remain < 0: return
  elif remain == 0: result.append(copy.deepcopy(combination))
  else:
    for idx in range(start, len(nums)):
      if idx > start and nums[idx] == nums[idx - 1]: continue #to skip duplicates
      combination.append(nums[idx])
      backtrack(result, combination, nums, remain - nums[idx], idx + 1)
      combination.pop(len(combination) - 1)

import unittest
class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        self.assertEqual(sorted(combination_sum_ii([10,1,2,7,6,1,5], 8)), sorted([[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]))
        self.assertEqual(sorted(combination_sum_ii([2,5,2,1,2], 5)), sorted([[1,2,2], [5]]))

if __name__ == "__main__": unittest.main()