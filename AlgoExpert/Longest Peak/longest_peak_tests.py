import unittest
from longest_peak import longest_peak

class TestLongestPeak(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(6, longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
        self.assertEqual(0, longest_peak([]))
        self.assertEqual(3, longest_peak([1, 3, 2]))
        self.assertEqual(6, longest_peak([1, 2, 3, 4, 5, 1]))
        self.assertEqual(3, longest_peak([5, 4, 3, 2, 1, 2, 1]))
        self.assertEqual(5, longest_peak([5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]))
        self.assertEqual(0, longest_peak([5, 4, 3, 2, 1, 2, 10, 12]))
        self.assertEqual(0, longest_peak([1, 2, 3, 3, 2, 1]))
        self.assertEqual(9, longest_peak([1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]))

if __name__ == "__main__": unittest.main()