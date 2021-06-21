class BSTNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root, array):
    if not root: return []
    if root.left: inorder(root.left, array)
    array.append(root.value)
    if root.right: inorder(root.right, array)
    return array

def preorder(root, array):
    if not root: return []
    array.append(root.value)
    if root.left: preorder(root.left, array)
    if root.right: preorder(root.right, array)
    return array

def postorder(root, array):
    if not root: return []
    if root.left: postorder(root.left, array)
    if root.right: postorder(root.right, array)
    array.append(root.value)
    return array