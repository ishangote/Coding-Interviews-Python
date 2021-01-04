"""
Examples: 
root =
		2 (2)
	-1		4 (2)
	   	   3  7 (4)
		   
target = 5

Use stack:
stack = []

stack.pop() -> (2, 2)
stack.pop() -> (4,2)
stack.pop() -> (7, 4)
"""
def get_closer(a, target, b):
	return a if abs(a - target) <= abs(b - target) else b

# Iterative Approach
def findClosestValueInBst(tree, target):
	assert(tree)
	stack = [(tree, tree.value)]
	
	while stack:
		node, prev_closest = stack.pop()
		if node.value == target: return node.value
		
		cur_closest = get_closer(prev_closest, target, node.value)
		if target < node.value and node.left: 
			stack.append((node.left, cur_closest))
		elif node.right:
			stack.append((node.right, cur_closest))
	
	return cur_closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
Average Case:
Time: O(logn)
Space: O(logn)

Worst Case:
Time: O(n)
Space: O(n)
"""