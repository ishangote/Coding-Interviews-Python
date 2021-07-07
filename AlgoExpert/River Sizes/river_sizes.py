"""
Questions:
1. diagonal 1s? not river
2. is input mutable? yes

Examples:
matrix = [
	1 0 0 1 0
	1 0 1 0 0
	0 0 1 0 1
	1 0 1 0 1
	1 0 1 1 0
]
river_sizes = []

DFS, mark visited 1s

Time: O(n x m)
Space: O(n x m)
"""
def get_size(row, col, matrix):
    if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])) or matrix[row][col] == 0: return 0
    cur_size = 1
    matrix[row][col] = 0
    cur_size += (get_size(row + 1, col, matrix) + get_size(row - 1, col, matrix) + get_size(row, col + 1, matrix) + get_size(row, col - 1, matrix))
    return cur_size

def get_river_sizes(matrix):
    if not matrix or len(matrix[0]) == 0: return []
    river_sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                river_size = get_size(i, j, matrix)
                river_sizes.append(river_size)
    return river_sizes