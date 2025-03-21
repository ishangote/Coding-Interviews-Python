import unittest


# Time: O(n * m), where n => number of strings, m => length of common prefix
# Space: O(1)
def longest_common_prefix_horizontal_scanning(input_strings):
    prefix = input_strings[0]

    for idx in range(1, len(input_strings)):
        word = input_strings[idx]

        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(longest_common_prefix_horizontal_scanning([""]), "")

    def test_all_duplicates(self):
        self.assertEqual(
            longest_common_prefix_horizontal_scanning(["apple", "apple", "apple"]),
            "apple",
        )

    def test_no_prefix(self):
        self.assertEqual(
            longest_common_prefix_horizontal_scanning(["apple", "dog", "cat"]), ""
        )

    def test_generic(self):
        self.assertEqual(
            longest_common_prefix_horizontal_scanning(
                ["apple", "apply", "apt", "ape", "at"]
            ),
            "a",
        )


if __name__ == "__main__":
    unittest.main()
