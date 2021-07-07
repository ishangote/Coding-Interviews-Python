"""
Questions:
1. Length: number of edges
2. root None? return 0

Examples:
root = 
        1
    2       3

path = 2 -> 1 -> 3 (number of edges = 2)

root = 
            1 
           /  \
          3    2
         / \
        7   4
       /     \
      8       5
     /         \
    9            6
 
path = 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
ans = 6

diameter = lheight + rheight + 1
max_diam = max(left_diam, right_diam, diameter)

            1
           /  \
          3    2
         / \
        7   4
       /     \
      8       5
     /         \
    9           6

    

node = 
    1
2       None

height(1) = 1 + max(height(2), height(None))
          = 1 + max(0, 0) = 1

node = 
        1
    2       3

"""
def get_height(node):
    if not node: return 0
    return 1 + max(get_height(node.left), get_height(node.right))
    
def diameter(root):
    if not root: return 0
    
    lheight = get_height(root.left)
    rheight = get_height(root.right)
    
    root_diameter = lheight + rheight

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(root_diameter, ldiameter, rdiameter)