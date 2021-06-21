"""
Questions:
1. if root == None? True
2. Are values integers? yes
3. Can there be duplicates? yes

Examples:
root = 
							5 (-inf, inf)
		(-inf, 5) 2								7[5, inf)
	 (-inf,2) 3  	 x [2, 5)			  [5, 7) y		z [7, inf)
	 
Do DFS and adjust low_bound, high_bound
"""
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def check_bounds(node, low_bound, high_bound):
    if not node: return True
    if not (low_bound <= node.val < high_bound): return False
    return check_bounds(node.left, low_bound, node.val) and check_bounds(node.right, node.val, high_bound)

import sys
def validate_bst(root):
    return check_bounds(root, -sys.maxsize, sys.maxsize)