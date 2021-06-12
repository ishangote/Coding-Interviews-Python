"""
Questions:
1. Case sensetive? input contains only lowercase chars

Examples:
in = 
0 1 2 3 4 5 6
a b c d c a f
^

counts = {
	a: 2
	b: 1
	c: 2
	d: 1
	f: 1
}

out = 1

Time: O(n), n => num of chars in input
Space: O(n)
"""
from collections import defaultdict
def first_non_repeating(input_string):
    char_count = defaultdict(lambda: 0)
    
    for ch in input_string:
        char_count[ch] += 1
    
    for idx, ch in enumerate(input_string):
        if char_count[ch] == 1: return idx
    
    return -1