import unittest
from smallest_subsequence_of_distinct_characters import remove_duplicate_letters

class TestSmallestSubsequenceOfDistinctCharacters(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(remove_duplicate_letters("bcabc"), "abc")
        self.assertEqual(remove_duplicate_letters("cbacdcbc"), "acdb")

if __name__ == "__main__": unittest.main()