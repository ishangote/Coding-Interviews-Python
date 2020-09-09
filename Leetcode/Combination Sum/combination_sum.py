"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

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

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""
def combination_sum(candidates, target):
    candidates.sort()
    ans = []
    cur = []
    backtrack(candidates, ans, cur, target, 0)
    return ans

def backtrack(candidates, ans, cur, remain, start):
    if remain < 0: return
    if remain == 0:
        ans.append(list(cur))
    else:
        for i in range(start, len(candidates)):
            cur.append(candidates[i])
            backtrack(candidates, ans, cur, remain - candidates[i], i)
            cur.pop()

import unittest
class TestCombinationSum(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(combination_sum([2,3,5], 8), [[2,2,2,2], [2,3,3], [3,5]])

if __name__ == "__main__": unittest.main()