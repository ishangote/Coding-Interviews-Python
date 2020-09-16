"""
    3
   / \
  9  20
    /  \
   15   7

queue = [7, 15]

ans = [3, 9, 20]

"""
from collections import defaultdict
from collections import deque
def level_order(root):
    if not root: return []
    queue = deque([[root, 0]])
    order = defaultdict(list)
    
    while queue:
        node, level = queue.pop()
        order[level].append(node.val)
        if node.left: queue.appendleft([node.left, level + 1])
        if node.right: queue.appendleft([node.right, level + 1])
    
    return list(order.values())