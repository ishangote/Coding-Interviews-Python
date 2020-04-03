"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder: return None
    
    root = BTNode(preorder[0])
    pivot = inorder.index(root.val)
    
    root.left = buildTree(preorder[1 : pivot + 1], inorder[:pivot])
    root.right = buildTree(preorder[pivot + 1:], inorder[pivot + 1:])
    
    return root

# TESTING
# --------------------------------------------------

from collections import deque
def level_order(root):
    ans = []
    q = deque([(root, 0)])
    if not root: return []
    
    while q:
        node, level = q.pop()
        if len(ans) <= level: ans.append([])
        ans[level].append(node.val)
        
        if node.left: q.appendleft((node.left, level + 1))
        if node.right: q.appendleft((node.right, level + 1))
            
    return ans

import unittest
class TestConstructBinaryTreeFromInorderPreorder(unittest.TestCase):
    def test_construct_bt(self):
        self.assertEqual(level_order(buildTree([3,9,20,15,7], [9,3,15,20,7])), [[3], [9, 20], [15, 7]])

if __name__ == "__main__": unittest.main()