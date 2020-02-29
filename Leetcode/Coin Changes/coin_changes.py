# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

"""
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

spend coins in this order ->
                1   2   5

                    11
        10          9               6
9   8   5       8   7   4       5   4   1

At each depth -> one coin spent

[1,2,5]
value:      0 1 2 3 4 5 6 7 8 9 10 11
num coins: [0 1 1 2...]

memo = [0] + [int('inf')] * amount
memo[i] = min(memo[i], 1 + memo[i - c])

"""
def coin_changes(coins, amount):
    memo = [0] + [float('inf')] * amount
    for i, v in enumerate(memo):
        for c in coins:
            if i >= c: memo[i] = min(memo[i], 1 + memo[i - c])
    return -1 if memo[-1] == float('inf') else memo[-1]

import unittest
class TestCoinChanges(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(coin_changes([], 12), -1)
        self.assertEqual(coin_changes([1, 2], 0), 0)
    
    def test_generic(self):
        self.assertEqual(coin_changes([1, 2, 5], 11), 3)

if __name__ == "__main__": unittest.main()