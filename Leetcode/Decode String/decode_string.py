# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].
"""
Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


01234567
3[a2[c]]
       ^
i       curr_num            curr_str        stack
0       3                   ""              []                  
1       0                   ""              [3, ""]
2       0                   "a"             [3, ""]
3       2                   "a"             [3, ""]
4       0                   ""              [3, "", 2, "a"]
5       0                   "c"             [3, "", 2, "a"]
6       0                   "acc"           [3, ""]
7       0                   "accaccacc"     []
"""

def decode_string(s):
    if not s: return s

    stack = []
    curr_str, curr_num = "", 0

    for ch in s:
        if ch == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ''
            curr_num = 0

        elif ch == ']':
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str

        elif ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        
        else:
            curr_str += ch

    return curr_str

import unittest
class TestDecodeStrings(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        
if __name__ == "__main__": unittest.main()