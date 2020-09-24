# Given the root node of a binary search tree, 
# return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

"""
Questions: 
1. Can there be duplicates? -> No
2. Negative numbers? -> Yes
3. How many nodes? -> 1000

Examples:
            10
        5         15
      3   7           18

l = 7, r = 15

sum(10, 7, 15) = 32

Traversing the tree: DFS vs BFS?

DFS: Can be implemented recursively
Time: O(n) n is number of nodes
Space: O(h) where h is max height of tree

BFS:
Time: O(n) n is number of nodes
Space: O(w) where w is max width of tree

            10*
        5       15
      3   7         18

l = 7, r = 15


"""

# Definition for a binary tree node.
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs_utility(self, node, lb, ub, ans):
    if lb <= node.val <= ub: ans[0] += node.val
    if node.left: self.dfs_utility(node.left, lb, ub, ans)
    if node.right: self.dfs_utility(node.right, lb, ub, ans)

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root: return 0
    ans = [0]
    self.dfs_utility(root, L, R, ans)
    return ans[0]