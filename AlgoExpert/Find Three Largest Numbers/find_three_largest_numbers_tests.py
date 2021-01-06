import unittest
from find_three_largest_numbers import findThreeLargestNumbers

class TestFindThreeLargestNumbers(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(findThreeLargestNumbers([55, 43, 11, 3, -3, 10]), [11, 43, 55])

if __name__ == "__main__":
    unittest.main()