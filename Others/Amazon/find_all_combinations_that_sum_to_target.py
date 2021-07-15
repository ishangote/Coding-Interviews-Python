"""
Given a positive integer, target, print all possible combinations of positive integers that
sum up to target

Questions:
1. Can one integer be used multiple times? yes

Examples:
target = 5
nums = 
{1, 2, 3, 4}
                            0 {1, 2, 3, 4}
                1
            2 [1, 1]
        3         4[1, 1, 2], c = 4
    4      5 
5 
(== target) [1, 1, 1, 1, 1]

res = [[1, 1, 1, 1, 1], [1, 1, 1, 2]]
"""
def backtrack(target, cur_sum, start, cur_combination, res):
    if cur_sum == target:
        res.append(list(cur_combination))
    
    else:
        for i in range(start, target):
            if cur_combination and i < cur_combination[-1]: continue
            tmp_sum = cur_sum + i
            if tmp_sum <= target:
                cur_combination.append(i)
                backtrack(target, tmp_sum, start, cur_combination, res)
                cur_combination.pop()
    
    return

def combinations(target):
    res = []
    backtrack(target, 0, 1, [], res)
    return res

import unittest
class TestFindAllCombinationsThatSumToTarget(unittest.TestCase):
    def test_generic(self):
        self.assertCountEqual([[1, 1, 1, 1, 1],[1, 1, 1, 2],[1, 2, 2],[1, 1, 3],[1, 4], [2, 3]], combinations(5))
if __name__ == "__main__": unittest.main()