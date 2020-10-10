# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
# After doing so, return the number of remaining intervals.
"""
Questions:
1. Is the input sorted? -> No

Constraints: 
c <= a and b <= d

Examples:
[[1,4],[3,6],[2,8]]
Sort by start => 
[[1,4],[2,8],[3,6]]
                    ^
ans = 
[[1,4], [2,8]]
         *

------------------

[[1,4],[2,3]]
             ^
ans = 
[[1, 4]]

------------------

Case where conflict in start times?
[[1,2], [3,4], [1,4]]
sort -> 
[[1,4], [1,2], [3,4]]

Time: O(nlogn)
Space: O(n)

"""
def remove_intervals(intervals):
    intervals.sort(key = lambda x:(x[0], -x[1]))
    ans = [intervals[0]]
    
    for intv in intervals[1:]:
        if ans[-1][0] <= intv[0] and intv[1] <= ans[-1][1]: continue
        ans.append(intv)
    
    return len(ans)

if __name__ == "__main__":
    intervals_len = int(input("Enter Number of Intervals: "))
    intervals = []
    for itr in range(intervals_len):
        nums = list(map(int, input("Enter the interval numbers separated by space ").strip().split()))
        intervals.append(nums)
        
    print("Length after removal: ", remove_intervals(intervals))