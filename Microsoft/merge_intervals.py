"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

[[3, 6], [5, 8], [6,8], [8, 13], [21, 22]]
                                  i

[[3,13], [21, 21]]
          j

[s1, e1], [s2, e2]
if e1 >= s2: [s1, max(e1, e2)]
"""

def merge_intervals(intervals):
    if not intervals or len(intervals) == 1: return intervals
    intervals.sort()
    ans = [intervals[0]]

    for idx in range(1, len(intervals)):
        if ans[-1][1] >= intervals[idx][0]:
            ans[-1][1] = max(ans[-1][1], intervals[idx][1])
        else:
            ans.append(intervals[idx])

    return ans

"""
In                            Expected                       Acutal
[]                                  []                       []
[[1, 3]]                            [[1, 3]]                 [[1, 3]]

[[1,3],[2,5]]                       [[1,5]]                  [[1, 5]]

[[1,3],[6,7]]                       [[1,3],[6,7]]            [[1,3],[6,7]]

[[1,3],[2,6],[8,10],[15,18]]    [[1,6], [8,10], [15,18]]
                     i

[[1,6], [8,10]]
         j

"""