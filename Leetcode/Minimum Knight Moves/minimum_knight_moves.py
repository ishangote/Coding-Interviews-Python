# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
"""
Questions:
1. What if the solution does not exist? -> valid solution will always exist

Examples:
Brute Force:
Since we want to traverse on the gird and return the minimum number of steps, BFS seems to be a good option to try out.
Directions:
[[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

Time: O(k) where k is number of coordinates visited
Space: O(k)
"""
def bfs_helper(target, visited, que):
    while que:
        cur_cords, cur_steps = que.pop()
        visited.add(cur_cords)
        if cur_cords == target: return cur_steps
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        for dir in directions:
            row, col = cur_cords[0] + dir[0], cur_cords[1] + dir[1]
            if (row, col) in visited: continue
            que.appendleft([(row, col), cur_steps + 1])
    
from collections import deque
def min_knight_moves_naive(x, y):
    visited = set()
    que = deque([[(0, 0), 0]])
    return bfs_helper((x, y), visited, que)

if __name__ == "__main__":
    target_x = int(input("Enter x co-ordinate of the target position: "))
    target_y = int(input("Enter y co-ordinate of the target position: "))
    print("Smallest number of steps: ", min_knight_moves_naive(target_x, target_y))