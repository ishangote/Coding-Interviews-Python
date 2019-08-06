# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "". All given inputs are in lowercase letters a-z.
"""
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Approach 1: Horizontal:

apple, apply, ape. at
|__________|
lcp = appl -> compare with next element

appl <-> ape -> lcp = ap -> compare with next element

ap <-> at -> lcp = a -> no further elements hence return a

Approach 2: Vertical

^
apple   a is commomn
apply   a is commomn
ape     a is commomn
at      a is commomn
^

 ^
apple   p is commomn
apply   p is commomn
ape     p is commomn
at      p != t => lcp = a -> return a
 ^

Python zip function:
>>> s = ["apple", "apply", "ape", "at"]
>>> for c in zip(*s):
...     print(c)

truncates remaining charcters which do not have correspondance

('a', 'a', 'a', 'a')
('p', 'p', 'p', 't')

len(set(c[0])) = 1 {a}
len(set(c[1])) = 2 {p, t}
"""

def longest_common_prefix(strings):    
    l = 0
    for letter_group in zip(*strings):
        if len(set(letter_group)) > 1: return strings[0][:l]
        l += 1
    return strings[0][:l] if strings else ''

import unittest
class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(longest_common_prefix([""]), "")
    
    def test_all_duplicates(self):
        self.assertEqual(longest_common_prefix(["apple", "apple", "apple"]), "apple")

    def test_no_prefix(self):
        self.assertEqual(longest_common_prefix(["apple", "dog", "cat"]), "")

    def test_generic(self):
        self.assertEqual(longest_common_prefix(["apple", "apply", "apt", "ape", "at"]), "a")

if __name__ == "__main__": unittest.main()