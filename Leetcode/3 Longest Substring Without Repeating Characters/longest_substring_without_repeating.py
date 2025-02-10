import unittest


# Time: O(n), where n => length of input string
# Space: O(n)
def length_substring_without_repeating(input_string):
    char_set = set()
    res, lb, rb = 0, 0, 0

    while rb < len(input_string):
        while input_string[rb] in char_set and lb < rb:
            char_set.remove(input_string[lb])
            lb += 1

        char_set.add(input_string[rb])
        res = max(res, len(char_set))
        rb += 1

    return res


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(length_substring_without_repeating(""), 0)

    def test_longest_substring_generic(self):
        self.assertEqual(length_substring_without_repeating("abcabcbb"), 3)
        self.assertEqual(length_substring_without_repeating("bbbbb"), 1)
        self.assertEqual(length_substring_without_repeating("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
