import unittest


# Time: O(n), where n => length of input string
# Space: O(1)
def minimum_add_to_make_parentheses_valid(input_string):
    balance, res = 0, 0

    for char in input_string:
        if char == "(":
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                res += 1

    return res + balance


class TestMinimumAddToMakeValidParentheses(unittest.TestCase):
    def test_minimum_add_to_make_parentheses_valid(self):
        self.assertEqual(minimum_add_to_make_parentheses_valid("())"), 1)
        self.assertEqual(minimum_add_to_make_parentheses_valid(")))"), 3)
        self.assertEqual(minimum_add_to_make_parentheses_valid("()))(("), 4)


if __name__ == "__main__":
    unittest.main()
