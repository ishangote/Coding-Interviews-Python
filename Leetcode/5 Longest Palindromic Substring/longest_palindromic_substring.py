import unittest


def expand_helper(left, right, input_string):
    while (
        left >= 0
        and right < len(input_string)
        and input_string[left] == input_string[right]
    ):
        left -= 1
        right += 1

    return left + 1, right - 1  # Adjust bounds to actual palindrome


# Time: O(n^2), where n => length of input string
# Space: O(1)
def longest_palindromic_substring_expand(input_string):
    res = [0, 0]

    for idx in range(len(input_string)):
        left_odd, right_odd = expand_helper(idx, idx, input_string)
        left_even, right_even = expand_helper(idx, idx + 1, input_string)

        if res[1] - res[0] < right_odd - left_odd:
            res = [left_odd, right_odd]

        if res[1] - res[0] < right_even - left_even:
            res = [left_even, right_even]

    return input_string[res[0] : res[1] + 1]


class TestLongestPalindromicSubString(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring_expand(""), "")
        self.assertEqual(longest_palindromic_substring_expand("a"), "a")
        self.assertEqual(longest_palindromic_substring_expand("babad"), "bab")
        self.assertEqual(longest_palindromic_substring_expand("banana"), "anana")
        self.assertEqual(longest_palindromic_substring_expand("cbbd"), "bb")
        self.assertEqual(longest_palindromic_substring_expand("bb"), "bb")


if __name__ == "__main__":
    unittest.main()
