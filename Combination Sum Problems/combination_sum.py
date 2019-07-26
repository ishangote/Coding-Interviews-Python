# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sums to target.
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

 
[2, 3, 6, 7]
       ^
                [], 7
                /
              [2], 5
             /      \
            /        \
          [2, 2], 3   [2, 3], 2
             /      \   \
            /        \  [2, 3, 3], -1
      [2, 2, 2], 1   [2, 2, 3], 0





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
      combination.append(nums[idx])
      backtrack(result, combination, nums, remain - nums[idx], idx) #not i + 1 because we can reuse same elements
      combination.pop(len(combination) - 1)

import unittest
class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(combination_sum([2,3,5], 8), [[2,2,2,2], [2,3,3], [3,5]])

if __name__ == "__main__": unittest.main()
