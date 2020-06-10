"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""
#Space: O(mxn)
def unique_paths_ii(grid):
    if not grid: return 0
    memo = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    memo[0][0] = 1 - grid[0][0]

    for i in range(1, len(grid)):
        memo[i][0] = memo[i-1][0] * (1 - grid[i][0])

    for i in range(1, len(grid[0])):
        memo[0][i] = memo[0][i-1] * (1 - grid[0][i])

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            memo[i][j] = (memo[i][j-1] + memo[i-1][j]) * (1 - grid[i][j])
    
    return memo[-1][-1]

import unittest
class TestUniquePathsII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(unique_paths_ii([[0,0,0], [0,1,0], [0,0,0]]), 2)

if __name__ == "__main__": unittest.main()