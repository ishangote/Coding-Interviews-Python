"""
Substring => Contiguous

ms = "aaat"
ch= "t"

Approach 1: Brute Force

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

Approach 2:

how many times to search substring in BF?

a z j s k f z t s, sz
l
r

a z j s k f z t s, sz
l
      r

a z j s k f z t s, sz           Best Soln: zjs
  l
      r

a z j s k f z t s, sz
    l
      r

a z j s k f z t s, sz
    l
            r

a z j s k f z t s, sz
        l
            r

a z j s k f z t s, sz
        l
                r

a z j s k f z t s, sz       Best soln too
            l
                r

a z j s k f z t s, sz
              l
                  r
"""
#Example of Counter
# >>> a = Counter(t)
# >>> a
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

from collections import Counter
def min_window_substring(s, t):    
    hm = Counter(t)
    missing = len(t)    #total number of characters to match
    start, end = 0, 0   # for best solution
    left = 0    #keep moving right right
    
    for right, ch in enumerate(s, 1):   #iterate right from index 1
        if hm[ch] > 0:
            missing -= 1
        hm[ch] -= 1
        
        if missing == 0: #all characters present
            while left < right and hm[s[left]] < 0:
                hm[s[left]] += 1
                left += 1
            hm[s[left]] += 1
            missing += 1

            if end == 0 or right - left < end - start:
                start, end = left, right   # best solution
            left += 1

    return s[start:end]

import unittest
class TestMinWindowSubstring(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(min_window_substring("abcde", "klm"), "")
    def test_generic(self):
        self.assertEqual(min_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(min_window_substring("azjskfzts", "sz"), "zjs")

if __name__ == "__main__": unittest.main()