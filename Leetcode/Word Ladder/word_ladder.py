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

import queue

def word_ladder(begin_word, end_word, word_list):
    if begin_word == end_word: return None
    if len(begin_word) != len(end_word): return None
    begin_word, end_word = begin_word.lower(), end_word.lower()

    if not word_list or len(word_list) == 0: return None
    word_list = list(set(word_list))
    if end_word not in word_list: return None

    my_q = queue.Queue()
    my_q.put((begin_word, 0))

    while my_q:
        word, level = my_q.get()
        if word == end_word: return level
        
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i]+ ch + word[i+1:]
                if new_word in word_list:
                    my_q.put((new_word, level + 1))
                    word_list.remove(new_word)
    return None

import unittest
class TestWordLadder(unittest.TestCase):
    def test_word_ladder_invalid_input(self):
        self.assertEqual(word_ladder('', 'cog', ["hot","dot","dog","lot","log","cog"]), None)
        self.assertEqual(word_ladder('hit', 'cog', []), None)

    def test_word_ladder(self):
        self.assertEqual(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 4)
        self.assertEqual(word_ladder("bit", "dog", ["but","put","big","pot","pog","dog","lot"]), 5)
        self.assertEqual(word_ladder("no", "go", ["to"]), None)
        self.assertEqual(word_ladder("bit", "pog", ["but","put","big","pot","pog","pig","dog","lot"]), 3)
        self.assertEqual(word_ladder("aa", "bb", ["ab","bb"]), 2)

if __name__ == "__main__": unittest.main()