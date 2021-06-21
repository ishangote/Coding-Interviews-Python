"""
Questions:
1. Are interval start/end integers? Yes
2. Inplace? Not necessary but can mutate input
3. is input sorted? Not necessary

Examples:
intervals = 
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
  		  						  i		
                          		  		  j
merge_interval = [3, 8]
res = 
[[1, 2], [3, 8], [9, 10]]

ans = 
[[1, 2], [3, 8], [9, 10]]

Important Case: [[-20, 30], [1, 22]]
[a, b], [c, d], s.t. a <= c
overlap if =>
1. c <= b => 
merged interval = [min(a, c), max(b, d)]

Time: O(nlogn), sorting, n is number of intervals
Space: O(n)
"""

def is_overlap(intv1, intv2):
    return True if intv2[0] <= intv1[1] else False

def merge_intervals(intervals):
    if not intervals: return []
    i = 0
    res = []
    # Sort Intervals
    intervals.sort(key = lambda x: x[0])

    while i < len(intervals):
        j = i + 1
        merge_interval = intervals[i]
        while j < len(intervals):
            if not is_overlap(merge_interval, intervals[j]): break
            merge_interval[0] = min(merge_interval[0], intervals[j][0])
            merge_interval[1] = max(merge_interval[1], intervals[j][1])
            j += 1

        res.append(merge_interval)
        i = j

    return res