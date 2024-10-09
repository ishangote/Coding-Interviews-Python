import unittest


def is_palindrome(input_string, lo, hi):
    while lo <= hi:
        if input_string[lo] != input_string[hi]:
            return False

        lo += 1
        hi -= 1

    return True


# Time: O(2n) ~ O(n), where n => length of input string
# Space: O(1)
def valid_palindrome_ii(input_string):
    lo, hi = 0, len(input_string) - 1

    while lo <= hi:
        if input_string[lo] == input_string[hi]:
            lo += 1
            hi -= 1

        else:
            return is_palindrome(input_string, lo + 1, hi) or is_palindrome(
                input_string, lo, hi - 1
            )

    return True


class TestValidPalindromeII(unittest.TestCase):
    def test_valid_palindrome_ii(self):
        self.assertTrue(valid_palindrome_ii("a"))
        self.assertTrue(valid_palindrome_ii("ab"))
        self.assertTrue(valid_palindrome_ii("aba"))
        self.assertTrue(valid_palindrome_ii("abdda"))

        self.assertFalse(valid_palindrome_ii("abc"))


if __name__ == "__main__":
    unittest.main()
