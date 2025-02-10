import unittest
from collections import defaultdict


# Time: O(26 * n), where n => number of characters in input_string
# Space: O(1)
def longest_repeating_character_replacement(input_string, k):
    count = defaultdict(int)
    lo, res = 0, 0

    for hi in range(len(input_string)):
        count[input_string[hi]] += 1

        # count can have at most 26 characters
        while (hi - lo + 1) - max(count.values()) > k:
            count[input_string[lo]] -= 1
            lo += 1

        res = max(res, hi - lo + 1)

    return res


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_longest_repeating_character_replacement(self):
        self.assertEqual(longest_repeating_character_replacement("", 2), 0)
        self.assertEqual(longest_repeating_character_replacement("AABABBA", 1), 4)
        self.assertEqual(longest_repeating_character_replacement("ABAA", 0), 2)
        self.assertEqual(longest_repeating_character_replacement("AAAA", 2), 4)
        self.assertEqual(longest_repeating_character_replacement("ABCD", 2), 3)
        self.assertEqual(longest_repeating_character_replacement("ABAB", 1), 3)
        self.assertEqual(longest_repeating_character_replacement("AABABBA", 2), 5)
        self.assertEqual(longest_repeating_character_replacement("ABABBA", 2), 5)


if __name__ == "__main__":
    unittest.main()
