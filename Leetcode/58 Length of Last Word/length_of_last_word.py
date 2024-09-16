"""
Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

## Brute Force
* Remove extra whitespaces
* Split string on whitespaces
* return length of last word

## Optimization
* Iterate backwards to find a character that is not a whitespace
* Once a character is found, traverse the substring and return

Example 1:
s = 
'Hello World   '
           ^
       *

"""

# Time: O(n), where n => length of input_string
# Space: O(n)
def length_of_last_word_brute_force(input_string):
    # * .split() operator splits on all whitespaces
    return len(input_string.split()[-1])


# Time: O(n), where n => length of input_string
# Space: O(1)
def length_of_last_word(input_string):
    end = len(input_string) - 1
    while end >= 0 and input_string[end] == " ": end -= 1

    start = end
    while start >= 0 and input_string[start] != " ": start -= 1

    return end - start


import unittest
class TestLengthOfLastWord(unittest.TestCase):
    def test_length_of_last_word_brute_force(self):
        self.assertEqual(length_of_last_word_brute_force("Hello World"), 5)
        self.assertEqual(length_of_last_word_brute_force("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word_brute_force("luffy is still joyboy"), 6)

    def test_edge_case(self):
        self.assertEqual(length_of_last_word(""), 0)
        self.assertEqual(length_of_last_word("    "), 0)

    def test_length_of_last_word(self):
        self.assertEqual(length_of_last_word("Hello World"), 5)
        self.assertEqual(length_of_last_word("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word("luffy is still joyboy"), 6)

if __name__ == "__main__": unittest.main()
