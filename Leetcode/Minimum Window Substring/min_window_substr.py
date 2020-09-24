"""
Questions:
1. Example: s = 'xaab' t = 'aab' => return 'aab' not 'ab'
2. Clarification about substring => contiguous
3. Case sensitive? Yes 'a' and 'A' not same

Example:
T = ABA
    0 1 2 3 4 5 6 7 8 9
S = X A B X T A M A B Y
      i
              j
    
#Checks if all chars in T or not
check_valid(X) -> False
check_valid(XA) -> False
check_valid(XABX) -> False
check_valid(XABXT) -> False
check_valid(XABXTA) -> True  -> record temp ans

Brute Force: 
Time: O(n^3)
Space: O(len(T))

Sliding Window:

T = ABA
    0 1 2 3 4 5 6 7 8 9
S = X A B B T A M A B Y
    i
    j

t_chars = {
A: 2
B: 1
}

cur_substr_chars = {
A: 0
B: 0
}

valid_char_count = 0

    0 1 2 3 4 5 6 7 8 9
S = X A B B T A M A B Y
    i
              j

t_chars = {
A: 2
B: 1
}

cur_substr_chars = {
A: 1
B: 2
}

valid_char_count = 3

    0 1 2 3 4 5 6 7 8 9
S = X A B B T A M A B Y
      i
              j

t_chars = {
A: 2
B: 1
}

cur_substr_chars = {
A: 1
B: 2
}

valid_char_count = 3
 
"""
import sys
from collections import Counter

def minWindow(s, t):
    t_chars = Counter(t)
    valid_char_count = 0
    cur_substr_chars = {}
    
    st, lo, end = 0, 0, sys.maxsize
    
    for tchar in t_chars: cur_substr_chars[tchar] = 0
    
    for hi, hi_val in enumerate(s):
        if hi_val not in t_chars: continue
        cur_substr_chars[hi_val] += 1
        
        if cur_substr_chars[hi_val] <= t_chars[hi_val]: valid_char_count += 1
        
        while valid_char_count == len(t):
            if end - st > hi - lo:
                st, end = lo, hi
            
            lo_val = s[lo]
            if lo_val in t_chars:
                cur_substr_chars[lo_val] -= 1
                if cur_substr_chars[lo_val] < t_chars[lo_val]: valid_char_count -= 1
            
            lo += 1
    
    return s[st : end + 1] if end - st != sys.maxsize else ""

"""
Time: O(s + t)
Space: O(s + t)
"""

import unittest
class TestMinWindowSubstring(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(minWindow("abcde", "klm"), "")
        self.assertEqual(minWindow("abcde", "abcde"), "abcde")
    def test_generic(self):
        self.assertEqual(minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minWindow("ADOBECODEBAANC", "AABC"), "BAANC")
        self.assertEqual(minWindow("ABA", "ABA"), "ABA")
        self.assertEqual(minWindow("azjskfzts", "sz"), "zjs")

if __name__ == "__main__": unittest.main()