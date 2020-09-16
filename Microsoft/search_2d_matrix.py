"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 16
Output: false

First Binary Search:
target = 33
l   m   h
1   10  23

Second Binary Search:
target

"""
def search_2d_matrix(matrix, target):
    if not matrix: return False

    #To find row
    lo, hi = 0, len(matrix) - 1
    target_row = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]: 
            target_row = mid
            break
        elif matrix[mid][0] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    #To find target
    lo, hi = 0, len(matrix[0]) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[target_row][mid] == target: return True
        elif matrix[target_row[mid] > target: hi = mid - 1
        else: lo = mid + 1
    return False


"""
target = 16
  0    1   2   3
0[1,   3,  5,  7],
1[10, 11, 16, 20],
2[23, 30, 34, 50]

lo = 1 hi = 2


"""
