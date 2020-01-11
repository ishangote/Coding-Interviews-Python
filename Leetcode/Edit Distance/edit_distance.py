"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


    ""   a   b   c   d   e   f
""  0    1   2   3   4   5   6
a   1    0   1   2   3   4   5
z   2    1   1   2   3   4   5
c   3    2   2   1   2   3   4
e   4    3   3   2   2   2   3
d   5    4   4   3   2   3   3

if str1[i] == str2[j]: dp[i][j] = dp[i-1][j-1]
else: dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
"""

def edit_distance(str1, str2):
    memo = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(memo)):
        memo[i][0] = i
    
    for i in range(len(memo[0])):
        memo[0][i] = i

    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            memo[i][j] = 1 + min(memo[i - 1][j - 1], memo[i][j - 1], memo[i - 1][j]) if str1[i - 1] != str2[j - 1] else memo[i - 1][j - 1]

    return memo[len(str1)][len(str2)]

import unittest
class TestEditDistance(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(edit_distance("azced", "abcdef"), 3)
        self.assertEqual(edit_distance("horse", "ros"), 3)
    
if __name__ == "__main__": unittest.main()