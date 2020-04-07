"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import sys
def buy_sell_stock(stocks):
    max_profit = 0
    min_cost = sys.maxsize

    for cost in stocks:
        if cost < min_cost: min_cost = cost
        elif cost - min_cost > max_profit: max_profit = cost - min_cost

    return max_profit

import unittest
class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(buy_sell_stock([7,1,5,3,6,4]), 5)
        self.assertEqual(buy_sell_stock([7,6,4,3,1]), 0)

if __name__ == "__main__": unittest.main()