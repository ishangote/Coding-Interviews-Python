"""
REF: https://www.geeksforgeeks.org/alternatively-merge-two-strings-in-java/

Input:
          i
s1 = hello 
s2 = worldmen
          j
ans = 'hweolrllod'

Output: 

ans = hweolrllodmen
"""

def merge_alternate_strings(s1, s2):
    ans = ''
    i, j = 0, 0
    
    while i < len(s1) and j < len(s2):
        ans += s1[i]
        i += 1
        ans += s2[j]
        j += 1
        if i  == len(s1) and j == len(s2): return ans

    return ans + s1[i:] if j == len(s2) else ans + s2[j:]

import unittest
class TestMergeTwoAlternateStrings(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(merge_alternate_strings("", "hello"), "hello")
        self.assertEqual(merge_alternate_strings("", ""), "")
    def test_genric(self):
        self.assertEqual(merge_alternate_strings("hello", "worldmen"), "hweolrllodmen")
        self.assertEqual(merge_alternate_strings("forgeeks", "geeks"), "fgoeregkeseks")

if __name__ == "__main__": unittest.main()