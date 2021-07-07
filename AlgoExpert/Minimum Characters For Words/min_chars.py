"""
Questions:
1. Case sensetive? yes
2. Can word have spaces? no

Examples:
words = 
["this", "that", "did", "deed", "them!", "a"]
                          ^
word = "that"
freq:
t: 2
h: 1
a: 1

word = "did"
freq:
d: 2
i: 1

chars_used = 
{
 "t": 2
 "h": 1
 "i": 1
 "s": 1
 'd': 2
}

Time: O(w * l), w => number of words, l => length of longest word in words
Space: O(c), c => total number of characters in all words combined
"""
from collections import defaultdict
def minimum_characters(words):
    chars_used = defaultdict(lambda: 0)
    for word in words:
        freq = defaultdict(lambda: 0)
        for ch in word:
            freq[ch] += 1
        
        for ch in freq:
            if chars_used[ch] >= freq[ch]: continue
            chars_used[ch] += (freq[ch] - chars_used[ch])
    
    res = []
    for ch in chars_used:
        for freq in range(chars_used[ch]):
            res.append(ch)
    
    return res