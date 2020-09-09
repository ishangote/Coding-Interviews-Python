"""
You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
"""

"""
f o o ( b a r ( b a z  )  )  b  l  i  m
      ^
stack = ["foo"]

f o o ( b a r ( b a z  )  )  b  l  i  m
      ^
stack = ["foo", ""]

f o o ( b a r ( b a z  )  )  b  l  i  m
            ^
stack = ["foo", "bar"]

f o o ( b a r ( b a z  )  )  b  l  i  m
              ^
stack = ["foo", "bar" ""]

f o o ( b a r ( b a z  )  )  b  l  i  m
                    ^
stack = ["foo", "bar" "baz"]

f o o ( b a r ( b a z ) ) b l i m
                      ^
stack = ["foo", "barzab"]

f o o ( b a r ( b a z ) ) b l i m
                        ^
stack = ["foobazrab"]

f o o ( b a r ( b a z ) ) b l i m
                                ^
stack = ["foobazrabblim"]
"""
def reverseInParentheses(inputString):
    stack = ['']
    for ch in inputString:
        if ch =='(':
            stack.append("")
        elif ch == ')':
            add = stack.pop()[::-1]
            stack[-1] += add
        else:
            stack[-1] += ch
            
    return stack.pop()

import unittest
class TestReverseInParantheses(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(reverseInParentheses("(bar)"), "rab")
        self.assertEqual(reverseInParentheses("foo(bar)baz"), "foorabbaz")
        self.assertEqual(reverseInParentheses("foo(bar)baz(blim)"), "foorabbazmilb")

if __name__ == "__main__": unittest.main()