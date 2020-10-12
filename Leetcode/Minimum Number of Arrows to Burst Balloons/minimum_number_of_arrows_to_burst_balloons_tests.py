import unittest
from minimum_number_of_arrows_to_burst_balloons import min_arrows

class TestMinimumArrows(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(min_arrows([]), 0)

    def test_generic(self):
        self.assertEqual(min_arrows([[10,16],[2,8],[1,6],[7,12]]), 2)
        self.assertEqual(min_arrows([[1,2],[3,4],[5,6],[7,8]]), 4)
        self.assertEqual(min_arrows([[1,2],[2,3],[3,4],[4,5]]), 2)
        self.assertEqual(min_arrows([[1,2]]), 1)
        self.assertEqual(min_arrows([[2,3],[2,3]]), 1)

if __name__ == "__main__": unittest.main()