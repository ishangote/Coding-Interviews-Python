import unittest
from collections import Counter


# Time: O(n)
# Space: O(n)
def palindrome_permutation(input_string):
    char_count = Counter(input_string)
    char_count = {char: count % 2 for char, count in char_count.items()}
    return sum(char_count.values()) <= 1


class TestPalindromePermutation(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertEqual(palindrome_permutation("code"), False)
        self.assertEqual(palindrome_permutation("aab"), True)
        self.assertEqual(palindrome_permutation("carecar"), True)
        self.assertEqual(palindrome_permutation("aaa"), True)


if __name__ == "__main__":
    unittest.main()
