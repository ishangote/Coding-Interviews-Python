# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.
"""
Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
] 
Output: "" 

Explanation: The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.


# Step1: Extracting relations between
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Two adjacent words at a time:
wrt, wrf => t -> f
wrf, er => w -> e
er, ett => r -> t
ett, rfttm => e -> r, m

        
        e -> r -> t -> f    m
        ^
        w

Topological Sorting (Requires DAG)

Note: Zip Function
>>> words = ['abc', 'bdw', 'pqe', 'pww']
>>> for first_word, second_word in zip(words, words[1:]):
...     print(first_word, second_word)
... 
abc bdw
bdw pqe
pqe pww

>>> s1 = "abc"
>>> s2 = "ab"
>>> for c, d in zip(s1, s2):
...     print(c, d)
... 
a a
b b
"""

from collections import defaultdict
def make_graph(words):
    graph = defaultdict(set)
    in_degree = {}
    for word in words:
        for ch in word:
            in_degree[ch] = 0

    for first_word, second_word in zip(words, words[1:]):
        for ch1, ch2 in zip(first_word, second_word):
            if ch1 != ch2:
                #Very important => [za, zb, ca, cb] => a->b edge should not be added twice to in_degree! Hence...
                if ch2 not in graph[ch1]:
                    graph[ch1].add(ch2)
                    in_degree[ch2] += 1
                break
        else:
            # Check that second word isn't a prefix of first word...
            if len(second_word) < len(first_word): 
                return []

    return [graph, in_degree]

def topological_sort(graph, in_degree):
    stack = [vertex for vertex in in_degree if in_degree[vertex] == 0]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node)
        for nbr in graph[node]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0: stack.append(nbr)
    
    for vertex in in_degree:
        if in_degree[vertex] > 0: return ""
    
    return ''.join(ans)

def alien_order(words):
    graph = make_graph(words)
    return topological_sort(graph[0], graph[1]) if graph else ""

import unittest
class TestAlienDictionary(unittest.TestCase):
    def test_make_graph(self):
        self.assertEqual(make_graph(["za","zb","ca","cb"]), [{'a':{'b'}, 'z':{'c'}}, {'a': 0, 'b': 1, 'c': 1, 'z': 0}])
        self.assertEqual(make_graph(["ozvcdpgfq","mridvkklqj","dpwecbwor","xxtistijm","xxuon","tudbazpggu","hnuumktbjy","bogbcoi"]), [{'o': {'m'}, 'm': {'d'}, 'd': {'x'}, 't': {'u', 'h'}, 'x': {'t'}, 'h': {'b'}}, {'o': 0, 'u': 1, 'g': 0, 'i': 0, 'b': 1, 'c': 0, 'h': 1, 'z': 0, 's': 0, 't':1, 'y':0 , 'k':0, 'v':0, 'j':0, 'f':0, 'p':0, 'd':1, 'e':0, 'q':0, 'r':0, 'n':0, 'a':0, 'w':0, 'm':1, 'x':1, 'l':0}])

    def test_alien_order(self):
        self.assertEqual(alien_order(["wrt", "wrf", "er", "ett", "rfttzmn"]), "nmzwertf")
        self.assertEqual(alien_order(['x', 'z']), "xz")
        self.assertEqual(alien_order(['x', 'z', 'x']), "")

        self.assertEqual(alien_order(['ab', 'abc']), "cba")
        self.assertEqual(alien_order(['abc', 'ab']), "")
        
        self.assertEqual(alien_order(["za","zb","ca","cb"]), "abzc")

        #Might fail for this test but multiple answers to topological sort...
        self.assertEqual(alien_order(["ozvcdpgfq","mridvkklqj","dpwecbwor","xxtistijm","xxuon","tudbazpggu","hnuumktbjy","bogbcoi"]), "yansewjlkirqfgpcvzomdxthbu")

if __name__ == "__main__": unittest.main()