import unittest


def recursive_helper(lo, hi, k, memo, input_string):
    if (lo, hi, k) in memo:
        return memo[(lo, hi, k)]

    if lo >= hi:
        memo[(lo, hi, k)] = True

    elif input_string[lo] == input_string[hi]:
        memo[(lo, hi, k)] = recursive_helper(lo + 1, hi - 1, k, memo, input_string)

    elif k == 0:
        memo[(lo, hi, k)] = False

    else:
        memo[(lo, hi, k)] = recursive_helper(
            lo + 1, hi, k - 1, memo, input_string
        ) or recursive_helper(lo, hi - 1, k - 1, memo, input_string)

    return memo[(lo, hi, k)]


"""
- There are O(n²) possible (lo, hi) pairs because lo and hi range from 0 to n-1, leading to n * n = O(n²) pairs.
- For each (lo, hi) pair, k can vary from 0 to k, leading to an additional factor of O(k).
"""


# Time: O(n^2 * k), where n => length of input string
# Space: O(n^2 * k)
def valid_palindrome_iii(input_string, k):
    memo = {}
    return recursive_helper(0, len(input_string) - 1, k, memo, input_string)


class TestValidPalindromeIII(unittest.TestCase):
    def test_basic_cases(self):
        self.assertTrue(
            valid_palindrome_iii("abcde", 2)
        )  # Remove 'b' and 'd' → "ace" (palindrome)
        self.assertTrue(
            valid_palindrome_iii("abca", 1)
        )  # Remove 'b' → "aca" (palindrome)
        self.assertFalse(
            valid_palindrome_iii("abcdef", 2)
        )  # Needs 3 removals, so not valid

    def test_already_palindrome(self):
        self.assertTrue(valid_palindrome_iii("racecar", 0))  # Already a palindrome
        self.assertTrue(valid_palindrome_iii("aa", 0))  # Already a palindrome

    def test_edge_cases(self):
        self.assertTrue(valid_palindrome_iii("", 0))  # Empty string is a palindrome
        self.assertTrue(
            valid_palindrome_iii("a", 0)
        )  # Single character is always a palindrome
        self.assertTrue(valid_palindrome_iii("ab", 1))  # Remove 'b' → "a" (palindrome)
        self.assertFalse(valid_palindrome_iii("abcd", 1))  # Need at least 2 removals

    def test_large_cases(self):
        self.assertTrue(
            valid_palindrome_iii("abcdeedcba", 1)
        )  # Remove 'd' → "abcceedcba" (palindrome)
        self.assertFalse(
            valid_palindrome_iii("abcdefgh", 3)
        )  # Needs at least 4 removals


if __name__ == "__main__":
    unittest.main()
