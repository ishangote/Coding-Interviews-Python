"""
Questions:
1. Input string empty? No
2. key -ve? no
3. string not mutable

Examples:
s = xyz
k = 2

0  1  2		  23 24 25		
a, b, c, ..., x, y, z
			  ^		^
			  
0  1  2		  23 24 25		
a, b, c, ..., x, y, z
*			     *

0  1  2		  23 24 25		
a, b, c, ..., x, y, z
   &				&

ans = zab

Time: O(n), n => number of chars in input string
Space: O(n)
"""
import string
def caesarCipherEncryptor(input_string, key):
    ch_idx = {}
    idx_ch = {}
    for idx, ch in enumerate(string.ascii_lowercase):
        ch_idx[ch] = idx
        idx_ch[idx] = ch
    
    ans = []
    for ch in input_string:
        _ch = idx_ch[(ch_idx[ch] + key) % 26]
        ans.append(_ch)

    return ''.join(ans)