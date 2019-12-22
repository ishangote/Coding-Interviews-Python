# Given a collection of intervals, merge all overlapping intervals.
"""
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge_intervals(intervals):
    if not intervals: return []
    intervals = sorted(intervals, key = lambda x: x[0])
    ans = [intervals[0]]
    for x in intervals[1:]:
        if x[0] <= ans[-1][1]: ans[-1][1] = max(x[1], ans[-1][1])
        else: ans.append(x)

    return ans

import unittest
class TestMergeOverlappingIntervals(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(merge_intervals([]), [])
    
    def test_generic(self):
        self.assertEqual(merge_intervals([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge_intervals([[1,4],[0,4]]), [[0, 4]])

if __name__ == "__main__": unittest.main()