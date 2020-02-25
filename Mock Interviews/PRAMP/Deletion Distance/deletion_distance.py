"""
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:
input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0

    str1
    ""  f   r   o   g
""  0   1   2   3   4
d   1   2   3   4   5
o   2   3   4   3   4
g   3   4   5   4   3

If i,j > 0 and str1[i] ≠ str2[j] then memo(i,j) = 1 + min(memo(i-1, j), memo(i, j-1))
If i,j > 0 and str1[i] = str2[j], then memo(i,j) = memo(i-1, j-1)
    0    1   2   3
    ""   d   o   g   
0""  0   1   2   3
1f   1   2   3   4   
2r   2   3   4   5
3o   3   4   3   4
4g   4   5   4   3

No need to store the entire matrix. O(min(l1, l2)) Space Complexity

"""

def deletion_distance(str1, str2):
    if str1 == str2: return 0
    if not str1:return len(str2)
    if not str2: return len(str1)

    if len(str1) < len(str2): str1, str2 = str2, str1
    l1, l2 = len(str1), len(str2)
    memo_prev = [0 for i in range(l2 + 1)]
    memo_curr = [0 for i in range(l2 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0: memo_curr[j] = j
            elif j == 0: memo_curr[i] = i
            else: memo_curr[j] = 1 + min(memo_prev[j], memo_curr[j - 1]) if str1[i - 1] != str2[j - 1] else memo_prev[j - 1]

        memo_prev = memo_curr
        memo_curr = [0 for i in range(l2 + 1)]

    return memo_prev[l2]

import unittest
class TestDeletionDistance(unittest.TestCase):
    def test_generic(self):