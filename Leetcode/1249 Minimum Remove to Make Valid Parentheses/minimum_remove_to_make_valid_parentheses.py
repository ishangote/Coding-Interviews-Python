import unittest


# Time: O(n), where n => length of input string
# Space: O(n)
def minimum_remove_valid_parentheses(input_string):
    string_list = list(input_string)
    balance = 0

    for idx, ch in enumerate(string_list):
        if ch == "(":
            balance += 1
        elif ch == ")":
            if balance == 0:
                string_list[idx] = ""
            else:
                balance -= 1
        else:
            continue

    for idx in range(len(string_list) - 1, -1, -1):
        if balance == 0:
            break
        if string_list[idx] == "(":
            string_list[idx] = ""
            balance -= 1

    return "".join(string_list)


class TestMinimumRemoveToMakeValidParentheses(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(
            minimum_remove_valid_parentheses("lee(t(c)o)de)"), "lee(t(c)o)de"
        )
        self.assertEqual(minimum_remove_valid_parentheses("a)b(c)d"), "ab(c)d")
        self.assertEqual(minimum_remove_valid_parentheses("))(("), "")
        self.assertEqual(minimum_remove_valid_parentheses("(a(b(c)d)"), "(a(bc)d)")


if __name__ == "__main__":
    unittest.main()
