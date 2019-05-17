# Given a collection of intervals, merge all overlapping intervals
"""

[[1,3],[2,6],[8,10],[15,18]]
                     ^
stack: [[1, 6], [8, 10], [12, 18]]


overlap(interval1, interval2):
    if interval2[0] <= interval1[1] < interval2[1]: true

"""
def overlap(interval1, interval2):
    if interval2[0] > interval1[1]: return False
    return True

def merge_interval(intervals):

    if not intervals or len(intervals) == 0: return intervals
    
    #Sort intervals
    intervals.sort(key = lambda x:x[0])

    stack = []
    stack.append(intervals[0])
    for interval in intervals[1:len(intervals)]:
        if overlap(stack[-1], interval):
            stack[-1][1] = max(stack[-1][1], interval[1])

        else: stack.append(interval)

    return stack

import unittest
class TestMergeIntervals(unittest.TestCase):
    
    def test_merge_intervals(self):
        self.assertEqual(merge_interval([[1,3],[2,6],[8,10],[15,18]]), [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(merge_interval([[1,4], [4, 5]]), [[1, 5]])

    def test_one_interval(self):
        self.assertEqual(merge_interval([[1, 9]]), [[1, 9]])

    def test_none_interval(self):
        self.assertEqual(merge_interval([]), [])
        self.assertEqual(merge_interval(None), None)

    def test_no_merge_intervals(self):
        self.assertEqual(merge_interval([[1, 2], [10, 15], [4, 9]]), [[1, 2], [4, 9], [10, 15]])

    def test_all_merge_intervals(self):
        self.assertEqual(merge_interval([[1, 6], [3, 4], [5, 6]]), [[1, 6]])

if __name__ == "__main__": unittest.main()