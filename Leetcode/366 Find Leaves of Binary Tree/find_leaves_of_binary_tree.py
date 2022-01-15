"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

        1 (2)
      /  \
 (1) 2    3 (0)
    / \
(0)4   5 (0)

heights = {
    0: [4, 5, 3 ],
    1: [2]
    2: [1]
}

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]

Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter 
the order on which elements are returned.
"""
from collections import defaultdict

def get_heights(node, heights):
    if not node: return -1

    node_height = 1 + max(get_heights(node.left, heights), get_heights(node.right, heights))
    
    heights[node_height].append(node.value)
    return node_height

def find_leaves(root):
    if not root: return []
    heights = defaultdict(list)
    result = []

    get_heights(root, heights)

    max_height = max(heights.keys())
    for itr in range(0, max_height + 1):
        result.append(heights[itr])
    
    return result