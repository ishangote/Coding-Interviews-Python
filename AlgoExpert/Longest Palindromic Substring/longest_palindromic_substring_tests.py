import unittest
from longest_palindromic_substring import longest_plaindrome

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.input = ["abaxyzzyxf", "it's highnoon", "z234a5abbba54a32z"]
        self.palin = ["xyzzyx", "noon", "5abbba5"]
    
    def test_generic(self):
        for idx, string in enumerate(self.input):
            self.assertEqual(self.palin[idx], longest_plaindrome(string))

if __name__ == "__main__": unittest.main()