"""
        3
    9         20
      15   17     7
    3            1  5

stack1 = []                     l then r while pushing
stack2 = []              r then l while pushing

ans =
[3, 9, 20, 7, 17, 15, 3, 1, 5]

"""
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import defaultdict
def zig_zag(root):
    if not root: return  []
    stack1 = [[root, 0]]
    stack2 = []

    order = defaultdict(list)
    
    while stack1 or stack2:
        while stack1:
            node, level = stack1.pop()
            order[level].append(node.val)
            
            if node.left: stack2.append([node.left, level + 1])
            if node.right: stack2.append([node.right, level + 1])
        
        while stack2:
            node, level = stack2.pop()
            order[level].append(node.val)
            
            if node.right: stack1.append([node.right, level + 1])
            if node.left: stack1.append([node.left, level + 1])

    return list(order.values())


"""
     3
    1   2
     3 5

order = {
   0: [3]
   1: [1, 2]
   2: [5, 3]



}
s1 []
s2 []
"""