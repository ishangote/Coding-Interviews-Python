"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        node.is_word = True

def search_words(board, i, j, node, path, ans):
    if node.is_word:
        ans.add(path)
        node.is_word = False
    
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return

    tmp = board[i][j]
    node = node.children.get(tmp)
    if not node: return

    board[i][j] = '#'
    search_words(board, i + 1, j, node, path + tmp, ans)
    search_words(board, i - 1, j, node, path + tmp, ans)
    search_words(board, i, j + 1, node, path + tmp, ans)
    search_words(board, i, j - 1, node, path + tmp, ans)
    board[i][j] = tmp
    
def word_search_ii(board, words):
    trie = Trie()
    for word in words:
        trie.insert_word(word)
    
    ans = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            search_words(board, i, j, trie.root, "", ans)
    
    return ans

import unittest
class TestWordSearchII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(word_search_ii([['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v']], ["oath","pea","eat","rain"]), {"eat","oath"})

if __name__ == "__main__": unittest.main()