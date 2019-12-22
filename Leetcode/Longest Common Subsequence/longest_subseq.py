#Longest Subsequnece => Non-contiguous
"""
Dynamic Prog =>

s1: AGGTAB
s2: GXTXAYB
return 4 => GTAB, GTAB


    AGGT   A    B (1)
       ^
    GXTXA  Y  B (1)
        ^

    0 1 2 3 4 5
s1: G X T X A Y B
s2: A G G T A B
    ^

     s2 0   1  2  3  4  5  6
s1      ""  A  G  G  T  A  B
0   ""   0  0  0  0  0  0  0
1   G    0  0  1  1  1  1  1
2   X    0  0  1  1  1  1  1
3   T    0  0  1  1  2  2  2
4   X    0  0  1  1  2  2  2
5   A    0  1  1  1  2  3  3
6   Y    0  1  1  1  2  3  3
7   B    0  1  1  1  2  3  4

"""

def lcs(s1, s2):

    if len(s1) == 0 or len(s2) == 0: return 0

    T = [[0 for cols in range(len(s2) + 1)] for rows in range(len(s1) + 1)]

    for row in range(1, len(T)):
        for col in range(1, len(T[0])):
            if s1[row - 1] == s2[col -1]:
                T[row][col] = 1 + T[row - 1][col - 1]
            
            else:
                T[row][col] = max(T[row - 1][col], T[row][col - 1])

    return T[len(s1)][len(s2)]

import unittest
class TestLongestCommonSubsequence(unittest.TestCase):
    def test_s1s2_empty(self):
        self.assertEqual(lcs('', ''), 0)

    def test_len_zero_lcs(self):
        self.assertEqual(lcs("abc", "def"), 0)

    def test_lcs(self):
        self.assertEqual(lcs("GXTXAYB", "AGGTAB"), 4)
        self.assertEqual(lcs("abba", "acdba"), 3)

if __name__ == "__main__": unittest.main()