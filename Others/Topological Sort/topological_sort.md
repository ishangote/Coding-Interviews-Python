# Topological Sort

## Explanation

> Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge 𝑢 → 𝑣, vertex 𝑢 comes before 𝑣 in the ordering. Topological sorting is not possible if the graph contains cycles.

## Kahn’s Algorithm (DFS) Implementation

- Calculate the in-degree of all vertices (the number of incoming edges).
- Add all vertices with in-degree 0 to a stack/queue (DFS/BFS).
- Process the stack:
  - Pop a vertex from the stack, add it to the result.
  - Decrease the in-degree of its neighbors.
  - If the in-degree of a neighbor becomes 0, add it to the stack.

## Time Complexity Analysis

- Step 1 (Calculate in-degree): For each edge in the graph, update the in-degree of the destination node. This takes `𝑂(𝐸)`.
- Step 2 (Queue processing): Each vertex is added to and removed from the queue once, and for every vertex, we traverse its outgoing edges. This takes `𝑂(𝑉+𝐸)`.

`Total Time Complexity: 𝑂(𝑉+𝐸)`

Note: `𝑉` is the number of vertices, and `𝐸` is the number of edges in the graph.

## Space Complexity Analysis

`Total Space Complexity: 𝑂(𝑉 + 𝐸)`

## References

- https://www.youtube.com/watch?v=dis_c84ejhQ&t=4s&ab_channel=Jenny%27sLecturesCSIT
