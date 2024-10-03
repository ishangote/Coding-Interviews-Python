import unittest


# Time: O(n^2), where n => length of input_string
# since extracting substring and adding to possible_substrings takes O(n)
#
# Space: O(n^2), since in the worst case we can have upto n substrings and
# each substring can have length 1 - n
def repeated_substring_pattern_bf(input_string):
    possible_substrings = []

    for idx in range(len(input_string)):
        if idx + 1 == len(input_string) or len(input_string) % (idx + 1) != 0:
            continue

        possible_substrings.append(input_string[: idx + 1])

    for substring in possible_substrings:
        if substring * (len(input_string) // len(substring)) == input_string:
            return True

    return False


# Time O(n + n) ~ O(n) where, n => length of input_string
# Space: O(n + n) ~ O(n)
def repeated_substring_pattern(input_string):
    doubled_string = input_string + input_string
    doubled_string = doubled_string[1 : len(doubled_string) - 1]

    return input_string in doubled_string


class TestRepeatedSubstringPattern(unittest.TestCase):
    def test_repeated_substring_pattern_bf(self):
        self.assertEqual(repeated_substring_pattern_bf("ababab"), True)
        self.assertEqual(repeated_substring_pattern_bf("ababa"), False)
        self.assertEqual(repeated_substring_pattern_bf("a"), False)
        self.assertEqual(repeated_substring_pattern_bf("bad"), False)

    def test_repeated_substring_pattern(self):
        self.assertEqual(repeated_substring_pattern("ababab"), True)
        self.assertEqual(repeated_substring_pattern("ababa"), False)
        self.assertEqual(repeated_substring_pattern("a"), False)
        self.assertEqual(repeated_substring_pattern("bad"), False)


if __name__ == "__main__":
    unittest.main()
