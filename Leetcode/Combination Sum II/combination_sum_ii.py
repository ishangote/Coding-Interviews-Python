"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
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

def combination_sum_ii(candidates, target):
    candidates.sort()
    ans = []
    backtrack(candidates, ans, [], target, 0)
    return ans

def backtrack(candidates, ans, cur, remain, start):
    if remain < 0: return
    if remain == 0:
        ans.append(list(cur))
    else:
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: continue
            cur.append(candidates[i])
            backtrack(candidates, ans, cur, remain - candidates[i], i + 1)
            cur.pop()

import unittest
class TestCombinationSumII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(sorted(combination_sum_ii([10,1,2,7,6,1,5], 8)), sorted([[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]))
        self.assertEqual(sorted(combination_sum_ii([2,5,2,1,2], 5)), sorted([[1,2,2], [5]]))

if __name__ == "__main__": unittest.main()