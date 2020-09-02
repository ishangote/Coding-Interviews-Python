# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
hit -> [*it] -> check all possible combinations -> if in wordlist append all to queue -> graph traversed to next node -> repeat for that element
    -> [h*t]
    -> [hi*]

# start = hit, end = cog

Init ->
word_list:
["hot","dot","dog","lot","log","cog"]
level = 1
queue [(hit, 1)]

Iteration of while queue ->

word_list:
["dot","dog","lot","log","cog"]
level = 1 -> hit popped
queue [(hot, 2)]

word_list:
["dog","log","cog"]
level = 2 -> hot popped
queue [(dot, 3), (lot, 3)]

word_list:
["log","cog"]
level = 3 -> dot popped
queue [(lot, 3), (dog, 4)]

word_list:
["cog"]
level = 3 -> lot popped
queue [(dog, 4), (log, 4)]

word_list:
[]
level = 4 -> dog popped
queue [(log, 4), (cog, 5)]

word_list:
[]
level = 4 -> log popped
queue [(cog, 5)]

word_list:
[]
level = 5 -> cog popped -> return level = 5 as popped == end_word
queue []

"""
from collections import defaultdict
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    combinations = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            combinations[word[:i] + '*' + word[i + 1:]].append(word)
            
    queue = deque([[beginWord, 1]])
    visited = set()
    
    while queue:
        word, trans_length = queue.pop()
        visited.add(word)
        if word == endWord: return trans_length
        for i in range(len(word)):
            comb = word[: i] + '*' + word[i + 1:]
            for new_word in combinations[comb]:
                if new_word not in visited:
                    queue.appendleft([new_word, trans_length + 1])
                    
            combinations[comb] = []
                        
    return 0

import unittest
class TestWordLadder(unittest.TestCase):
    def test_word_ladder(self):
        self.assertEqual(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(word_ladder("bit", "dog", ["but","put","big","pot","pog","dog","lot"]), 6)
        self.assertEqual(word_ladder("no", "go", ["to"]), 0)
        self.assertEqual(word_ladder("bit", "pog", ["but","put","big","pot","pog","pig","dog","lot"]), 4)
        self.assertEqual(word_ladder("aa", "bb", ["ab","bb"]), 3)

if __name__ == "__main__": unittest.main()