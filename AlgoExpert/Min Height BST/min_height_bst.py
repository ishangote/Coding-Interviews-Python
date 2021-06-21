"""
Questions:
1. if array is empty? return None
2. Duplocates? Yes
3. Is input array sorted? No
4. Is input array mutable? yes

Examples:
[10, 4, 5, 1, 3]

one possible BST:
	root = 
			10
		 5
	  4
	1
	  3
	
	height = 4

BST inorder gives sorted array = [1, 3, 4, 5, 10] where root is mid element
										^
root = get_node([1, 3, 4, 5, 10]) ... 4
root.left = get_node([1, 3]) ... 1
	root.left = get_node([]) ... None
	root.right = get_node([3]) ... 3
root.right = get_node([5, 10]) ... 5
	root.left = get_node([]) ... None
	root.right = get_node([10]) ... 10

return root = 
		4
	1		5
  N	  3   N	   10
  
(Balanced BST) min height
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(lo, hi, array):
    if hi < lo: return None
    mid = (lo + hi) // 2
    root = BSTNode(array[mid])
    root.left = construct_tree(lo, mid - 1, array)
    root.right = construct_tree(mid + 1, hi, array)
    return root

def min_height_bst(array):
    return construct_tree(0, len(array) - 1, array)

"""
Time: O(n)
Space: O(n)
"""