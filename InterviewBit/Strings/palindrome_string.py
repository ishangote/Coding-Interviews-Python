# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
Example:
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

def isPalindrome(A):
    if not A: return 1
    chars = []
    
    for ch in A:
        if ch.isalnum(): chars.append(ch.lower())
    
    # if chars[::-1] == chars: return 1
    # return 0
    
    lo, hi = 0, len(chars) - 1
    
    while lo < hi:
        if chars[lo] != chars[hi]: return 0
        lo += 1
        hi -= 1
    
    return 1