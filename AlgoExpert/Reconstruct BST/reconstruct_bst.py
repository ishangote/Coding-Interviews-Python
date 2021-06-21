"""
Questions:
1. if preorder is empty? return None
2. Can preorder have duplicates? yes

Examples:
(Root - Left - Right)
preorder = 
 0	 1	2  3  4  5	 6 	 7
[10, 4, 2, 1, 5, 17, 19, 18]
     i

root = 10
"""
class BSTNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def reconstruct_tree_naive(preorder):
    if not preorder: return None
    root_val = preorder[0]
    right_subtree_idx = len(preorder)
    for idx, val in enumerate(preorder):
        if val > root_val: right_subtree_idx = idx
        break
    
    left_subtree = reconstruct_tree_naive(preorder[1:right_subtree_idx])
    right_subtree = reconstruct_tree_naive(preorder[right_subtree_idx:])

    return BSTNode(root_val, left_subtree, right_subtree)