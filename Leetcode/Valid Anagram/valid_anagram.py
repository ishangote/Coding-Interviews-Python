"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.


"""

def valid_anagram1(s, t):
    if len(s) == len(t): return sorted(s) == sorted(t)
    return False

# Given a string of length one, return an integer representing the Unicode code point of the character
def valid_anagram2(s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

import unittest
class TestValidAnagram(unittest.TestCase):
    def test_genric(self):
        self.assertEqual(valid_anagram1("anagram", "nagaram"), True)
        self.assertEqual(valid_anagram2("anagram", "nagaram"), True)

        self.assertEqual(valid_anagram1("rat", "tac"), False)
        self.assertEqual(valid_anagram2("rat", "tac"), False)

if __name__ == "__main__": unittest.main()