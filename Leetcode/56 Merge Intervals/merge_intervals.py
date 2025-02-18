import unittest


def is_overlapping(interval1, interval2):
    if interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
        return True
    return False


def merge_interval_helper(interval1, interval2):
    return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]


# Time: O(nlogn), where n => number of intervals
# Space: O(n)
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]

    for idx in range(1, len(intervals)):
        if is_overlapping(intervals[idx], stack[-1]):
            merged_interval = merge_interval_helper(intervals[idx], stack.pop())
            stack.append(merged_interval)
        else:
            stack.append(intervals[idx])

    return stack


class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([[1, 9]]), [[1, 9]])
        self.assertEqual(
            merge_intervals([[1, 2], [10, 15], [4, 9]]), [[1, 2], [10, 15], [4, 9]]
        )

        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])
        self.assertEqual(merge_intervals([[1, 6], [3, 4], [5, 6]]), [[1, 6]])


if __name__ == "__main__":
    unittest.main()
