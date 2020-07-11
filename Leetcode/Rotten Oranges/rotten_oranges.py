"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

    0   1   2

0   2   1   1
1   1   1   0
2   0   1   2

init: q = [(0, 0), (2, 2)]

q.pop()
(0,0)
    0   1   2

0   2   2   1
1   2   1   0
2   0   1   2

q = [(2, 2), (0, 1), (1, 0)]

q.pop()
(2, 2)
    0   1   2

0   2   2   1
1   2   1   0
2   0   2   2

q = [(0, 1), (1, 0), (2, 1)]

q.pop()
(0, 1)
    0   1   2

0   2   2   2
1   2   2   0
2   0   2   2

q = [(1, 0), (2, 1)]

To keep track of one generation appendleft (-1, -1) after each generation
"""


from collections import deque
def rotten_oranges(grid):
    fresh_oranges = 0
    q = deque([])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                fresh_oranges += 1
            if grid[i][j] == 2:
                q.appendleft((i, j))
    
    q.appendleft((-1, -1))
    
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    ans = 0
    
    while q:
        i, j = q.pop()
        if i == -1:
            ans += 1
            if q:
                q.appendleft((-1, -1))
        
        else:
            for (x, y) in dirs:
                r = i + x
                c = j + y

                if r >= 0 and r <len(grid) and c >=0 and c <len(grid[0]) and grid[r][c] == 1:
                    fresh_oranges -= 1
                    grid[r][c] = 2
                    q.appendleft((r, c))

    return ans - 1 if fresh_oranges == 0 else -1

import unittest
class TestRottenOranges(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(rotten_oranges([[2,1,1],[1,1,0],[0,1,2]]), 2)

if __name__ == "__main__": unittest.main()
     