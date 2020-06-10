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
    unique_chars_count = 0
    st, end = 0, sys.maxsize
    left = 0

    chars_count_map = {}
    for ch in t:
        chars_count_map[ch] = 0

    for right, right_val in enumerate(s):
        if right_val not in chars_count_map: continue
        if chars_count_map[right_val] == 0: unique_chars_count += 1
        chars_count_map[right_val] += 1

        while unique_chars_count == len(t):
            if end - st > right - left: st, end = left, right
            if s[left] in chars_count_map:
                chars_count_map[s[left]] -= 1
                if chars_count_map[s[left]] == 0: unique_chars_count -= 1

            left += 1

    return s[st : end + 1] if end - st != sys.maxsize else ""

import unittest
class TestMinWindowSubstring(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(min_window_substring("abcde", "klm"), "")
    def test_generic(self):
        self.assertEqual(min_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(min_window_substring("azjskfzts", "sz"), "zjs")

if __name__ == "__main__": unittest.main()