"""
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). 
If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.

Sample Input :
   0. 1. 2.
0.[1, 0, 0],
1.[1, 0, 0],
2.[1, 9, 1]]

Sample Output :
3

Questions:
1. Where does the robot start? [0, 0]
2. Robot can move diagonals? No

Shortest Distance => BFS
Init:
queue = 
[]
 ---->

cur = (0, [0, 0])
cur = (1, [1, 0])
cur = (2, [2, 0])
cur = (3, [2, 1]) == 9 => return 3
"""

from collections import deque
def demolition_robot(grid):
    if not grid or not grid[0]: return -1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, [0, 0])])
    while queue:
        (dist, loc) = queue.pop()
        if grid[loc[0]][loc[1]] == 9: return dist
        
        for dir in directions:
            new_row, new_col = loc[0] + dir[0], loc[1] + dir[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 0:
                queue.appendleft((dist + 1, [new_row, new_col]))
    
    return -1


import unittest
class TestDemolitionRobot(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(3, demolition_robot([[1, 0, 0],[1, 0, 0], [1, 9, 1]]))
        self.assertEqual(5, demolition_robot([[1,1,1,1], [0,1,1,1], [0,1,0,1], [1,1,9,1], [0,0,1,1]]))

if __name__ == "__main__": unittest.main()