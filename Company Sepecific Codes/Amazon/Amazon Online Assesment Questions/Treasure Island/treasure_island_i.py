"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. 
There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. 
You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. 
The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

from collections import deque
def treasure_island_i(grid):
    if not grid: return -1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0)])
    ans = 0
    visited = set()
    visited.add((0, 0))

    while q:
        for i in range(len(q)):
            x, y = q.popleft()
            
            if grid[x][y] == 'X': return ans

            for dir in directions:
                new_x, new_y = x + dir[0], y + dir[1]
                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] != 'D':
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
            
        ans += 1

    return ans

import unittest
class TestTreasureIslandI(unittest.TestCase):
    def test_genric(self):
        grid = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
        self.assertEqual(treasure_island_i(grid), 5)

if __name__ == "__main__": unittest.main()