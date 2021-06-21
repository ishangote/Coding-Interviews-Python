"""
Questions: 
1. For each node, swap its left node with corresponding right node
2. Inplace? yes

Examples:
root = 
        1
    2       

invert = 
        1
            2

root = 
        2
    1       3

invert = 
        2
    3       1

root =
        1<
    2       3
  4   5   6   7
8   9

invert = 
          1
      3        2
    7   6    5    4
                9   8

Time: O(n), n => number of nodes
Space: O(h), h => height of BT
"""

def invert_bt(root):
    if not root: return
    if not root.left and not root.right: return

    root.left, root.right = root.right, root.left

    invert_bt(root.left)
    invert_bt(root.right)

    return root    