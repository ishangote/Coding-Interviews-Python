"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Approach:
Since robot can move either down or right, there is only one path to reach the cells in the first row: right->right->...->right.
The same is valid for the first column, though the path here is down->down-> ...->down.
What about the "inner" cells (m, n)? To such cell one could move either from the upper cell (m, n - 1), or from the cell on the right (m - 1, n). 
That means that the total number of paths to move into (m, n) cell is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).

"""
def unique_paths(m, n):
    if m == 1 or n == 1: return 1
    itr = 0
    prev_row = [1] * n
    curr_row = [1] + [-1] * (n - 1)

    while itr < m - 1:
        for i in range(1, len(curr_row)):
            curr_row[i] = curr_row[i - 1] + prev_row[i]
        
        prev_row = curr_row
        curr_row = [1] + [-1] * (n - 1)
    
        itr += 1

    return prev_row[n - 1]

import unittest
class TestUniquePaths(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(unique_paths(3, 4), 10)
        self.assertEqual(unique_paths(3, 1), 1)

if __name__ == "__main__": unittest.main()