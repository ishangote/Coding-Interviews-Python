# There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
# Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.
"""
Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Example 4:
Input: points = [[1,2]]
Output: 1

Example 5:
Input: points = [[2,3],[2,3]]
Output: 1
 
Constraints:
0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1
"""

"""
Questions:
1. Are the points sorted by start? -> No
2. Does the arrow stop? How many baloons can be burst by a single arrow? -> all in its way

Examples:

[[10,16],[2,8],[1,6],[7,12]]
sort by end of the baloon.
[[1,6],[2,8],[7,12],[10,16]]

1------6
  2--------8
         7------12
             10------16
The number of baloons burst by one arrow are determined by the end co-ordinates.

Time: O(nlogn)
Space: O(n) for sort
"""
def min_arrows(points):
    assert 0 <= len(points) < 104
    assert all(-231 <= points[i][0] < points[i][1] <= 231 - 1 for i in range(len(points)))

    if not points: return 0
    arrows = 1
    points.sort(key = lambda x: x[1])
    first_end = points[0][1]
    for point in points[1:]:
        if point[0] <= first_end: continue
        arrows += 1
        first_end = point[1]
    return arrows
    
if __name__ == "__main__":
    number_of_balloons = int(input("Enter number of balloons: "))
    points = []
    for itr in range(number_of_balloons):
        point = input("Enter the co-ordinates seperated by space: ")
        point = [int(p) for p in point.split()]
        points.append(point)
    
    print("Arrows: ", min_arrows(points))