"""
Given a  2D Array:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .
"""

"""
Questions:
1. Can there be negative values in the matrix? -> yes


Example:
 
   0  1  2  3 4 5
0 -9 -9 -9  1 1 1
1  0 -9  0  4 3 2
2 -9 -9 -9  1 2 3
3  0  0  8  6 6 0
4  0  0  0 -2 0 0
5  0  0  1  2 4 0

mid_row =>[1, 4]
mid_col =>[1, 4]

iterate over all hourglasses by taking index of the middle element

Time: O(1)
Spac: O(1)
"""
import sys
def hourglassSum(arr):
    ans = -sys.maxsize
    dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1), (-1, 0), (1, 0)]
    for mid_row in range(1, 5):
        for mid_col in range(1, 5):
            cur_sum = arr[mid_row][mid_col]
            for d in dirs:
                row, col = mid_row + d[0], mid_col + d[1]
                cur_sum += arr[row][col]
            ans = max(cur_sum, ans)
    
    return ans