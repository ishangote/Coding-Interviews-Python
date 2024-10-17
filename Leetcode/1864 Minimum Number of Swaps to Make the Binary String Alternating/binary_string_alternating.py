import unittest
from collections import Counter


def min_swaps_helper(expected, input_string):
    mismatches = 0
    for ch in input_string:
        if ch != expected:
            mismatches += 1

        expected = "1" if expected == "0" else "0"

    return mismatches // 2


# Time: O(n), where n => length of input string
# Space: O(1)
def minimum_swaps(input_string):
    count_map = Counter(input_string)

    if abs(count_map["0"] - count_map["1"]) > 1:
        return -1

    if count_map["0"] > count_map["1"]:
        return min_swaps_helper("0", input_string)

    if count_map["0"] < count_map["1"]:
        return min_swaps_helper("0", input_string)

    return min(min_swaps_helper("0", input_string), min_swaps_helper("1", input_string))


class TestMinimumSwaps(unittest.TestCase):
    def test_minimum_swaps(self):
        self.assertEqual(minimum_swaps("1"), 0)
        self.assertEqual(minimum_swaps("0"), 0)
        self.assertEqual(minimum_swaps("010"), 0)

        self.assertEqual(minimum_swaps("111000"), 1)
        self.assertEqual(minimum_swaps("01101"), 1)
        self.assertEqual(minimum_swaps("100"), 1)

        self.assertEqual(minimum_swaps("000"), -1)
        self.assertEqual(minimum_swaps("1000"), -1)


if __name__ == "__main__":
    unittest.main()
