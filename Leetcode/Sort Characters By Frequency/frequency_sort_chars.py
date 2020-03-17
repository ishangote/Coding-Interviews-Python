# Given a string, sort it in decreasing order based on the frequency of characters.
"""
Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

import heapq
def frequency_sort(s):
    counts = {}
    for ch in s:
        if ch in counts: counts[ch] += 1
        else: counts[ch] = 1
    
    max_heap = []
    for ch in counts:
        heapq.heappush(max_heap, [-counts[ch], ch])
        
    ans = ""
    
    while max_heap:
        count, ch = heapq.heappop(max_heap)
        ans = ans + (-count * ch)
        
    return ans

import unittest
class TestSortCharactersByFrequency(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(frequency_sort("aabcAecc"), "cccaaAbe")

if __name__ == "__main__": unittest.main()