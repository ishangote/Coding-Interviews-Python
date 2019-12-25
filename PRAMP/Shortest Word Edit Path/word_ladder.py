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

def word_ladder(begin, end, words):
    if end not in words or not end or not begin or not words: return None

    hm = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            hm[w[:i] + '*' + w[i + 1:]].append(w)

    #Output:

    q = deque([(begin, 0)])
    visited = set()
    visited.add(begin)

    while q:
        w, level = q.popleft()
        for i in range(len(w)):
            new_w = w[:i] + '*' + w[i + 1:]
            for word in hm[new_w]:
                if word not in visited:
                    if word == end: return level + 1
                    visited.add(word)
                    q.append((word, level + 1))
            hm[new_w] = []

    return 0

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