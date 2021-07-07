import unittest
from levenshtein_distance import levenshtein_distance
class TestLevenshteinDistance(unittest.TestCase):
    def setUp(self) -> None:
        self.string1s = ["abc", "", "", "abc", "abc", "abc", "yabcx", "abcdefghij", "cereal", "table"]
        self.string2s = ["yabd", "", "abc", "abc", "abx", "abcx", "abc", "a234567890", "saturday", "bal"]
        self.distance = [2, 0, 3, 0, 1, 1, 2, 9, 6, 3]

    def test_generic(self):
        for idx, ans in enumerate(self.distance):
            self.assertEqual(ans, levenshtein_distance(self.string1s[idx], self.string2s[idx]))

if __name__ == "__main__": unittest.main()