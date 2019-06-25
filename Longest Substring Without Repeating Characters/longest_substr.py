# Given a string, find the length of the longest substring without repeating characters.
"""
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Approach 1: Brute Force: For all substrings -> O(n^2) and check if duplicates O(n) -> O(n^3)

----------------------------------------------------

Approach 2: Sliding Window with hashset
0 1 2 3 4 5
p w w k e w
      i
            j
hs -> maintains all chars in the current substring
max_len = max(max_len, j - i + 1)

hs = {}
max_len = 0

hs = {p}
max_len = 1

hs = {p, w}
max_len = 2

hs = {}
max_len = 2

hs = {w, k, e}
max_len = 3

hs = {k, e, w}
max_len = 3

----------------------------------------------------

Approach 3: Sliding Window Optimized with hashmap

The reason is that if char_at_j is duplicate in current substring then we don't need to increase i little by little. We can skip all the elements in the range i to duplicated element (may or may not be at i)
hm -> to map char and idx 

0 1 2 3 4 5
p w w k e w
i
st
hm = {p:0, }
max_len = 1

0 1 2 3 4 5
p w w k e w
  i
st
hm = {p:0, w:1}
max_len = 2

0 1 2 3 4 5
p w w k e w
    i
    st
hm = {p:0, w:2}
max_len = 2

0 1 2 3 4 5
p w w k e w
      i
    st
hm = {p:0, w:2, k:3}
max_len = 2

0 1 2 3 4 5
p w w k e w
        i
    st
hm = {p:0, w:2, k:3, e:4}
max_len = 3

0 1 2 3 4 5
p w w k e w
          i
      st
hm = {p:0, w:5, k:3, e:4}
max_len = 3
"""
def longest_substring_sliding_window(input_string):
    if not input_string: return 0
    hs, i, j = set(), 0, 0
    max_len = 0
    while j < len(input_string) and i < len(input_string):
        if input_string[j] in hs:
            hs.remove(input_string[i])
            i += 1
        else:
            hs.add(input_string[j])
            max_len = max(max_len, j - i + 1)
            j += 1
    return max_len

def longest_substring_sliding_window_optimized(input_string):
    if not input_string: return 0
    hm, max_len = {}, 0
    st = 0

    for idx, chr in enumerate(input_string):
        if chr in hm:
            st = max(st, hm[chr] + 1)

        hm[chr] = idx
        max_len = max(max_len, idx - st + 1)

    return max_len

import unittest
class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(longest_substring_sliding_window(''), 0)
        self.assertEqual(longest_substring_sliding_window_optimized(''), 0)

    def test_longest_substring_generic(self):
        self.assertEqual(longest_substring_sliding_window("abcabcbb"), 3)
        self.assertEqual(longest_substring_sliding_window("bbbbb"), 1)
        self.assertEqual(longest_substring_sliding_window("pwwkew"), 3)

        self.assertEqual(longest_substring_sliding_window_optimized("abcabcbb"), 3)
        self.assertEqual(longest_substring_sliding_window_optimized("bbbbb"), 1)
        self.assertEqual(longest_substring_sliding_window_optimized("pwwkew"), 3)

if __name__ == "__main__": unittest.main()