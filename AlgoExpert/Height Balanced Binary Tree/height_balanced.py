"""
Questions: 
1. if not root: return True
2. height => max number of nodes in left/right subtree

Examples:
root = 
	1
	 \
	  2
	 /
	3

lheight = 0
rheight = 2
return False
	  
	  
root = 
	 1
	/ \
   5   2
	  /	\
	 3   4

For node 1,
lheight = 1
rheight = 2
return True


Time: O(n), n => number of nodes
Space: O(h), h => height of tree
"""
class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_height(node):
    if not node: return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def is_balanced(root):
    if not root: return True
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) > 1: return False

    return is_balanced(root.left) and is_balanced(root.right)