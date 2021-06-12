import unittest
from fnr import first_non_repeating
class TestFirstNonRepeatingCharacters(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(1, first_non_repeating("abcdcaf"))
        self.assertEqual(6, first_non_repeating("faadabcbbebdf"))
        self.assertEqual(0, first_non_repeating("a"))
        self.assertEqual(0, first_non_repeating("ab"))
        self.assertEqual(1, first_non_repeating("abac"))
        self.assertEqual(5, first_non_repeating("ababac"))
        self.assertEqual(25, first_non_repeating("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.assertEqual(-1, first_non_repeating(""))
        self.assertEqual(-1, first_non_repeating("aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccdddddddddddeeeeeeeeffghgh"))
        self.assertEqual(-1, first_non_repeating("aabbccddeeff"))

if __name__ == "__main__": unittest.main()