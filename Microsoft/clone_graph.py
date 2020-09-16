"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity sake, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

  1     2      3    4
[[2,4],[1,3],[2,4],[1,3]]

node_map:
{
    1:1'
    2:2'
    3:3'
    4:4'
}
  1'     2'        3'      4'
[[2'4'] [1',3']  [2',4]    [1',3']]


Input: 1.neighbors = [2, 4]

  1     2      3    4
[[2,4],[1,3],[2,4],[1,3]]

node_map = {
    1:1'
    2:2'
    4:4'
    3:3'
}
stack = []
cur = 2

ans =
1  [2', 4']
4  [1', 3']
3' [2',4']
2' [1',3']
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

from collections import defaultdict
def clone_graph(node):
    if not node: return None
    node_map = defaultdict(Node)
    node_map[node] = Node(node.val)
    stack = [node]

    while stack:
        cur = stack.pop()
        for nbr in cur.neighbors:
            if nbr not in node_map:
                node_map[nbr] = Node(nbr.val)
                node_map[cur].neighbors.append(node_map[nbr])
                stack.append(nbr)
            else:
                node_map[cur].neighbors.append(node_map[nbr])
    
    return node_map[node]