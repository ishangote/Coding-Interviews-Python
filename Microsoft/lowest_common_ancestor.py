"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

            3
    5               1
6       2       0       8
  7    4


lca(5, 4) -> 5
lca(7, 2) -> 5

lca(0, 2) -> 3


        2
    1       3
  4

lca (3, 4)

parent = 2
found_p = True
found_q = True

Base conditions:
    if not root: return None
    if root.val == p.val or root.val == q.val: return root


    3
1       2



"""
class BTNode:
    def __init__(sefl, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p. q):
    if not root: return None
    if root.val == p.val or root.val == q.val: return root

    left_search = lowest_common_ancestor(root.left, p, q)
    right_search = lowest_common_ancestor(root.right, p, q)

    if not left_search: return right_search
    if not right_search: return left_search
    return root 

"""
    3
2       1

lca(2, 1)

"""