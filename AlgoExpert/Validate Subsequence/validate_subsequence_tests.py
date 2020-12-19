import unittest
from validate_subsequence import isValidSubsequence
class TestValidateSubsequence(unittest.TestCase):
    def test_validate_subsequence(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True)
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10]), True)

if __name__ == "__main__": unittest.main()