# Given an input string, reverse the string word by word.
"""
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"the sky  is blue!"
   ^
.split()
["the", "sky", "is", "blue"]

return " ".join()

"""

def reverse_words(input):
    if not input or len(input) == 0 or len(input) == 1: return ''.join(input.split())

    input = input.split()

    start, end = 0, len(input) - 1
    while start < end:
        input[start], input[end] = input[end], input[start]
        start += 1
        end -= 1

    return " ".join(word for word in input)

import unittest
class TestReverseWords(unittest.TestCase):
    def test_len01_string(self):
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words(" "), "")
        self.assertEqual(reverse_words("a"), "a")

    def test_reverse_words_multiple_spaces(self):
        self.assertEqual(reverse_words("the sky   is blue"), "blue is sky the")
        self.assertEqual(reverse_words("             the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words("the sky is blue          "), "blue is sky the")

    def test_reverse_words_punctuation(self):
        self.assertEqual(reverse_words("the sky, is blue"), "blue is sky, the")
        self.assertEqual(reverse_words("the sky is blue!"), "blue! is sky the")

    
if __name__ == "__main__": unittest.main()