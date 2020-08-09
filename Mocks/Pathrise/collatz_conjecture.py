"""
start = 3, target = 7
[3, 10, 5, 14, 7]   

start = 4, target = 7
[]

start = 5, target = 7
[5, 14, 7]

start = 11, target = 7
[11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7]

start = 15, target = 7
[15, 44, 22, 11, 34, 17, 50, 25, 74, 37, 112, 56, 28, 14, 7]
"""
# BFS
from collections import deque
def collatz_conjecture(start, target):
    queue = deque([start])
    visited  = set()
    while queue:
        num = queue.pop()
        visited.add(num)
        if num == target: return True
        if num % 2 == 0:
            if num // 2 not in visited: 
                queue.appendleft(num // 2)
        else:
            if (3 * num) - 1 not in visited: queue.appendleft((3 * num) - 1)
            if (3 * num) + 1 not in visited: queue.appendleft((3 * num) - 1)

    return False