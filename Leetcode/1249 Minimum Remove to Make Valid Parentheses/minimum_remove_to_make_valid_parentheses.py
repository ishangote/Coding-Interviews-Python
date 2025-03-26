import unittest
from collections import defaultdict


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


# ------------------------------------------------------------------------ #

# * Variation: Multiple Types of Parentheses


# Time: O(n), where n => length of s
# Space: O(s)
def minimum_remove_valid_parentheses_variation(input_string):
    # Convert string to list (for in-place modification)
    s_list = list(input_string)

    # Counters for unmatched opening brackets
    balances = {"(": 0, "[": 0, "{": 0}

    # Forward pass: remove extra closing brackets.
    # If a closing bracket appears when there’s no matching opening,
    # mark it for removal by setting it to an empty string.
    for i, ch in enumerate(s_list):
        if ch == "(":
            balances["("] += 1
        elif ch == "[":
            balances["["] += 1
        elif ch == "{":
            balances["{"] += 1
        elif ch == ")":
            if balances["("] > 0:
                balances["("] -= 1
            else:
                s_list[i] = ""
        elif ch == "]":
            if balances["["] > 0:
                balances["["] -= 1
            else:
                s_list[i] = ""
        elif ch == "}":
            if balances["{"] > 0:
                balances["{"] -= 1
            else:
                s_list[i] = ""

    # Reverse pass: remove extra opening brackets.
    # For each opening bracket that is still “extra” (its count > 0),
    # remove occurrences from right to left.
    for i in range(len(s_list) - 1, -1, -1):
        if s_list[i] == "(" and balances["("] > 0:
            s_list[i] = ""
            balances["("] -= 1
        elif s_list[i] == "[" and balances["["] > 0:
            s_list[i] = ""
            balances["["] -= 1
        elif s_list[i] == "{" and balances["{"] > 0:
            s_list[i] = ""
            balances["{"] -= 1

    return "".join(s_list)


class TestMinimumRemoveToMakeValidParentheses(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(
            minimum_remove_valid_parentheses("lee(t(c)o)de)"), "lee(t(c)o)de"
        )
        self.assertEqual(minimum_remove_valid_parentheses("a)b(c)d"), "ab(c)d")
        self.assertEqual(minimum_remove_valid_parentheses("))(("), "")
        self.assertEqual(minimum_remove_valid_parentheses("(a(b(c)d)"), "(a(bc)d)")


class TestMinimumRemoveValidParenthesesVariation(unittest.TestCase):
    def test_balanced_string(self):
        s = "a(b)c"
        # The string is already balanced.
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "a(b)c")

    def test_extra_closing(self):
        s = "a)b(c)d)"
        # Forward pass removes unmatched ')' at index 1 and index 7.
        # Expected: "ab(c)d"
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "ab(c)d")

    def test_extra_opening(self):
        s = "a(b(c"
        # Forward pass: counts become {"(": 2}.
        # Reverse pass: removes one '(' at index 3 then one at index 1.
        # Expected: "abc"
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "abc")

    def test_multiple_types_balanced(self):
        s = "a{b[c(d]e)f}g"
        # Even though the order might look off,
        # the counts for each type are balanced so nothing is removed.
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "a{b[c(d]e)f}g")

    def test_all_extra_brackets(self):
        s = "({[)]}"
        # Forward pass:
        #   '(' -> count('(') becomes 1
        #   '{' -> count('{') becomes 1
        #   '[' -> count('[') becomes 1
        #   ')' -> matches a '(' so count('(') becomes 0
        #   ']' -> matches a '[' so count('[') becomes 0
        #   '}' -> matches a '{' so count('{') becomes 0
        # No extra removals are needed.
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "({[)]}")

    def test_empty_string(self):
        s = ""
        self.assertEqual(minimum_remove_valid_parentheses_variation(s), "")


if __name__ == "__main__":
    unittest.main()
