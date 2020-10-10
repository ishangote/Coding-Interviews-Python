"""
You are given two strings s and t of the same length, consisting of uppercase English letters. Your task is to find the minimum number of "replacement operations" needed to get some anagram of the string t from the string s. A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.
Example
For s = "AABAA" and t = "BBAAA", the output should be
createAnagram(s, t) = 1;
For s = "OVGHK" and t = "RPGUC", the output should be
createAnagram(s, t) = 4.


Guaranteed constraints:
5 ≤ s.length ≤ 35.
[input] string t
Guaranteed constraints:
t.length = s.length.
[output] integer
The minimum number of replacement operations needed to get an anagram of the string t from the string s.
"""
"""
Questions
1. anagram => both strings are equal in length and have same chars in same frequency

Examples:

s = 
AAABP
t =
ABABQ

chars_count = {
    A:3
    B:1
    P:1
    Q:0
}

t = 
ABABQ
^

chars_count = {
    A:1
    B:-1 -> ans += 1 = 1
    P:1
    Q:-1 -> ans += 1 = 2
}

t = 
ABABQ
    ^
"""

from collections import defaultdict
def createAnagram(s, t):
    # default to 0
    chars_count = defaultdict(lambda: 0)
    #Count chars in s
    for ch in s:
        chars_count[ch] += 1
    
    ans = 0
    for ch in t:
        #If char is in s then use that or update answer
        chars_count[ch] -= 1
        if chars_count[ch] < 0: ans += 1
    
    return ans