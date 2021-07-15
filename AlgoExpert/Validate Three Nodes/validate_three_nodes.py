"""
Questions:
1. is node ancestor/decendant of itself? 
2. Any input node None? No
3. It is a BST? Yes
4. Parent pointer for each node? No 
5. Are there duplicate values? Maybe


Examples:
root = 	
			 5
		   /   \
		  2	    7
	  	 / \   /  \
	    1   4 6    8
	   /   /
	  0   3
	  
node1 = 5
node2 = 2
node3 = 3

Find ancestory of node 2: 
	Search from node1 -> True
	Search from node3 -> False

If no ancestor: return False

Is decendant node3? 
	Search from node 2 for node 3 -> True

If not decendant: return False

Time: O(d), d => depth of tree
Space: O(d)
"""
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_ancestor(ancestor, node):
    if not ancestor: return False
    if ancestor == node: return True
    if node.value < ancestor.value:
        return is_ancestor(ancestor.left, node)
    return is_ancestor(ancestor.right, node)

"""NOT required..."""
# def is_decendant(decendant, node):
# 	if not node: return False
# 	if node == decendant: return True
# 	if decendant.value < node.value:
# 		return is_decendant(decendant, node.left)
# 	return is_decendant(decendant, node.right)
	
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    is_nodeOne_ancestor = is_ancestor(nodeOne, nodeTwo)
    is_nodeThree_ancestor = is_ancestor(nodeThree, nodeTwo)

    # XOR: (T, T) => F and (F, F) => F
    if not (is_nodeOne_ancestor ^ is_nodeThree_ancestor): return False

    if is_nodeOne_ancestor:
        return is_ancestor(nodeTwo, nodeThree)

    return is_ancestor(nodeTwo, nodeOne)