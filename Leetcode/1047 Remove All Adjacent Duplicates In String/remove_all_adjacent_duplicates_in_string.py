import unittest


# Time: O(n), where n => length of input string
# Space: O(1)
def remove_all_adjacent_duplicates_in_string(input_string):
    stack = []

    for ch in input_string:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


# ------------------------------------------------------ #


# * Variation: Remove All Duplicates
# Time: O(n)
# Space: O(1)
def remove_all_duplicates(input_string):
    stack = []
    idx = 0

    while idx < len(input_string):
        if not stack or stack[-1] != input_string[idx]:
            stack.append(input_string[idx])
            idx += 1
        elif input_string[idx] == stack[-1]:
            while idx < len(input_string) and input_string[idx] == stack[-1]:
                idx += 1
            stack.pop()

    return "".join(stack)


class TestRemoveAllAdjacentDuplicatesInString(unittest.TestCase):
    def test_remove_all_adjacent_duplicates_in_string(self):
        self.assertEqual(remove_all_adjacent_duplicates_in_string("abbaca"), "ca")
        self.assertEqual(remove_all_adjacent_duplicates_in_string("azxxzy"), "ay")

    def test_remove_all_duplicates(self):
        self.assertEqual(remove_all_duplicates("abbbacxdd"), "cx")


if __name__ == "__main__":
    unittest.main()
