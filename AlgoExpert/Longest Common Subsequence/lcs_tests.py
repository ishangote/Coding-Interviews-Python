import unittest
from lcs import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.string1s = ["ZXVVYZW", "", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFG"]
        self.string2s = ["XKYKZPW", "", "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV", "APPLES"]
        self.subsequences = [["X", "Y", "Z", "W"], [], ["C", "D", "E", "G", "H", "J", "K", "L", "T", "U", "V"], ["A", "E"]]
        return super().setUp()

    def test_generic(self):
        for idx in range(len(self.string1s)):
            self.assertEqual(self.subsequences[idx], longest_common_subsequence(self.string1s[idx], self.string2s[idx]))

if __name__ == "__main__": unittest.main()