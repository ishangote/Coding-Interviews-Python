import unittest
from collections import Counter


# Time: O(n), where n => number of unique characters (~ length) of the input string
# Space: O(n)
def longest_palindrome(input_string):
    res, odd_found = 0, False

    char_count = Counter(input_string)

    for count in char_count.values():
        if count % 2 == 0:
            res += count
        else:
            odd_found = True
            res += count - 1

    return res if not odd_found else res + 1


# Time: O(n)
# Space: O(n)
def longest_palindrome_set(input_string):
    char_set = set()
    res = 0

    for char in input_string:
        if char not in char_set:
            char_set.add(char)
        else:
            res += 2
            char_set.remove(char)

    return res if not char_set else res + 1


import unittest


class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("aacaabbccdeee"), 11)
        self.assertEqual(longest_palindrome("abccccdd"), 7)

    def test_longest_palindrome_set(self):
        self.assertEqual(longest_palindrome_set("aacaabbccdeee"), 11)
        self.assertEqual(longest_palindrome_set("abccccdd"), 7)


if __name__ == "__main__":
    unittest.main()
