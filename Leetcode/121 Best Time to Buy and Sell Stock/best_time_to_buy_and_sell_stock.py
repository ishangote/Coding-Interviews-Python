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


# ------------------------------------------------------------------ #

# * Variation 1: Departures/Returns


# Time: O(n), where n => length of departures/returns
# Space: O(1)
def minimum_ticket_price(departures, returns):
    min_depart_price = sys.maxsize
    min_cost = sys.maxsize

    for depart_price, return_price in zip(departures, returns):
        if depart_price < min_depart_price:
            min_depart_price = depart_price

        cost = min_depart_price + return_price

        if cost < min_cost:
            min_cost = cost

    return min_cost


# ------------------------------------------------------------------ #


class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]), 0)

    def test_best_time_to_buy_and_sell_stock_clean(self):
        self.assertEqual(best_time_to_buy_and_sell_stock_clean([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(best_time_to_buy_and_sell_stock_clean([7, 6, 4, 3, 1]), 0)


class TestMinimumTicketPrice(unittest.TestCase):
    def test_single_day(self):
        departures = [5]
        returns = [7]
        # Only one day: cost is 5 + 7 = 12.
        self.assertEqual(minimum_ticket_price(departures, returns), 12)

    def test_multiple_days(self):
        departures = [3, 2, 4]
        returns = [5, 3, 1]
        # Day 1: cost = 3 + 5 = 8
        # Day 2: update min_depart_price to 2, cost = 2 + 3 = 5
        # Day 3: cost = 2 + 1 = 3 (lowest)
        self.assertEqual(minimum_ticket_price(departures, returns), 3)

    def test_same_departure_prices(self):
        departures = [5, 5, 5]
        returns = [3, 2, 1]
        # All departures are equal; best cost comes from the last day: 5 + 1 = 6.
        self.assertEqual(minimum_ticket_price(departures, returns), 6)

    def test_descending_departures(self):
        departures = [10, 9, 8, 7]
        returns = [1, 2, 3, 4]
        # Minimum departure price gets updated day by day:
        # Day 4: cost = 7 + 4 = 11, which is the lowest.
        self.assertEqual(minimum_ticket_price(departures, returns), 11)

    def test_increasing_departures_and_decreasing_returns(self):
        departures = [1, 2, 3, 4, 5]
        returns = [5, 4, 3, 2, 1]
        # Day 1: cost = 1 + 5 = 6
        # From Day 2 onward, the best departure remains 1, so the best cost is 1 + 1 = 2.
        self.assertEqual(minimum_ticket_price(departures, returns), 2)

    def test_empty_lists(self):
        departures = []
        returns = []
        # With no days, the function never updates the initial values.
        # Depending on your use case, you might want to handle this separately.
        self.assertEqual(minimum_ticket_price(departures, returns), sys.maxsize)


if __name__ == "__main__":
    unittest.main()
