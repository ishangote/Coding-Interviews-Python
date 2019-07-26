# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
"""
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
from copy import deepcopy
def subset_ii(nums):
    result = []
    nums.sort()
    backtrack(result, [], nums, 0)
    return result

def backtrack(result, subset, nums, start):
    result.append(deepcopy(subset))
    for idx in range(start, len(nums)):
        if idx > start and nums[idx] == nums[idx - 1]: continue
        subset.append(nums[idx])
        backtrack(result, subset, nums, idx + 1)
        subset.pop()

import unittest
class TestSubset(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(sorted(subset_ii([1,2,2])), sorted([[2], [1], [1,2,2], [2,2], [1,2], []]))

if __name__ == "__main__": unittest.main()