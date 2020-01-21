"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.


[1,2],[3,5],[6,7],[8,10],[12,16]    [4, 9]
  
CASES:
1) Size of interval array as 0.

2) newInterval being an interval preceding all intervals in the array. Given interval (3,6),(8,10), insert and merge (1,2)

3) newInterval being an interval succeeding all intervals in the array. Given interval (1,2), (3,6), insert and merge (8,10)

4) newInterval not overlapping with any interval and falling in between 2 intervals in the array. Given interval (1,2), (8,10) insert and merge (3,6) 

5) newInterval covering all given intervals. Given interval (3, 5), (7, 9) insert and merge (1, 10)

"""

def merge_intervals(intervals, new_interval):
    ans = []
    for i, intv in enumerate(intervals):
        if intv[1] < new_interval[0]: ans.append(intv)
        elif intv[0] > new_interval[1]:
            ans.append(new_interval)
            return ans + intervals[i:]
        
        else:
            new_interval = [min(new_interval[0], intv[0]), max(new_interval[1], intv[1])]

    ans.append(new_interval)
    return ans


import unittest
class TestMergeIntervals(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(merge_intervals([], [2, 5]), [[2,5]])
    def test_generic(self):
        self.assertEqual(merge_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]), [[1,2],[3,10],[12,16]])
        self.assertEqual(merge_intervals([[1,3],[6,9]], [2, 5]), [[1,5],[6,9]])
        
if __name__ == "__main__": unittest.main()