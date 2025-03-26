import unittest
import sys


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


# * Variation: Merge 2 sorted intervals


# Time: O(n + m), where n => length of intervals1, m => length of intervals2
# Space: O(1)
def merge_intervals_variation(intervals1, intervals2):
    if not intervals1:
        return intervals2
    if not intervals2:
        return intervals1

    pt1, pt2 = 0, 0
    stack = []

    # Initialize stack list with the interval that starts first.
    if intervals1[0][0] <= intervals2[0][0]:
        stack.append(intervals1[0])
        pt1 += 1
    else:
        stack.append(intervals2[0])
        pt2 += 1

    # Merge intervals from both lists.
    while pt1 < len(intervals1) or pt2 < len(intervals2):
        if pt1 < len(intervals1) and (
            pt2 >= len(intervals2) or intervals1[pt1][0] <= intervals2[pt2][0]
        ):
            interval = intervals1[pt1]
            pt1 += 1
        else:
            interval = intervals2[pt2]
            pt2 += 1

        # Merge if overlapping; otherwise, add the interval.
        if is_overlapping(stack[-1], interval):
            stack[-1] = merge_interval_helper(stack[-1], interval)
        else:
            stack.append(interval)

    return stack


class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([[1, 9]]), [[1, 9]])
        self.assertEqual(
            merge_intervals([[1, 2], [10, 15], [4, 9]]), [[1, 2], [4, 9], [10, 15]]
        )

        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])
        self.assertEqual(merge_intervals([[1, 6], [3, 4], [5, 6]]), [[1, 6]])


class TestMergeIntervalsVariation(unittest.TestCase):
    def test_both_empty(self):
        self.assertEqual(merge_intervals_variation([], []), [])

    def test_one_empty(self):
        self.assertEqual(merge_intervals_variation([[1, 3]], []), [[1, 3]])
        self.assertEqual(merge_intervals_variation([], [[2, 4]]), [[2, 4]])

    def test_non_overlapping(self):
        intervals1 = [[1, 2], [5, 6]]
        intervals2 = [[3, 4], [7, 8]]
        self.assertEqual(
            merge_intervals_variation(intervals1, intervals2),
            [[1, 2], [3, 4], [5, 6], [7, 8]],
        )

    def test_overlapping(self):
        intervals1 = [[1, 5], [10, 14]]
        intervals2 = [[2, 6], [13, 18]]
        # [1,5] and [2,6] merge to [1,6], [10,14] and [13,18] merge to [10,18]
        self.assertEqual(
            merge_intervals_variation(intervals1, intervals2), [[1, 6], [10, 18]]
        )

    def test_complex_case(self):
        intervals1 = [[1, 3], [6, 9]]
        intervals2 = [[2, 5], [10, 13]]
        # [1,3] and [2,5] merge to [1,5]; [6,9] and [10,13] remain separate.
        self.assertEqual(
            merge_intervals_variation(intervals1, intervals2),
            [[1, 5], [6, 9], [10, 13]],
        )


if __name__ == "__main__":
    unittest.main()
