"""
Questions:
1. each row sorted, each column sorted? yes
2. IF target not in matrix? return [-1, -1]
3. Are there duplicates? No

Examples:
Naive: Iterate over the entire matrix and return the indexes
Time: O(n * m), n => # rows, m => # cols
Space: O(1)

matrix = [
    0.1.2. 3.
	
0.	1 4 7  12 
1.	2 5 19 31 < lb = 2 ub = 31
2.	3 8 24 33
]
target = 19

Binary Search for [2, 5, 19, 31]
Time: O(n) + O(logm)
Space: O(1)


matrix = [
    0.1.2. 3.
	
0.	1 4 7  12 
1.	2 5 *19 31
2.	3 8 24 33
]   
target = 19

Start from bottom left or top right and start search
Time: O(n + m)
Space: O(1)
"""

def search_matrix(matrix, target):
    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target: return [row, col]
        if matrix[row][col] < target: col += 1
        else: row -= 1
    
    return [-1, -1]