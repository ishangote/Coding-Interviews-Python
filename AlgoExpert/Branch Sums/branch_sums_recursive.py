"""
Questions:
1. Is it a BST? No

Examples:
		1  
	2		3
  4   5	       -2<


Depth First
ans = [7, 8, 2]
node = 3
accu_sum = 2

#Base Conditions:
1. Encounter leaf => append accu_sum to the ans
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_helper(node, accu_sum, ans):
	#Base Condition: if node leaf append to ans
	if not node.left and not node.right: 
		ans.append(accu_sum + node.value)

	if node.left:
		dfs_helper(node.left, accu_sum + node.value, ans)

	if node.right:
		dfs_helper(node.right, accu_sum + node.value, ans)
	
# Recursive Solution
def branchSumsRecursive(root):
	# Input validations
	if not root: return []
	ans = []
	dfs_helper(root, 0, ans)
	return ans

"""
Time: O(n), n is number of nodes
Space: O(n), implicit stack
"""