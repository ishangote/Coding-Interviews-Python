#Write a function that reverses a string. The input string is given as an array of characters char[].
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#You may assume all the characters consist of printable ascii characters.

"""
['h', 'e', 'l', 'l', 'o']    ->    ['o', 'l', 'l', 'e', 'h']
"""

def reverse_string(s):

    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s