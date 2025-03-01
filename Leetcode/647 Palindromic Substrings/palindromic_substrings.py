import unittest


def expand_helper(left, right, input_string):
    substrings = 0

    while (
        left >= 0
        and right < len(input_string)
        and input_string[left] == input_string[right]
    ):
        substrings += 1
        left -= 1
        right += 1

    return substrings


# Time: O(n^2), where n => length of input string
# Space: O(n)
def palindromic_substrings(input_string):
    res = 0

    for idx in range(len(input_string)):
        res += expand_helper(idx, idx, input_string) + expand_helper(
            idx, idx + 1, input_string
        )

    return res


class TestPalindromicSubstring(unittest.TestCase):
    def test_palindromic_substring(self):
        self.assertEqual(palindromic_substrings(""), 0)
        self.assertEqual(palindromic_substrings("abc"), 3)
        self.assertEqual(palindromic_substrings("aaa"), 6)


if __name__ == "__main__":
    unittest.main()
