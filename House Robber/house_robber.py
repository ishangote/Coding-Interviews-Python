# Maximum Sum Subsequence Non-Adjacent
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
# adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""
Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Approach: DP

 0 1 2 3 4
[2,7,9,3,1]

incl = 0
excl = 0
[2,7,9,3,1]

incl = 2
excl = 0

[2,7,9,3,1]
 ^
 
incl = 7
excl = 2

[2,7,9,3,1]
   ^

incl = 11
excl = 7

[2,7,9,3,1]
     ^

incl = 11
excl = 11

[2,7,9,3,1]
       ^
       
incl = 12
excl = 11

[2,7,9,3,1]
         ^
return max(incl, exlc)
"""

def house_robber(arr):
    if not arr or len(arr) == 0: return 0
    
    incl, excl = 0, 0
    
    for num in arr:
        temp_incl = incl
        incl = max(incl, excl + num)
        excl = temp_incl

    return max(incl, excl)

import unittest
class MaximumSumSubsequenceNonAdjacent(unittest.TestCase):
    def test_none_arr(self):
        self.assertEqual(house_robber([]), 0)
        self.assertEqual(house_robber(None), 0)

    def test_all_0_arr(self):
        self.assertEqual(house_robber([0, 0, 0, 0, 0]), 0)
    
    def test_len1_arr(self):
        self.assertEqual(house_robber([2]), 2)

    def test_len2_arr(self):
        self.assertEqual(house_robber([3, 6]), 6)

    def test_house_robber(self):
        self.assertEqual(house_robber([2,7,9,3,1]), 12)
        self.assertEqual(house_robber([1,2,3,1]), 4)

if __name__ == "__main__": unittest.main()