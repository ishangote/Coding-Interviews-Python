"""
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. 
Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.
Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 
4-directionally adjacent to the previous location.
It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.
If the task is impossible, return -1.

Examples:
input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011

Constraints:
[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer
"""
#BFS
from collections import deque
def shortest_cell_path(grid, sr, sc, tr, tc):
    q = deque([[sr,sc,0]])
    visited = set()
    while q:
        x, y, depth = q.pop()

        if x == tr and y == tc: return depth

        for (r, c) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r,c) not in visited and grid[r][c] == 1:
                q.appendleft([r, c, depth + 1])
                visited.add((r,c))

    return -1

import unittest
class TestShortestCellPath(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(shortest_cell_path([[1,1,1,1],[0,0,0,1],[1,1,1,1]], 0, 0, 2, 0), 8)
        self.assertEqual(shortest_cell_path([[1,1,1,1],[0,0,0,1],[1,0,1,1]], 0, 0, 2, 0), -1)
        self.assertEqual(shortest_cell_path([[0,1,0],[1,0,0],[1,0,1]], 2, 0, 1, 0), 1)

if __name__ == "__main__": unittest.main()