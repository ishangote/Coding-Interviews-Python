"""
Questions:
1. is input mutable? yes


Examples:
matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

Start with locations around the edges of matrix and do DFS to find locations connected to edges.
These are not to be removed
  
matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

Time: O(w x h), width and height of matrix
Space: O(w x h)
"""

def remove_islands_helper(locations, row, col, matrix):
    if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])) or (row, col) in locations or matrix[row][col] == 0: return
    locations.add((row, col))
    remove_islands_helper(locations, row - 1, col, matrix)
    remove_islands_helper(locations, row + 1, col, matrix)
    remove_islands_helper(locations, row, col - 1, matrix)
    remove_islands_helper(locations, row, col + 1, matrix)

def remove_islands(matrix):
    preserved_locations = set()

    for i in range(len(matrix)):
        for j in [0, len(matrix[0]) - 1]:
            if matrix[i][j] == 1: remove_islands_helper(preserved_locations, i, j, matrix)

    for i in [0, len(matrix) - 1]:
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1: remove_islands_helper(preserved_locations, i, j, matrix)

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 1 and (i, j) not in preserved_locations: matrix[i][j] = 0
    
    return matrix