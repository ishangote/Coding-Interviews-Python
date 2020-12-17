import unittest
from string_minimization import string_minimization

class TestStringMinimization(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(string_minimization("aabcccabba"), 4)
        self.assertEqual(string_minimization("abba"), 0)
        self.assertEqual(string_minimization("abcba"), 1)

if __name__ == "__main__": unittest.main()