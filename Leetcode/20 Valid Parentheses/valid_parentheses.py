import unittest


# Time: O(n), where n => length of input_string
# Space: O(n)
def is_valid_parenthesis(input_string):
    close_to_open_map = {")": "(", "}": "{", "]": "["}

    stack = []

    for parentheses in input_string:
        if parentheses in close_to_open_map:
            # Check if stack empty for case input = "}" to avoid list index out of range error
            if not stack or stack[-1] != close_to_open_map[parentheses]:
                return False
            stack.pop()
        else:
            stack.append(parentheses)

    # "return True" not working for edge case input = "{" as stack is not empty after the for loop
    return not stack


class TestIsValidParentheses(unittest.TestCase):
    def test_is_valid_parentheses(self):
        self.assertEqual(is_valid_parenthesis("{"), False)
        self.assertEqual(is_valid_parenthesis("}"), False)

        self.assertEqual(is_valid_parenthesis("{}[]()"), True)
        self.assertEqual(is_valid_parenthesis("{[]}"), True)

        self.assertEqual(is_valid_parenthesis("{[]()"), False)
        self.assertEqual(is_valid_parenthesis("{]"), False)


if __name__ == "__main__":
    unittest.main()
