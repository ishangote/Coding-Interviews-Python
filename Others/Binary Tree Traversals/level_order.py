# Definition for a binary tree node.
class BTNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def level_order(root):
    ans = []
    q = deque([(root, 0)])
    if not root: return []
    
    while q:
        node, level = q.pop()
        if len(ans) <= level: ans.append([])
        ans[level].append(node.val)
        
        if node.left: q.appendleft((node.left, level + 1))
        if node.right: q.appendleft((node.right, level + 1))
            
    return ans