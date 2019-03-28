#Given an array of strings, group anagrams together.

"""

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[["ate","eat","tea"], ["nat","tan"], ["bat"]]

"""

import unittest
def group_anagrams(input_strings):

    hm = {}
    for word in input_strings:
        if ''.join(sorted(word)) in hm: hm[''.join(sorted(word))].append(word)

        else: hm[''.join(sorted(word))] = [word]

    return list(hm.values())