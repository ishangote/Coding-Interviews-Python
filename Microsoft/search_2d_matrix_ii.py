"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

target = 25
 
[1,   4,  7, 11, 15],
[2,   5,  8, 12, 19],
[3,   6,  9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]


-> move to right if want greater num
-> moe top if want smaller num

"""

def search_matrix(matrix, target):
    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target: return True
        elif matrix[row][col] < target: col += 1
        else: row -= 1

    return False