# 0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
# from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
# weight.

"""
weights = [1, 3, 4, 5]
values = [1,  4, 5, 7]

                
idx    ->       0 1 2 3 4 5 6 7 
                <-max_bag_weight->
idx     val  wt 0 1 2 3 4 5 6 7
0       (1)  1  0 1 1 1 1 1 1 1
1       (4)  3  0 1 1 4 5 5 5 5
2       (5)  4  0 1 1 4 5 6 6 9
3       (7)  5  0 1 1 4 5 7 8 9

T[1][3] = max(4 + 0, 1)
T[1][4] = max(4 + 1, 1)

"""

def knapsack_01(weights, values, max_bag_weight):
    if not len(weights) == len(values) or len(weights) == 0: return False    #Invalid input
    
    rows = len(weights) + 1
    cols = max_bag_weight + 1

    memo = [[0 for itr1 in range(cols)] for itr2 in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if j < weights[i - 1]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], values[i - 1] + memo[i - 1][j - weights[i - 1]])
    return memo[rows - 1][cols - 1]

import unittest
class Test01Knapsack(unittest.TestCase):
    def test_invlaid_input(self):
        self.assertEqual(knapsack_01([1, 2, 4, 5], [3, 1, 3], 7), False)

    def test_knapsack_generic(self):
        self.assertEqual(knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)

if __name__ == "__main__": unittest.main()