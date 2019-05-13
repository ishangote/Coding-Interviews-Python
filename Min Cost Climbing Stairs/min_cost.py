#On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
#and you can either start from the step with index 0, or the step with index 1.

"""
        0    1  2
cost = [10, 15, 20]


min_cost[i] =  ost[i] + min(min_cost[i - 1], min_cost[i - 2])

fill dp -> stores all min_cost for each stair i

dp
[10, 15, 30]

n = 3 -> 3rd floor target

min_cost[3] = min(dp[n-1], dp[n-2]) = 15

so we need only two variables dp[n-1] and dp[n-2] -> reduce space complexity ->

dp1, dp2

dp_i -> ith stair value -> cost[i] + min(dp1, dp2)

cost-> [10, 15, 20]

i   dp_i    dp2    dp1
0   10      0      10
1   15      10     15
2   30      15     30


"""

import unittest
def min_cost(cost):
    dp1, dp2 = 0, 0
    for i in range(len(cost)):
        dp_i = cost[i] + min(dp1, dp2)
        dp2 = dp1
        dp1 = dp_i
        
    return min(dp1, dp2)

class TestMinCostToClimStairs(unittest.TestCase):
    def test_one_step(self):
        self.assertEqual(min_cost([10]), 0)

    def test_two_step(self):
        self.assertEqual(min_cost([10, 15]), 10)

    def test_min_cost(self):
        self.assertEqual(min_cost([10, 15, 20]), 15)
        self.assertEqual(min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

if __name__ == "__main__": unittest.main()