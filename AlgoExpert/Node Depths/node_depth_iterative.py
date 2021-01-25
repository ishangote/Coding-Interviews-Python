"""
Questions:
1. root depth? 0
2. Is the tree balanced? Not always

Examples:

		1 (0)
	2(1)	3(1)
4(2)	
 	5(3)
	
BFS
queue = []
queue.deq() -> (1, 0)
ans = 0
queue.deq() -> (2, 1)
ans = 1
queue.deq() -> (3, 1)
ans = 2
queue.deq() -> (4, 2)
ans = 4
queue.deq() -> (5, 3)
ans = 7

"""
from collections import deque
def node_depth_iterative(root):
    #Input Validations
    if not root: return 0
    qu = deque([(root, 0)])
    ans = 0

    while qu:
        node, depth = qu.popleft()
        ans += depth
        if node.left: qu.append((node.left, depth + 1))
        if node.right: qu.append((node.right, depth + 1))

    return ans

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
"""
Time: O(n), n => number of nodes
Space: O(n)
"""