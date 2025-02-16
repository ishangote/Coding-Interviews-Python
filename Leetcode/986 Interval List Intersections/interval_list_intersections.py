import unittest


def is_overlapping(interval1, interval2):
    return interval1[0] <= interval2[1] and interval2[0] <= interval1[1]


# Time: O(N + M), where n => number of intervals in first list, m => number of intervals in second list
# Space: O(1)
def interval_list_intersections(first_list, second_list):
    first, second = 0, 0
    res = []

    while first < len(first_list) and second < len(second_list):
        interval1, interval2 = first_list[first], second_list[second]

        if is_overlapping(interval1, interval2):
            res.append(
                [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
            )

        if interval1[1] <= interval2[1]:
            first += 1

        else:
            second += 1

    return res


class TestIntervalListIntersections(unittest.TestCase):
    def test_interval_list_intersections(self):
        self.assertListEqual(
            interval_list_intersections(
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
            ),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        )

        self.assertListEqual(
            interval_list_intersections(
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [],
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
