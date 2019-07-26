# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
"""
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []]
"""
import copy
def subsets(nums):
    if not nums: return []
    nums.sort()
    result, subset = [], []
    backtrack(result, subset, nums, 0)
    return result
    
def backtrack(result, subset, nums, start):
    result.append(copy.deepcopy(subset))
    for idx in range(start, len(nums)):
        subset.append(nums[idx])
        backtrack(result, subset, nums, idx + 1)
        subset.pop(len(subset) - 1)

import unittest
class TestSubset(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(sorted(subsets([1, 2, 3])), sorted([[], [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2]]))

if __name__ == "__main__": unittest.main()