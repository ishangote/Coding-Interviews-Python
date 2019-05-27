
"""
n = 1 ()
n = 2 (()), ()()
n = 3 ((())), (()()), , ()(()), (())(), ()()()

-> length of each is 2 * n -> n open n close



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