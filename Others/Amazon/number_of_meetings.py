# Question: We have to find the maximum number of meetings that we can allocate keeping in mind the arrival times and duration of those meetings.

# Inputs: Arrival Time = [ 1,3,5 ] , Duration= [ 2,2,2]
# Output: 3 ( maximum number of presentations that we can allocate without overlapping)

"""
Example 1:
start_times = [1, 3, 5]
durations = [2, 2, 2]

1   2   3   4   5   6   7
---------
    m1
        ---------
            m2
                ---------
                    m3

ans = 3

=========================================

Example 2:
start_times = [1, 5, 7, 9]
durations = [6, 1, 3, 1]
=>
end_times = 
[7, 6, 10, 10]

meeting_times = [[1, 7], [5, 6], [7, 10], [9, 10]]

return number of non overlapping meeting times? => {[5, 6], [7,10]} = 2
"""