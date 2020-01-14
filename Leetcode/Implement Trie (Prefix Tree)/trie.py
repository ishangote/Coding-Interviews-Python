"""
                                   root
                                    -
                            p              q
                        q      s          r
                      n   r    s           t
                    m      s    t         s

"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_end = False
        self.freq = 0

from collections import deque
class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def add_word(self, word):
        if not word: return
        node = self.root

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

    """
    Check and return 
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    def search_prefix(self, prefix):
        if not prefix: return True

        node = self.root

        for char in prefix:
            if char in node.children.keys():
                node = node.children[char]    
            else: return False
        
        return node.freq

    def search_word(self, word):
        if not word: return True

        node = self.root

        for char in word:
            if char in node.children.keys():
                node = node.children[char]
            else: return False
        return True if node.word_end else False

    # def print_trie(self):
    #     queue = deque([self.root])
    #     ans = []

    #     while queue:
    #         node = queue.pop()
    #         for chld in node.children.keys():
    #             queue.appendleft(node.children[chld])
    #         ans.append(node.char)

    #     return ans[1:]

import unittest
class TestLeetCodeTrie(unittest.TestCase):
    
    def test_generic(self):
        trie = Trie()
        self.assertEqual(trie.add_word("apple"), None)
        self.assertEqual(trie.search_word("apple"), True)
        self.assertEqual(trie.search_word("app"), False)
        self.assertEqual(trie.search_prefix("app"), 1)
        self.assertEqual(trie.add_word("app"), None)
        self.assertEqual(trie.search_word("app"), True)

if __name__ == "__main__": unittest.main()