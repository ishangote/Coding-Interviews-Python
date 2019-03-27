#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.


"""
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3

=> DFS triggered for each 1 in grid and replacement of adjacent 1's with 0's

"""

import unittest
def num_islands(grid):

    island_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                island_count += 1
                dfs(grid, row, col)

    return island_count

def dfs(grid, r, c):
    if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1 or grid[r][c] != '1': return
    
    grid[r][c] = '0'
    dfs(grid, r - 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)
    dfs(grid, r + 1, c)



class TestNumIslands(unittest.TestCase):
    def test_all_0s_grid(self):
        grid = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
        self.assertEqual(num_islands(grid), 0)

    def test_all_1s_grid(self):
        grid = [["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]]
        self.assertEqual(num_islands(grid), 1)

    def test_generic_example(self):
        """
        ["1","1","1","1","0"]
        ["1","1","0","1","0"]
        ["1","1","0","0","0"]
        ["0","0","1","0","1"]
        """
        grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","1","0","1"]]
        self.assertEqual(num_islands(grid), 3)

if __name__ == '__main__': unittest.main()