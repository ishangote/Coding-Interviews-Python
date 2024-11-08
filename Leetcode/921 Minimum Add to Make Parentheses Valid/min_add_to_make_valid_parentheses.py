import unittest


# Time: O(n), where n => length of input string
# Space: O(1)
def adds_to_make_valid_parentheses(input_string):
    open_count, res = 0, 0

    for char in input_string:
        if char == "(":
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                res += 1

    return res + open_count


class TestMinimumAddToMakeValidParentheses(unittest.TestCase):
    def test_adds_to_make_valid_parentheses(self):
        self.assertEqual(adds_to_make_valid_parentheses("())"), 1)
        self.assertEqual(adds_to_make_valid_parentheses(")))"), 3)
        self.assertEqual(adds_to_make_valid_parentheses("()))(("), 4)


if __name__ == "__main__":
    unittest.main()
