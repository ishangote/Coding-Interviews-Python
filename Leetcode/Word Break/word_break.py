# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
"""
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
def word_break(s, word_dict):
    word_set = set(word_dict)
    # Memoization dictionary stroes answers to duplicated sub problems True/False
    memo = {}
    return word_break_util(s, word_dict, memo)
    
def word_break_util(s, word_set, memo):
    if not s: return True
    if s in memo: return memo[s]

    for i in range(1, len(s) + 1):
        if s[:i] not in word_set:
            continue
        if word_break_util(s[i:], word_set, memo):
            memo[s] = True
            return True
    
    memo[s] = False
    return False

import unittest
class TestWordBreak(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(word_break("leetcode", ["leet", "code"]), True)
        self.assertEqual(word_break("thequickbrownfox", ["the", "quick", "fox", "brown"]), True)
        self.assertEqual(word_break("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "away"]), False)
        self.assertEqual(word_break("bedbathandbeyond", ["teddy", "bath", "bedbath", "and", "beyond"]), True)
        self.assertEqual(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
        self.assertEqual(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)
        
if __name__ == "__main__": unittest.main()