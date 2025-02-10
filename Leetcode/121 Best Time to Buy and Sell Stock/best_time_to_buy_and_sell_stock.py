import unittest
import sys


# Time: O(n), where n => length of prices
# Space: O(1)
def best_time_to_buy_and_sell_stock(prices):
    if not prices:
        return 0

    res, left, right = 0, 0, 1

    while right < len(prices):
        profit = prices[right] - prices[left]
        res = max(res, profit)

        if profit <= 0:
            left = right

        right += 1

    return res


# Time: O(n)
# Space: O(1)
def best_time_to_buy_and_sell_stock_clean(prices):
    min_price = sys.maxsize
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]), 0)

    def test_best_time_to_buy_and_sell_stock_clean(self):
        self.assertEqual(best_time_to_buy_and_sell_stock_clean([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(best_time_to_buy_and_sell_stock_clean([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
