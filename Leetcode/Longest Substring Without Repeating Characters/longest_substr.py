# Given a string, find the length of the longest substring without repeating characters.

"""
Questions:
1. Can substring/ans be empty? yes
2. Clarification about substring -> contiguous

Examples:

0 1 2 3 4 5
p w w k e w
    i
      j
check_valid(p) => True
check_valid(pw) => True
check_valid(pww) => False
check_valid(ww) => False
check_valid(w) => True
check_valid(wk) => True
...

Brute Force: check all possible substrings
Time: O(n^3)
Space: O(k) => For set to check if all chars are unique


Sliding Window: Optimization over brute force => O(1) to check if the cur_substr is valid
0 1 2 3
d v d f
i
j

ans = 0
cur_substr_chars = {d}

0 1 2 3
d v d f
i
  j

ans = 0
cur_substr_chars = {d, v}

0 1 2 3
d v d f
  i
    j

ans = 2
cur_substr_chars = {v}


0 1 2 3
d v d f
  i
      j

ans = 2
cur_substr_chars = {v, d}

0 1 2 3
d v d f
  i
        j

ans = 2
cur_substr_chars = {v, d, f}

return max(ans, len(cur_substr_chars)) = 3

"""

def lengthOfLongestSubstring(s):
    i, j = 0, 0
    cur_substr_chars = set()
    ans = 0
    while i < len(s) and j < len(s):
        if s[j] not in cur_substr_chars:
            cur_substr_chars.add(s[j])
            j += 1
        
        else:
            ans = max(ans, len(cur_substr_chars))
            # Remove the element at ith index
            cur_substr_chars.remove(s[i])
            i += 1
    
    
    # Handled cases like 'aab'
    return max(ans, len(cur_substr_chars))

"""
Testcases:

Input                   Expected                Actual
''                      0                       0
'a'                     1                       1
"aa"                    1                       1
"ab"                    2                       2     
"aab"                   2                       2
"dvdf"                  3                       3
"""

"""
Time: O(2n) ~ O(n) in worst case we will go over each character twice
Space: O(n)
"""

import unittest
class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(lengthOfLongestSubstring(''), 0)
        self.assertEqual(lengthOfLongestSubstring_optimized(''), 0)

    def test_longest_substring_generic(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == "__main__": unittest.main()