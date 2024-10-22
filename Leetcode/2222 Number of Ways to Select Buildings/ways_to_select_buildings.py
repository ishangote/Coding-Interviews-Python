import unittest


def helper(input_string, direction, bit):
    res = [0] * len(input_string)
    count = 0

    start, end, step = (
        (0, len(input_string), 1)
        if direction == "LEFT"
        else (len(input_string) - 1, -1, -1)
    )

    for idx in range(start, end, step):
        if input_string[idx] == bit:
            count += 1
        else:
            res[idx] = count

    return res


# Time: O(n), where n => length of input string
# Space: O(n)
def ways_to_select_buildings(input_string):
    left_zeroes = helper(input_string, "LEFT", "0")
    right_zeroes = helper(input_string, "RIGHT", "0")
    left_ones = helper(input_string, "LEFT", "1")
    right_ones = helper(input_string, "RIGHT", "1")

    res = 0

    for idx, bit in enumerate(input_string):
        if bit == "0":
            res += left_ones[idx] * right_ones[idx]
        else:
            res += left_zeroes[idx] * right_zeroes[idx]

    return res


class TestNumberOfWaysToSelectBuildings(unittest.TestCase):
    def test_ways_to_select_buildings(self):
        self.assertEqual(ways_to_select_buildings("001101"), 6)
        self.assertEqual(ways_to_select_buildings("11100"), 0)


if __name__ == "__main__":
    unittest.main()
