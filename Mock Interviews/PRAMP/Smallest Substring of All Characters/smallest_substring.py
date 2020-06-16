"""
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.
Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

Explanation: Check image in folder
"""
import sys
def get_shortest_unique_substring(arr, s):
  is_valid_flag = 0
  lo = 0
  st, end = 0, sys.maxsize

  #is_valid_dict maintains the valid count of chars in t
  is_valid_dict = {}
  #chars_count maintains the count of chars in the current substring
  chars_count = {}
  for ch in arr:
    chars_count[ch] = 0
    if ch not in is_valid_dict: 
      is_valid_dict[ch] = 1  
    else: 
      is_valid_dict[ch] += 1

  for hi, hi_val in enumerate(s):
    if hi_val not in chars_count: continue
    chars_count[hi_val] += 1

    #if count of current char is <= required valid count of current char update flag
    if chars_count[hi_val] <= is_valid_dict[hi_val]:
      is_valid_flag += 1

    while is_valid_flag == len(arr):
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
class TestSmallestUniqueSubstring(unittest.TestCase):
    def test_pramp(self):
        self.assertEqual(get_shortest_unique_substring(["A"], ""), '')
        self.assertEqual(get_shortest_unique_substring(["A"], "B"), '')
        self.assertEqual(get_shortest_unique_substring(["A"], "A"), 'A')
        self.assertEqual(get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD"), 'BANC')
        self.assertEqual(get_shortest_unique_substring(["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI"), "KADOBECODEBANCDDDEI")
        self.assertEqual(get_shortest_unique_substring(["x","y","z"], "xyyzyzyx"), "zyx")
        self.assertEqual(get_shortest_unique_substring(["x","y","z","r"], "xyyzyzyx"), '')

if __name__ == "__main__": unittest.main()