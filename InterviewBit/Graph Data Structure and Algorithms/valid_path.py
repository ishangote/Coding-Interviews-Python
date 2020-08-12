# There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.
# Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.
# Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.
"""
Input Format
1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO
   
Explanation:
    There is NO valid path in this case
"""
import math
from collections import deque
def distance_between_points(p, q):
    return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

def is_point_inside_circle(point, circles_params):
    circ_x, circ_y, radius = circles_params
    row, col = point
    for cur_x, cur_y in zip(circ_x, circ_y):
        if distance_between_points((row, col), (cur_x, cur_y)) < radius: return True

    return False

def get_legal_moves(position, rect_size):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
    ans = []

    for [row, col] in dirs:
        next_x, next_y = position[0] + row, position[1] + col
        if 0 <= next_x <= rect_size[0] and 0 <= next_y <= rect_size[1]: ans.append((next_x, next_y))
            
    return ans
	        
def bfs(queue, end, visited, circles_params):
    while queue:
        cur = queue.pop()
        visited.add(cur)
        if cur == end: return True
        legal_moves = get_legal_moves(cur, end)
        for (row, col) in legal_moves:
            if (row, col) not in visited and not is_point_inside_circle((row, col), circles_params) : queue.appendleft((row, col))

    return False

def valid_path(rect_x, rect_y, num_circles, radius, circ_x, circ_y):
    visited = set()
    circles_params = [circ_x, circ_y, radius]

    if radius == 0: return True
    if is_point_inside_circle((0, 0), circles_params) or is_point_inside_circle((rect_x, rect_y), circles_params): return False
    
    queue = deque([(0, 0)])
    return bfs(queue, (rect_x, rect_y), visited, circles_params)

import unittest
class TestValidPath(unittest.TestCase):
    def test_generic(self):
        #Radius Zero
        self.assertEqual(valid_path(41, 67, 5, 0, [17, 16, 12, 0, 40], [ 52, 61, 61, 25, 31]), True)
        self.assertEqual(valid_path(2, 3, 1, 1, [2], [3]), False)
        self.assertEqual(valid_path(2, 3, 1, 1, [1], [1]), True)

if __name__ == "__main__": unittest.main()