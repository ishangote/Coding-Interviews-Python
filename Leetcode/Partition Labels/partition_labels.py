# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible 
# so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

"""
abc
[a, b, c]
[ab, c]
[a, bc]

abba
[abba]

abbcdefga
[abbcdefga]

* = start of part
j = end of part
i = current pointer

*
      j
0 1 2 3 4
a b a b c
      i

        *
            j
0 1 2 3 4 5 6 7 8
a b a b c h c m n 
            i

              *
              j
0 1 2 3 4 5 6 7 8
a b a b c h c m n 
              i

                *
                j
0 1 2 3 4 5 6 7 8
a b a b c h c m n 
                i
"""
# Time = O(n)
# Space = O(1) because in the worst case there will be 26 characters to store in last_occ whcih is constant

def partition_labels(ip_str):
    # Input Validations

    # Last occurance of each character
    last_occ = {}
    for idx, ch in enumerate(ip_str):
        last_occ[ch] = idx
    
    st = end = 0
    ans = []
    for idx, ch in enumerate(ip_str):
        end = max(end, last_occ[ch])
        if idx == end:
            ans.append(end - st + 1)
            st = idx + 1
    
    return ans

import unittest
class TestPartitionLabels(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(partition_labels("abc"), [1, 1, 1])
        self.assertEqual(partition_labels("ababchcmn"), [4, 3, 1, 1])
        self.assertEqual(partition_labels("ababcbacadefegdehijhklij"), [9, 7, 8])

if __name__ == "__main__": unittest.main()       