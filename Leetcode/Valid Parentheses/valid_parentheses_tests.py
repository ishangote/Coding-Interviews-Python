import unittest
from valid_parentheses import is_valid_parenthesis
class TestIsValidParentheses(unittest.TestCase):
    # def test_none_input(self):
    #     self.assertEqual(is_valid_parenthesis(None), False)
    
    def test_len_one_input(self):
        self.assertEqual(is_valid_parenthesis('{'), False)
        self.assertEqual(is_valid_parenthesis('}'), False)

    def test_generic_example(self):
        self.assertEqual(is_valid_parenthesis("{}[]()"), True)
        self.assertEqual(is_valid_parenthesis("{[]}"), True)

        self.assertEqual(is_valid_parenthesis("{[]()"), False)
        self.assertEqual(is_valid_parenthesis("{]"), False)
    
if __name__ == '__main__': unittest.main()