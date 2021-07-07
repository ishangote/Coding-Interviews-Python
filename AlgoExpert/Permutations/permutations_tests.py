import unittest
from permutations import permutations

class TestPermutations(unittest.TestCase):
    def test_generic(self):
        self.assertEqual([[1, 2, 3],[1, 3, 2],[2, 1, 3],[2, 3, 1],[3, 1, 2],[3, 2, 1]], permutations([1, 2, 3]))

if __name__ == "__main__": unittest.main()