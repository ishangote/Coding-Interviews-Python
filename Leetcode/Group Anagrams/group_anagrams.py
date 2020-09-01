#Given an array of strings, group anagrams together.

"""

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[["ate","eat","tea"], ["nat","tan"], ["bat"]]

"""
# Time: O(NKlogK) where N is number of words in strs and K is length of the longest word in strs
# Space: O(NK)
from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

import unittest
class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagram(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

if __name__ == '__main__': unittest.main()