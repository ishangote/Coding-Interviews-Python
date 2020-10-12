# Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

"""
Questions:
1. Empty string? -> Not as input
2. Case sensitive? -> only lowercase letters in input

To find smallest lexicographical subsequence which has all chars of original string only once.

Examples:
 01234567
"bcacdcbc"
    i     
        j

Candidate: (Keep track of smallest one lexicographically)
bcad
cadb
acdb
cd

Time: O(n^2) where n is the length of input
Space: O(n) to store the answer

--------------------------
Efficient:
for example, s = 'cdadabcc', s contains a, b, c, d
index['a'] = [2, 4]
index['b'] = [5]
index['c'] = [0, 6, 7]
index['d'] = [1, 3]

which will be the first letter in ans?
it will be letter 'a', cause 2 < min(5, 7, 3), (5,7,3) is the last index of other letters

last_char_idx = {
    a: 4
    b: 5
    c: 7
    d: 3
}

s = 'cdadabcc'
       i
stack = [c, d]

s = 'cdadabcc'
       i
stack = [c]
check if last_idx_d > i? -> yes hence pop

s = 'cdadabcc'
       i
stack = []
check if last_idx_c > i? -> yes hence pop

s = 'cdadabcc'
           i
stack = [a, d, b]
check if b is smaller than d? - yes then,
check if last_idx_d > i? -> no hence can not pop

s = 'cdadabcc'
           i
stack = [a, d, b]
check if c is smaller than b? - no hence simply append

s = 'cdadabcc'
              i
stack = [a, d, b, c]
"""
def remove_duplicate_letters(s):
    assert 1 <= len(s) <= 1000
    assert all(ch in "abcdefghijklmnopqrstuvwxyz" for ch in s)

    # O(n)
    last_char_idx = {ch:idx for idx, ch in enumerate(s)}
    stack = []
    in_stack = [False] * 26
    
    for idx, ch in enumerate(s):
        if in_stack[ord(ch) - ord('a')] : continue
        while stack and stack[-1] > ch and last_char_idx[stack[-1]] > idx:
            popped = stack.pop()
            in_stack[ord(popped) - ord('a')] = False
            
        stack.append(ch)
        in_stack[ord(ch) - ord('a')] = True
    
    return ''.join(stack)
"""
Time: O(n)
Space:O(26)
"""

if __name__ == "__main__":
    s = input("Enter string: ")
    print(remove_duplicate_letters(s))