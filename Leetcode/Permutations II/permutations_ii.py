"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

def permutations_ii(nums):
    nums = sorted(nums)
    ans = []
    cur = []
    used_idx = [False] * len(nums)
    backtrack(ans, cur, used_idx, nums)
    return ans

def backtrack(ans, cur, used_idx, nums):
    if len(cur) == len(nums):
        ans.append(list(cur))

    else:
        for i in range(len(nums)):
            if used_idx[i] or (i > 0 and nums[i] == nums[i - 1] and not used_idx[i - 1]): continue
            used_idx[i] = True
            cur.append(nums[i])
            backtrack(ans, cur, used_idx, nums)
            used_idx[i] = False
            cur.pop()

import unittest
class TestPermutations(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(permutations_ii([1, 2, 1]), [[1,1,2], [1,2,1], [2,1,1]])

if __name__ == "__main__": unittest.main()