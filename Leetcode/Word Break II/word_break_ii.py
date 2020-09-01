# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences.
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
"""
Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

"""
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = catsanddog

                    catsanddog
                (cat)/       \(cats)
                sanddog     anddog
                /(sand)         \(and)
              dog               dog
              /(dog)               \(dog)
             ""                    ""

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

                                pineapplepenapple
                                /(pine)     \(pineapple)
                        applepenapple       penapple
                        /(apple) \(applepen)     \(pen)
                    penapple      apple         apple
                    /(pen)          |(apple)        \(apple)
                apple               ""              ""
                /(apple)
               ""

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

                            catsandog
                            /(cats) \(cat)
                        andog        sandog
                        /(and)          \(sand)
                      og                og

"""
from functools import lru_cache
# Top - Down
def word_break_ii(s, word_dict):
    word_dict = set(word_dict)
    @lru_cache(None)
    def generate_sentences(i):
        if i == len(s): return [[]]
        
        ans = []
        for word in word_dict:
            if s.startswith(word, i):
                for sentence in generate_sentences(i + len(word)):
                    ans.append([word] + sentence)
        
        return ans

    return [' '.join(sent) for sent in generate_sentences(0)]

import unittest
class TestWordBreakII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ['cats and dog', 'cat sand dog'])
        self.assertEqual(word_break_ii("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple'])
        self.assertEqual(word_break_ii("catsandog", ["cats", "dog", "sand", "and", "cat"]), [])

if __name__ == "__main__": unittest.main()