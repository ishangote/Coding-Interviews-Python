class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root, array):
    if not root: return []
    if root.left: inorder(root.left, array)
    array.append(root.value)
    if root.right: inorder(root.right, array)
    return array

def kth_largest_value_inorder(root, k):
    sorted_vals = inorder(root, [])
    return sorted_vals[len(sorted_vals) - k]