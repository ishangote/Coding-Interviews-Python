# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

"""
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


        PATTERN
        0  1 2 3 4 5 6
        '' x a * b . c
   0 ''  T F F F F F F
T  1 x   F T F 
E  2 a   F
X  3 a   F
T  4 b   F
   5 y   F
   6 c   F

Pseudo:
if p[j] == t[i] or p[j] == '.':
    memo[i][j] = memo[i - 1][j - 1]
elif p[j] == '*':
    memo[i][j] = memo[i][j - 2]
    if p[j] == t[i] or p[j] == '.':
        memo[i][j] = memo[i - 1][j]

else: memo[i][j] = False
"""

def regex(text, pattern):
    memo = [[False for j in range(len(pattern) + 1)] for i in range(len(text) + 1)]
    memo[0][0] = True

    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == '*':
            memo[0][j] = memo[0][j - 2]

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                memo[i][j] = memo[i - 1][j - 1]
                
            elif pattern[j - 1] == '*':
                memo[i][j] = memo[i][j - 2]
                if pattern[j - 1 - 1] == text[i - 1] or pattern[j - 1 -1] == '.':
                    memo[i][j] = memo[i][j] or memo[i - 1][j]
                    
            else: memo[i][j] = False

    return memo[len(text)][len(pattern)]

import unittest
class TestRegularExpressionMatching(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(regex("mississippi", "mis*is*p*."), False)
        self.assertEqual(regex("aab", "c*a*b"), True)
        self.assertEqual(regex("ab", ".*"), True)
        self.assertEqual(regex("ab", ".*"), True)
        self.assertEqual(regex("aa", "a*"), True)
        self.assertEqual(regex("aa", "a"), False)

if __name__ == "__main__": unittest.main()