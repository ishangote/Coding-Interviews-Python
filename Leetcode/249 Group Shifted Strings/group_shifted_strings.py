import unittest
from collections import defaultdict


def get_hash(input_string):
    hash = ()
    for idx in range(len(input_string) - 1):
        difference = (ord(input_string[idx + 1]) - ord(input_string[idx]) + 26) % 26
        hash += (difference,)

    return hash


# Time: O(n*m), where n => number of strings and m => max length of a string
# Space: O(n)
def group_shifted_strings(strings):
    grouped_string = defaultdict(list)

    for s in strings:
        hash = get_hash(s)
        grouped_string[hash].append(s)

    return list(grouped_string.values())


class TestGroupShiftedStrings(unittest.TestCase):
    def test_group_shifted_strings(self):
        self.assertListEqual(
            group_shifted_strings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]),
            [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]],
        )
        self.assertListEqual(group_shifted_strings(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
