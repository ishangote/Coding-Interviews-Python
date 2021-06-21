"""
Reverse Inorder Solution!

Examples:
root = 
		10 
	8		  15 (visit = 3 = k)
  		   11	  17 (visit = 1)
			     15 (visit = 2)

k = 3 (third largest number)
ans = 15
"""
def reverse_inorder(root, array, k):
    if root.right: reverse_inorder(root.right, array, k)
    if len(array) == k: return array
    array.append(root.value)
    if len(array) < k: 
        if root.left: reverse_inorder(root.left, array, k)
    
    return array

def kth_largest_value_reverse_inorder(root, k):
    vals = reverse_inorder(root, [], k)
    return vals[-1]