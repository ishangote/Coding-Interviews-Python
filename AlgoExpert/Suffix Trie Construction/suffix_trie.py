"""
Questions:
1. is empty string suffix? yes

Examples
string = "apple"
                                        '/'
                            a        p      l           e*
                        p          p  l        e*
                    p             l    e*
                l               e*
            e*

insert(apple)
self.root = 
{   
    a: {p: {p: {l: {e: {*: True}}}}}
    p: {p: {l: {e: {*: True}}}, l: {e: {*: True}}}
    l: {e: {*: True}}
    e: {*: True}
}
"""
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def insert_substring_starting_at(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node: node[letter] = {}
            node = node[letter]

        node[self.endSymbol] = True

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def contains(self, string):
        node = self.root

        for letter in string:
            if letter not in node: return False
            node = node[letter]

        return self.endSymbol in node