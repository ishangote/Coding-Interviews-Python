# Given a string including character: {}[]() return true if it is valid

"""
Valid: {}, (){}, {()}, ...
Invlaid: {, (}, ]()[, ...

# { [ } ]
      ^
hm = {")": "(", "}": "{", "]": "["}
stack = ['{', '[' ]

"""
import unittest
def is_valid_parenthesis(input_string):
    if not input_string: return False

    hm = {')': '(', '}': '{', ']': '['}
    stack = []

    # { } [ ] ( ) 

    for ch in input_string:
        if ch in hm.keys():
            if len(stack) != 0 and hm[ch] == stack[-1]: stack.pop()
            else: return False
        else:
            stack.append(ch)

    return len(stack) == 0

class TestIsValidParentheses(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(is_valid_parenthesis(None), False)
    
    def test_len_one_input(self):
        self.assertEqual(is_valid_parenthesis('{'), False)
        self.assertEqual(is_valid_parenthesis('}'), False)

    def test_generic_example(self):
        self.assertEqual(is_valid_parenthesis("{}[]()"), True)
        self.assertEqual(is_valid_parenthesis("{[]}"), True)

        self.assertEqual(is_valid_parenthesis("{[]()"), False)
        self.assertEqual(is_valid_parenthesis("{]"), False)
    
if __name__ == '__main__': unittest.main()