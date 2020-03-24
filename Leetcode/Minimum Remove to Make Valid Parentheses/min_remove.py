# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the 
# resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
"""
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 
Constraints:
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

def min_remove_parentheses(s):
    #Lists in python are mutable!
    s = list(s)

    balance = 0
    for i, c in enumerate(s):
        if c == '(': balance += 1
        if c == ')':
            if balance == 0: 
                s[i] = ''
            else: 
                balance -= 1

        
    for i in range(len(s) - 1, -1, -1):
        if balance == 0: break
        if s[i] == '(': 
            s[i] = ''
            balance -=1

    return ''.join(s)

import unittest
class TestMinimumRemoveToMakeValidParentheses(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(min_remove_parentheses("lee(t(c)o)de)"), "lee(t(c)o)de")
        self.assertEqual(min_remove_parentheses("a)b(c)d"), "ab(c)d")
        self.assertEqual(min_remove_parentheses("))(("), "")
        self.assertEqual(min_remove_parentheses("(a(b(c)d)"), "(a(bc)d)")

if __name__ == "__main__": unittest.main()    