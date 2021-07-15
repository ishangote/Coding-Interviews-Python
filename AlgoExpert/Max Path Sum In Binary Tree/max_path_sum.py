"""
Questions:
1. Path must pass from root? No
2. Integers (-ve) as values? yes
3. Can single node be in path? yes

Examples:
tree = 
			    1 
			  /	  \
		     2*	   3
		    / \	  / \
		   4   5 6	 7

# BS => Branch Sum
# MS => Max Path Sum (Tracks running max path sum accros tree)
# L/RBS => Left/Right Branch Sum
# L/RMS => left/Right Max path sum
mps(T):
	(LBS, LMS) = mps(T.left)
	(RBS, RMS) = mps(T.right)
	
	BS = max(T.value, T.value + max(LBS, RBS))
	MS = max(T.value, T.value + max(LBS, RBS), T.value + LBS + RBS, 
			 LMS, RMS)
	=> 
	MS = max(BS, T.value + LBS + RBS, LMS, RMS)
	
	return (BS, MS)

Time: O(n)
Space: O(logn)
"""
class BTNode:
	def __init__(self, value) -> None:
		self.value = value
		self.left = None
		self.right = None

def find_path_sums(node):
	if not node: return (0, -float('inf'))
	(left_branch_sum, left_max_path_sum) = find_path_sums(node.left)
	(right_branch_sum, right_max_path_sum) = find_path_sums(node.right)

	node_branch_sum = max(node.value, node.value + max(left_branch_sum, right_branch_sum))
	node_max_path_sum = max(node_branch_sum, node.value + left_branch_sum + right_branch_sum, left_branch_sum, right_branch_sum)

	return (node_branch_sum, node_max_path_sum)

def maxPathSum(root):
	branch_sum, max_path_sum = find_path_sums(root)
	return max_path_sum