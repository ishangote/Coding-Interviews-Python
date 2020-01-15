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
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_end = False

def create_trie(words):
    if not words: return None
    root = node = TrieNode('')

    for word in words:
        for char in word:
            if char in node.children:
                node.freq += 1
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                new_node.freq = 1

                node.children[char] = new_node
                node = new_node
        
        node.word_end = True
    return root

def word_search_ii(board, words):
    root = create_trie(words)

    ans = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, root, i, j, "", ans)
    
    return ans


def dfs(board, node, i, j, path, ans):
    if node.word_end == True: 
        ans.add(path)
        node.word_end = False

    if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1: return

    tmp = board[i][j]

    if tmp not in node.children: return

    node = node.children[tmp]

    board[i][j] = '#'
    dfs(board, node.children[tmp], i + 1, j, path + tmp, ans)
    dfs(board, node.children[tmp], i - 1, j, path + tmp, ans)
    dfs(board, node.children[tmp], i, j + 1, path + tmp, ans)
    dfs(board, node.children[tmp], i, j - 1, path + tmp, ans)
    board[i][j] = tmp


import unittest
class TestWordSearchII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(word_search_ii([['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v']], ["oath","pea","eat","rain"]), ["eat","oath"])

if __name__ == "__main__": unittest.main()