import unittest
from binary_search_iterative import binary_search_iterative
from binary_search_recursive import binary_search_recursive

class TestBinarySearch(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(binary_search_iterative([-4, 1, 2, 3], -4), 0)
        self.assertEqual(binary_search_recursive([-4, 1, 2, 3], -4), 0)

        self.assertEqual(binary_search_iterative([-4, 1, 2, 3], 4), -1)
        self.assertEqual(binary_search_recursive([-4, 1, 2, 3], 4), -1)

if __name__ == "__main__": unittest.main()