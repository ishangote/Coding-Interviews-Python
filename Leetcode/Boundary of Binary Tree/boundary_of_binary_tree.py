# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
# Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
# (The values of the nodes may still be duplicates.)
# Left boundary is defined as the path from root to the left-most node.
# Right boundary is defined as the path from root to the right-most node.
# If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. 
# Note this definition only applies to the input binary tree, and not applies to any subtrees.
# The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists.
# If not, travel to the right subtree. Repeat until you reach a leaf node.
# The right-most node is also defined by the same way with left and right exchanged.

"""
Questions:
1. If root is Null? -> return []
2. How many nodes in the BT? Can we use recursion? -> Yes
3. Are there any duplicates? -> Yes

Examples:

Input:
            -1
         4      9
          2    3
              0 5

        l         b          r
[-1,    4,     2, 0, 5,    3, 9]

populate_root() -> -1
populate_left() -> 4
populate_bottom() -> 2, 0, 5
populate_right() -> 3, 9

populate_left(node)
    if node leaf: return
    ans.add(node.val)
    if node.left: populate_left(node.left)
    elif node.right: populate_left(node.right)

populate_bottom(node):
    if node leaf: ans.append(node.val)
    if node.left: popoulate_bottom(node.left)
    if node.right: popoulate_bottom(node.right)

populate_right(node):
    if node leaf: return
    if node.right: populate_right(node.right)
    elif node.left: populate_left(node.left)
    ans.append(node.val)
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
Input:
    1
        2
       1

Expected:
[1 1 2]

Actual:
[1 1 2]
"""

"""
Time:
O(3n) ~ O(n)
Space:
O(n)
"""