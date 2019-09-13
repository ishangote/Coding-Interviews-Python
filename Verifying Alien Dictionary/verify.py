# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# Note:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.

"""
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', 
where '∅' is defined as the blank character which is less than any other character (More info).
                               012345678910 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
["hello","leetcode"], order = "hlabcdefgij  k  m  n  o  p  q  r  s  t  u  v  w  x  y  z"

dict = {h:0
        l:1
        a:2
        ...
        z:25}
          *             *
words = [[0,6,1,1,14], [1,6,6,19,4,14,5,6]]     first_char <second_char => true
"""

def verify_words(words, order):
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

import unittest
class TestAilienDictionary(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(verify_words(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(verify_words(["word","world","row"], "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(verify_words(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)

if __name__ == "__main__": unittest.main()