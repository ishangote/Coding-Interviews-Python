"""
Questions:
1. target and k are integers? Yes
2. tree is root node? Yes
3. parent pointer? No
4. Unique numbers? Yes

Examples:
root = 			1 
			   / \
			  2   3*
			 / \   \
			4   5   6
			       / \
				  7   8

If parent pointer were to exist: classic BFS problem
Hence create,
parents = {
	1: None
	2: 1`
	4: 2`
	5: 2`
	3: 1`
	6: 3`
	7: 6`
	8: 6`
}
return BFS(3`, 0)
"""
class BTNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def populate_parents(node, parent, parents):
    parents[node.value] = parent
    if node.left: populate_parents(node.left, node, parents)
    if node.right: populate_parents(node.right, node, parents)

from collections import deque
def findNodesDistanceK(root, target_value, k):
    parents = {}
    populate_parents(root, None, parents)

    target_parent = parents[target_value]
    if not target_parent: 
        target_node = root
    else:
        if target_parent.left and target_parent.left.value == target_value:
            target_node = target_parent.left
        else:
            target_node = target_parent.right
    
    #BFS
    res = []
    queue = deque([(target_node, 0)])
    visited = set()
    visited.add(target_node)

    while queue:
        node, distance = queue.pop()
        if distance == k: res.append(node.value)
        else:
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.appendleft((node.left, distance + 1))
            
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.appendleft((node.right, distance + 1))

            if parents[node.value] and parents[node.value] not in visited:
                visited.add(parents[node.value])
                queue.appendleft((parents[node.value], distance + 1))
    
    return res