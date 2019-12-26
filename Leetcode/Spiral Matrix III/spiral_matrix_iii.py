"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
Now, we walk in a clockwise spiral shape to visit every position in this grid. 
Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 
Eventually, we reach all R * C spaces of the grid.
Return a list of coordinates representing the positions of the grid in the order they were visited.

Example 1:
Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]



    0   1   2   3   4   5   

0   30  25  16  7   8   9
1   29  24  15  6   1   2
2   28  23  14  5   4   3
3   27  22  13  12  11  10
4   26  21  20  19  18  17



                            SPIRAL ORDER STEPS: => 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8....

                                    3
                                  ______
                                2|  __
                                 |____|1
                                    2

"""

def spiral_matrix_iii(R, C, r0, c0):
    #          E        S       W       N
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dir_idx = 0     #   1       2       3
    #Every EVEN(2, 4, 6, 8, ...) steps we change increment (1 1, 2 2, 3, 3, ...)
    steps, increment = 1, 1

    ans = [[r0, c0]]

    while len(ans) < R * C:
        for i in range(increment):
            r0 += dirs[dir_idx][0]
            c0 += dirs[dir_idx][1]

            if r0 < R and r0 > -1 and c0 < C and c0 > -1:
                ans.append([r0, c0])
        # Very important changing direction using mod to stay in the bounds
        dir_idx = (dir_idx + 1) % 4

        if steps % 2 == 0:
            increment += 1
        
        steps += 1

    return ans

import unittest
class TestSpiralMatrixIII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(spiral_matrix_iii(5, 6, 1, 4), [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])
        self.assertEqual(spiral_matrix_iii(1, 4, 0, 0), [[0,0],[0,1],[0,2],[0,3]])

if __name__ == "__main__": unittest.main()