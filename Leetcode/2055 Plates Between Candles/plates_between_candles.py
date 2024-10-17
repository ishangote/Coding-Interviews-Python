import unittest


def get_prefix_sum_plates(input_string):
    prefix_sum = []
    count = 0

    for ch in input_string:
        if ch == "*":
            count += 1

        prefix_sum.append(count)

    return prefix_sum


def get_nearest_left_candles(input_string):
    nearest_left = []
    nearest_plate_idx = -1

    for idx, ch in enumerate(input_string):
        if ch == "|":
            nearest_plate_idx = idx

        nearest_left.append(nearest_plate_idx)

    return nearest_left


def get_nearest_right_candles(input_string):
    nearest_right = []
    nearest_plate_idx = -1

    for idx in range(len(input_string) - 1, -1, -1):
        if input_string[idx] == "|":
            nearest_plate_idx = idx

        nearest_right.append(nearest_plate_idx)

    return nearest_right[::-1]


# Time: O(n), where n => length of input string
# Space: O(n)
def plates_between_candles(input_string, queries):
    prefix_sum_plates = get_prefix_sum_plates(input_string)
    nearest_left_candles = get_nearest_left_candles(input_string)
    nearest_right_candles = get_nearest_right_candles(input_string)

    def compute_plates_between(query):
        lo, hi = query
        candle_to_right_of_lo = nearest_right_candles[lo]
        candle_to_left_of_hi = nearest_left_candles[hi]

        if (
            candle_to_right_of_lo != -1
            and candle_to_left_of_hi != -1
            and candle_to_right_of_lo <= candle_to_left_of_hi
        ):
            return (
                prefix_sum_plates[candle_to_left_of_hi]
                - prefix_sum_plates[candle_to_right_of_lo]
            )

        return 0

    return list(map(compute_plates_between, queries))


class TestPlatesBetweenCandles(unittest.TestCase):
    def test_plates_between_candles(self):
        self.assertEqual(plates_between_candles("**|**|***|", [[2, 5], [5, 9]]), [2, 3])
        self.assertEqual(
            plates_between_candles(
                "***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
            ),
            [9, 0, 0, 0, 0],
        )


if __name__ == "__main__":
    unittest.main()
