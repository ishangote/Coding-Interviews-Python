# 133. Clone Graph

## Problem Statement

> Given a reference of a node in a connected undirected graph.
>
> Return a deep copy (clone) of the graph.
>
> Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

> Test case format:
>
> For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
>
> An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
>
> The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

> Constraints:
>
> - The number of nodes in the graph is in the range [0, 100].
> - 1 <= Node.val <= 100
> - Node.val is unique for each node.
> - There are no repeated edges and no self-loops in the graph.
> - The Graph is connected and all nodes can be visited starting from the given node.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

Example 3:

```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

## BFS (Iterative) Solution

### Approach:

1. Edge Case Check: If the input node is None, return None.
2. Initialize Structures:

- Create a hash map (hm) to store original nodes as keys and their corresponding copies as values.
- Use a queue (q) to traverse the graph level by level (BFS).

3. Create the First Node Copy:

- Copy the given node and store it in hm.
- Push the original node into q to process its neighbors.

4. Process Nodes Using BFS:

- While q is not empty:
  - Pop a node and iterate over its neighbors.
  - If a neighbor is not cloned yet:
    - Create its copy, add it to hm, and push it into q.
    - Add the copied neighbor to the current node’s neighbor list.
  - If the neighbor is already cloned, just append it to the current node's neighbor list.

5. Return the Copy of the Given Node stored in hm.

### Key Points to Remember:

1. Use a hash map (hm) to track cloned nodes and avoid duplicate copies.
2. Use a queue (q) for BFS traversal to ensure all nodes are visited.
3. Order of operations matters: Clone nodes before adding them to the queue.

## References

- https://www.youtube.com/watch?v=vma9tCQUXk8&ab_channel=BackToBackSWE
