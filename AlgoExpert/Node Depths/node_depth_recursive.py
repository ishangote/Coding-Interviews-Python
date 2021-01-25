"""
Examples:

DFS Recursive:
		1 (0)<
	2(1)	3(1)
4(2)	
 	5(3)
	
Base Conditions:
if not node: return 0

dfs(1, 0, ans = 0)
ans += 0 (0)
>
dfs(2, 1, ans = 0)
ans += 1 (1)
>
dfs(4, 2, ans = 1)
ans += 2 (3)
>
dfs(None, 3, ans = 3)
return
>
dfs(5, 3, ans = 3)
ans += 3 (6)
>
dfs(None, 4, ans = 6)
return
dfs(None, 4, ans = 6)
return
>
dfs(3, 1, ans = 6)
ans += 1 (7)
>
dfs(None, 2, ans = 7)
return
>
dfs(None, 2, ans = 7)
return
"""
def dfs_recursive(node, depth, ans):
    if not node: return
    ans[0] += depth
    dfs_recursive(node.left, depth + 1, ans)
    dfs_recursive(node.right, depth + 1, ans)
    return

def node_depth_recursive(root):
    ans = [0]	
    dfs_recursive(root, 0, ans)
    return ans[0]

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
Time: O(n)
Space: O(n)
"""