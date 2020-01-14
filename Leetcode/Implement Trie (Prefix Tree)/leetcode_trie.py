"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_end = False
        self.freq = 0

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
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
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word: return True

        node = self.root

        for char in word:
            if char in node.children.keys():
                node = node.children[char]
            else: return False
        return True if node.word_end else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix: return True

        node = self.root

        for char in prefix:
            if char in node.children.keys():
                node = node.children[char]    
            else: return False
        
        return True
        
import unittest
class TestLeetCodeTrie(unittest.TestCase):
    
    def test_generic(self):
        trie = Trie()
        self.assertEqual(trie.insert("apple"), None)
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        self.assertEqual(trie.insert("app"), None)
        self.assertEqual(trie.search("app"), True)

if __name__ == "__main__": unittest.main()