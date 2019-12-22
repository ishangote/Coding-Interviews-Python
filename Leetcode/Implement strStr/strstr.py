# Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

def strStr(haystack, needle):
    if not haystack and not needle: return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle: return i
        
    return -1

import unittest
class TestStrStr(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(strStr("", ""), 0)
        self.assertEqual(strStr("", "a"), -1)
        self.assertEqual(strStr("abaab", ""), 0)

    def test_generic_inputs(self):
        self.assertEqual(strStr("hello", "ll"), 2)
        self.assertEqual(strStr("hello", "elo"), -1)

if __name__ == "__main__": unittest.main()