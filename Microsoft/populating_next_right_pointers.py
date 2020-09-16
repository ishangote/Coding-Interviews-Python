"""
            2
        1       3
      4   3    7

Breadth first search:

next = None
queue = []
            2 -> None

next = None
queue = [1, 3]
            2 -> None

next = 3
queue = [4, 3, 7]
            2 -> None
          1 -> 3 -> None


next = 7
queue = []
            2 -> None
          1 -> 3 -> None
         4->3  -> 7 -> None
"""
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

from collections import deque
def populating_next_right(root):
    if not root: return None

    queue = deque([root])

    while queue:
        next_node = None
        cur_len = len(queue)
        for i in range(cur_len):
            node = queue.pop()
            node.next = next_node
            next_node = node
            if node.right: queue.appendleft(node.right)
            if node.left: queue.appendleft(node.left)
    
    return root

"""
In                  Expected                Actual
None                None                    None

1                   1 -> None               1 -> None

    1               1 -> None               1->None  
2       3         2 -> 3                  2 -> 3->None

q=[]
nn = 2
"""