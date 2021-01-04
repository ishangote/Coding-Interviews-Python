"""
Questions:
1. define closest value to target: num = 12 11 is closer or 13? there will only be one closest value 11/13 in BST
2. If target in BST? return target 
3. root == Null?

Examples:
root =
		2
	-1		4 (2)
	   	   3  7 (4)

target = 5

prev_closest = (2)
pass the prev closest
"""
def get_closer(a, target, b):
	return a if abs(a - target) <= abs(b - target) else b
# Recursive Approach
def dfs_helper(prev_closest, node, target):
	#Base Conditions
	if not node: return prev_closest
	if node.value == target: return node.value
	
	cur_closest = get_closer(prev_closest, target, node.value)
	
	if target < node.value:
		return dfs_helper(cur_closest, node.left, target)
	else:
		return dfs_helper(cur_closest, node.right, target)
	
def findClosestValueInBst(tree, target):
	assert(tree)
	return dfs_helper(tree.value, tree, target)

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
"""
n = number of nodes
Average Case: 
Time: O(logn)
Space: O(logn)

Worst Case: (completely unbalanced tree)
Time: O(n)
Space: O(n)
"""