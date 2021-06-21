import unittest
from monotonic_array import isMonotonic
class TestMonotonicArray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(True, isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
        self.assertEqual(True, isMonotonic([]))
        self.assertEqual(True, isMonotonic([1, 5, 10, 1100, 1101, 1102, 9001]))
        self.assertEqual(False, isMonotonic([1, 2, 0]))
        self.assertEqual(False, isMonotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]))

if __name__ == "__main__": unittest.main()