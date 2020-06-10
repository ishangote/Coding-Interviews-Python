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
  unique_chars_count = 0
  st, end = 0, sys.maxsize
  left = 0
  
  chars_count_map = {}
  for ch in arr:
    chars_count_map[ch] = 0
    
  for right, right_val in enumerate(s):
    if right_val not in chars_count_map: continue
    if chars_count_map[right_val] == 0: unique_chars_count += 1
    chars_count_map[right_val] += 1
    
    while unique_chars_count == len(arr):
      if end - st > right - left: st, end = left, right
      if s[left] in chars_count_map:
        chars_count_map[s[left]] -= 1
        if chars_count_map[s[left]] == 0: unique_chars_count -= 1
      
      left += 1
      
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