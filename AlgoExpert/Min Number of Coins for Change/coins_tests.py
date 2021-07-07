import unittest
from coins import min_coins

class TestMinNumberOfCoins(unittest.TestCase):
    def setUp(self) -> None:
        self.denoms = [[1, 5, 10], [1, 2, 3], [2, 1], [1, 5, 10], [1, 5, 10], [39, 45, 130, 40, 4, 1]]
        self.target = [7, 0, 3, 4, 11, 135]
        self.coins = [3, 0, 2, 4, 2, 3]
    
    def test_generic(self):
        for idx in range(len(self.denoms)):
            self.assertEqual(self.coins[idx], min_coins(self.target[idx], self.denoms[idx]))

if __name__ == "__main__": unittest.main()