import unittest


def monotonic_stack_helper(heights, direction):
    res = [len(heights)] * len(heights) if direction == "NEXT" else [-1] * len(heights)
    stack = []
    (lo, hi, skip) = (
        (0, len(heights), 1) if direction == "NEXT" else (len(heights) - 1, -1, -1)
    )

    for idx in range(lo, hi, skip):
        while stack and heights[idx] < heights[stack[-1]]:
            update_idx = stack.pop()
            res[update_idx] = idx

        stack.append(idx)

    return res


# Time: O(n), where n => length of heights
# Space: O(n)
def largest_rectangle_histogram(heights):
    res = 0
    next_smaller_index = monotonic_stack_helper(heights, "NEXT")
    prev_smaller_index = monotonic_stack_helper(heights, "PREV")

    for idx, height in enumerate(heights):
        res = max(res, (next_smaller_index[idx] - prev_smaller_index[idx] - 1) * height)

    return res


class TestLargestRectangleInHistogram(unittest.TestCase):
    def test_largest_rectangle_histogram(self):
        self.assertEqual(largest_rectangle_histogram([1, 2, 3, 4, 5]), 9)
        self.assertEqual(largest_rectangle_histogram([5, 4, 3, 2, 1]), 9)
        self.assertEqual(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_rectangle_histogram([6, 1, 4, 3, 4, 1]), 9)
        self.assertEqual(largest_rectangle_histogram([2, 1, 5, 3, 6, 2, 3]), 10)


if __name__ == "__main__":
    unittest.main()
