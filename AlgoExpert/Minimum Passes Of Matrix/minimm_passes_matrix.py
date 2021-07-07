"""
Questions:
1. A number 0 can convert negative to positive? No
2. What if it is not possible to convert all -ves? return -1
3. Is the input matirx mutable? yes

Examples:
   0.  1.  2.  3.  4.
0. 0  -1  -3   2   0
1. 1, -2, -5, -1, -3
2. 3,  0,  0, -4, -1

init = 
 -> 
cur_queue = [(0, 3), (1, 0), (2, 0)]
next_queue = []
   0.  1.  2.  3.  4.
0. 0  -1  -3   2   0
1. 1, -2, -5, -1, -3
2. 3,  0,  0, -4, -1


cur_queue = [(1, 0), (2, 0)]
next_queue = [(0, 2), (1, 3)]
   0.  1.  2.  3.  4.
0. 0  -1   3   2   0
1. 1, -2, -5,  1, -3
2. 3,  0,  0, -4, -1

cur_queue = [(2, 0)]
next_queue = [(1, 1), (0, 2), (1, 3)]
   0.  1.  2.  3.  4.
0. 0  -1   3   2   0
1. 1,  2, -5,  1, -3
2. 3,  0,  0, -4, -1

cur_queue = []
next_queue = [(1, 1), (0, 2), (1, 3)]
   0.  1.  2.  3.  4.
0. 0  -1   3   2   0
1. 1,  2, -5,  1, -3
2. 3,  0,  0, -4, -1

iter += 1

cur_queue = [(1, 1), (0, 2), (1, 3)]
next_queue = []
   0.  1.  2.  3.  4.
0. 0  -1   3   2   0
1. 1,  2, -5,  1, -3
2. 3,  0,  0, -4, -1

continue...

Time: O(W x H)
Space: O(W x H)
"""
from collections import deque
def change_value(row, col, matrix):
    if not(0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])) or matrix[row][col] >= 0: return False
    matrix[row][col] *= -1
    return True

def minimum_passes(matrix):
    cur_q, next_q = deque([]), deque([])
    nbrs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    itrs = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0: cur_q.appendleft((i, j))

    while cur_q:
        row, col = cur_q.pop()
        
        for nb in nbrs:
            nb_row, nb_col = row + nb[0], col + nb[1]
            if change_value(nb_row, nb_col, matrix): next_q.appendleft((nb_row, nb_col))

        if not cur_q: 
            cur_q, next_q = next_q, cur_q
            itrs += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0: return -1
    
    return itrs - 1