import unittest
from minimum_knight_moves import min_knight_moves_naive

class TestMinimumKnightMoves(unittest.TestCase):
    def test_small(self):
        self.assertEqual(min_knight_moves_naive(2, 1), 1)
        self.assertEqual(min_knight_moves_naive(5, 5), 4)

if __name__ == "__main__": unittest.main()