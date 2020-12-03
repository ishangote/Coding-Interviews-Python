import unittest
from buy_sell_stock import buy_sell_stock_naive, buy_sell_stock

class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(buy_sell_stock_naive([7,1,5,3,6,4]), 5)
        self.assertEqual(buy_sell_stock_naive([7,6,4,3,1]), 0)

        self.assertEqual(buy_sell_stock([7,1,5,3,6,4]), 5)
        self.assertEqual(buy_sell_stock([7,6,4,3,1]), 0)

if __name__ == "__main__": unittest.main()