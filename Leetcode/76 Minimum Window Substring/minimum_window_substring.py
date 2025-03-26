import unittest
import sys
from collections import Counter, defaultdict


# Time: O(n), where n => length of input_string, k => unique characters in required_characters
# Space: O(k)
def minimum_window_substring(input_string, required_characters):
    lo, hi = -1, -1
    min_length = sys.maxsize
    start = 0

    required_characters_freq = Counter(required_characters)
    window_freq = defaultdict(int)
    have, need = 0, len(required_characters_freq)

    for end in range(len(input_string)):
        if input_string[end] in required_characters_freq:
            window_freq[input_string[end]] += 1
            if (
                window_freq[input_string[end]]
                == required_characters_freq[input_string[end]]
            ):
                have += 1

        while start <= end and have == need:
            if end - start + 1 < min_length:
                lo, hi = start, end
                min_length = end - start + 1

            if input_string[start] in required_characters_freq:
                window_freq[input_string[start]] -= 1
                if (
                    window_freq[input_string[start]]
                    < required_characters_freq[input_string[start]]
                ):
                    have -= 1

            start += 1

    return "" if lo == -1 else input_string[lo : hi + 1]


class TestMinWindowSubstring(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(minimum_window_substring("abcde", "klm"), "")
        self.assertEqual(minimum_window_substring("abcde", "abcde"), "abcde")

    def test_generic(self):
        self.assertEqual(minimum_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minimum_window_substring("ADOBECODEBAANC", "AABC"), "BAANC")
        self.assertEqual(minimum_window_substring("ABA", "ABA"), "ABA")
        self.assertEqual(minimum_window_substring("azjskfzts", "sz"), "zjs")


if __name__ == "__main__":
    unittest.main()
