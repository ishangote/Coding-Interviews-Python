"""
input: "abc"
output: "abc"

input: "a"
output: "a"

input: "abbadaadel"
output: "el"

input: "abba"
output: ""

* => start of palindorme prefix

0 1 2 3 4 5 6 7 8 9 
a b b a d a a d e l
        *
      j

"""

def prefix_palindrome_cutting(input_string):
    start = 0
    for j in range(len(input_string)):
        tmp = input_string[start : j + 1]
        if len(tmp) > 1 and tmp == tmp[::-1]:
            start = j + 1

    return input_string[start:]

import unittest
class TestPrefixPalindromeCutting(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(prefix_palindrome_cutting("abc"), "abc")
        self.assertEqual(prefix_palindrome_cutting("a"), "a")
        self.assertEqual(prefix_palindrome_cutting("abbadaadel"), "el")
        self.assertEqual(prefix_palindrome_cutting("abba"), "")

if __name__ == "__main__": unittest.main()