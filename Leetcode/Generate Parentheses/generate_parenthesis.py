
"""
Solution: https://www.youtube.com/watch?v=sz1qaKt0KGQ&t=1s

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

n = 1 ()
n = 2 (()), ()()
n = 3 ((())), (()()), , ()(()), (())(), ()()()

-> length of each is 2 * n -> n open n close

Our Choice -> Open a bracket or close a bracket
Our Constraints -> 1. cannot close until we open. 2. n count of open brackets
Our Goal -> n*2 is length of any correct answer n = 1 () -> 2n length


"""

def generate_parenthesis(n):
    result = []
    def backtrack(curr_string, open_count, close_count):
        if len(curr_string) == 2 * n: 
            result.append(curr_string)
            return

        if open_count < n:
            backtrack(curr_string + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(curr_string + ')', open_count, close_count + 1)

    backtrack('', 0, 0)    
    return result

import unittest
class TestGenerateParenthesis(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(generate_parenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

if __name__ == "__main__": unittest.main()