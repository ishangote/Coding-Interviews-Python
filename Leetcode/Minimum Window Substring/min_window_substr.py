"""
Substring => Contiguous

ms = "aaat"
ch= "t"

Approach 1: Brute Force O(n^2)

0 1 2 3
a a a t

substrings possible: 
left = 0 => a
            aa
            aaa
            aaat
     = 1 => a
            aa
            aat
     = 2 => a
            at
     
     = 3 => t

keep check of the best length substring

Approach 2: Sliding Window
t = abc
s =
0 1 2 3 4 5 6 7 8 9 10
a b d b a n b c d d d

unique_chars_count = 0
chars_count_map = {a: 0, b: 0, c: 0}
l, r = 0, 0
st, end = 0, inf

s =
0 1 2 3 4 5 6 7 8 9 10
a b d b a n b c d d d

unique_chars_count = 1
chars_count_map = {a: 1, b: 0, c: 0}
l, r = 0, 0
st, end = 0, inf

s =
0 1 2 3 4 5 6 7 8 9 10
a b d b a n b c d d d
l r
unique_chars_count = 2
chars_count_map = {a: 1, b: 1, c: 0}
l, r = 0, 1
st, end = 0, inf

s =
0 1 2 3 4 5 6 7 8 9 10
a b d b a n b c d d d
l   r
unique_chars_count = 2
chars_count_map = {a: 1, b: 1, c: 0}
l, r = 0, 1
st, end = 0, inf

s =
0 1 2 3 4 5 6 7 8 9 10
a b d b a n b c d d d
l     r
unique_chars_count = 2
chars_count_map = {a: 1, b: 2, c: 0}
l, r = 0, 1
st, end = 0, inf

...

"""
#Example of Counter
# >>> a = Counter(t)
# >>> a
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})


# Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
# >>> a['k'] -= 1
# >>> a
# Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'k': -1})        Very important it adds chars by itself

# Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'k': -1})
# >>> a['n'] > 0
# False
import sys
def min_window_substring(s, t):
    if s == t: return s
    is_valid_flag = 0
    lo = 0
    st, end = 0, sys.maxsize

    is_valid_dict = {}
    chars_count = {}
    for ch in t:
        chars_count[ch] = 0
        if ch not in is_valid_dict: 
            is_valid_dict[ch] = 1  
        else: 
            is_valid_dict[ch] += 1

    for hi, hi_val in enumerate(s):
        if hi_val not in chars_count: continue
        chars_count[hi_val] += 1

        if chars_count[hi_val] <= is_valid_dict[hi_val]:
            is_valid_flag += 1

        while is_valid_flag == len(t):
            if end - st > hi - lo:
                st, end = lo, hi
            lo_val = s[lo]
            if lo_val in chars_count:
                chars_count[lo_val] -= 1
                if chars_count[lo_val] < is_valid_dict[lo_val]: 
                    is_valid_flag -= 1

            lo +=1

    return s[st : end + 1] if end - st != sys.maxsize else ""

import unittest
class TestMinWindowSubstring(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(min_window_substring("abcde", "klm"), "")
    def test_generic(self):
        self.assertEqual(min_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(min_window_substring("ADOBECODEBAANC", "AABC"), "BAANC")
        self.assertEqual(min_window_substring("ABA", "ABA"), "ABA")
        self.assertEqual(min_window_substring("azjskfzts", "sz"), "zjs")

if __name__ == "__main__": unittest.main()