import unittest


# Time: O(n), where n => length of input string
# Space: O(n)
def remove_all_adjacent_duplicates_in_string(input_string):
    stack = []

    for ch in input_string:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


class TestRemoveAllAdjacentDuplicatesInString(unittest.TestCase):
    def test_remove_all_adjacent_duplicates_in_string(self):
        self.assertEqual(remove_all_adjacent_duplicates_in_string("abbaca"), "ca")
        self.assertEqual(remove_all_adjacent_duplicates_in_string("azxxzy"), "ay")


if __name__ == "__main__":
    unittest.main()
