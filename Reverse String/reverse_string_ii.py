# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
# If there are less than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and 
# leave the other as original.
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]
"""
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

abcdefg
^
bacdefg
   ^
bacdfeg
      ^
"""

def reverse_string_ii(s, k):
    s = list(s)
    for i in range(0, len(s), 2 * k):
        s[i: i + k] = reversed(s[i: i + k])
    return ''.join(s)