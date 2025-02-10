import unittest


# Time: O(n), where n => length of valid string
# Space: O(1)
def max_depth_parentheses(valid_string):
    res, open_count = 0, 0

    for ch in valid_string:
        if ch == "(":
            open_count += 1
            res = max(res, open_count)
        elif ch == ")":
            open_count -= 1
        else:
            continue

    return res


class MaximumNestingDepthOfParentheses(unittest.TestCase):
    def test_max_depth_parentheses(self):
        self.assertEqual(max_depth_parentheses("()(())((()()))"), 3)
        self.assertEqual(max_depth_parentheses("(1+(2*3)+((8)/4))+1"), 3)
        self.assertEqual(max_depth_parentheses("(1)+((2))+(((3)))"), 3)


if __name__ == "__main__":
    unittest.main()
