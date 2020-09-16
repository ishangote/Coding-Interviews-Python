"""
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].


                2
    3
        4
    5       6
1

"""
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left  = None
        self.right = None

def populate_left(node, ans):
    if not node.left and not node.right: return

    ans.append(node.val)
    if node.left:
        populate_left(node.left, ans)
    elif node.right:
        populate_left(node.right, ans)

def populate_bottom(node, ans):
    if not node.left and not node.right:
        ans.append(node.val)
        return
    if node.left:
        populate_bottom(node.left, ans)
    if node.right:
        populate_bottom(node.right, ans)

def populate_right(node, ans):
    if not node.left and not node.right: return

    if node.right:
        populate_right(node.right, ans)
    elif node.left:
        populate_right(node.left, ans)
    ans.append(node.val)

def boundary_binary_tree(root):
    if not root: return []

    ans = [root.val]
    
    if root.left: populate_left(root.left, ans)
    if root.left or root.right: populate_bottom(root, ans)
    if root.right: populate_right(root.right, ans)

    return ans

"""
    1
        2
       1

Expected:
[1 1 2]

root = 1
Actual:
ans [1 1 2]
"""