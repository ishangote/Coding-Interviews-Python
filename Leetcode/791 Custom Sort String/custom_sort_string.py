import unittest
from collections import Counter


# Time: O(n + m), where n => length of input_string, m => length of order
# Space: O(n)
def custom_sort_string(order, input_string):
    char_count = Counter(input_string)
    res = ""

    for ch in order:
        if ch not in char_count:
            continue
        res += char_count[ch] * ch
        del char_count[ch]

    for ch in char_count:
        res += char_count[ch] * ch

    return res


class TestCustomSortString(unittest.TestCase):
    def test_custom_sort_string(self):
        self.assertEqual(custom_sort_string("bcafg", "abcd"), "bcad")
        self.assertEqual(custom_sort_string("bcafg", "xyz"), "xyz")
        self.assertEqual(custom_sort_string("bcafg", "gfacb"), "bcafg")


if __name__ == "__main__":
    unittest.main()
