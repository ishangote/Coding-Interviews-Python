# Data Structure: Disjoint Set/Union Find

> Union by Rank & Path Compression

## Explanation

Disjoint sets, also known as disjoint-set data structures or union-find data structures, are a way to efficiently group elements into distinct, non-overlapping subsets. These sets are useful for solving problems involving grouping, connectivity, and partitioning.

## Implementation

```
Disjoint-set:

TreeNode:
rank    -> approximate depth, default 0
value   -> value of the node (x)
parent  -> pointer to the parent node, default to itself

Operations:
make_set(x):
- Creates a new set containing the single element x.

union(x, y):
- Combines two sets containing elements x and y into a single set.
- This operation may use union by rank or size to keep the data structure balanced.


find_set(x):
- Determines which set a particular element x belongs to.
- This operation often includes path compression, which flattens the structure of the tree to optimize future queries.

```

## Example

```
* Initially each element is in its own set
make_set(1) => 1 (rank = 0, parent = 1)
make_set(2) => 2 (rank = 0, parent = 2)
make_set(3) => 3 (rank = 0, parent = 3)
make_set(4) => 4 (rank = 0, parent = 4)
make_set(5) => 5 (rank = 0, parent = 5)
make_set(6) => 6 (rank = 0, parent = 6)
make_set(7) => 7 (rank = 0, parent = 7)


union(1, 2)

    1 (rank = 1)    * Increment rank for 1
  /
 2 (rank = 0)       * 2.parent = 1


union(2, 3)
    * find root of 2 => 1 (rank = 1)
    * 3 (rank = 0)
    * 1 will be the root of the new set, rank does not change

    1 (rank = 2)
   / \
  2   3 (0)


union(4, 5)

    1 (rank = 1)            4 (rank = 1)
   / \                     /
  2   3                   5 (0)


union(6, 7)

    1 (rank = 1)            4 (rank = 1)            6 (rank = 1)
   / \                     /                       /
  2   3                   5 (0)                   7 (0)



union(5, 6)
   * update parent of 6 to representative of the set 5 belongs to, i.e 4
   * rank of 4 will increment since we merged 2 nodes of same rank

    1 (rank = 1)           4 (rank = 2)
   / \                    / \
  2   3                  5   6
                            /
                           7


find(7) -> return 4
    * traverse from 7 to 4 using parent pointer
    * perform path-compression, so that future queries are optimized
    * decrement rank of 4

    4 (rank = 2)                 4 (rank = 1)
   / \                         / | \
  5   6             =>        5  7  6
     /
    7


union(3, 7)
    * representative of 3 = 1 (rank = 1)
    * representative of 7 = 4 (rank = 2), 4 will become rep of new set

              4 (rank = 2)
           / / \  \
          5 6   7  1
                  / \
                 2   3


find(2)
    * representative of 2 = 4
    * perform path compression, i.e 2.parent = 4

              4 (rank = 2)
           / / \  \  \
          5  6  7  1  2
                    \
                     3

```

## Time Complexity

With path compression and union by rank, the amortized time complexity for both _find_set_ and _union_ operations is nearly constant, specifically `𝑂(𝛼(𝑛))`, where 𝑛 is the number of elements, `𝛼(𝑛)` is the inverse Ackermann function (very slow-growing), i.e `𝛼(𝑛)` <= `4` for all practical purposes.

Hence, if we have `m` operations, time complexity to perform those would be `O(m * 𝛼(𝑛)) ~ O(m)`.

## Applications

1. Graph Algorithms:
   1. Detecting cycles in a undirected graph.
   2. Implementing Kruskal’s Minimum Spanning Tree algorithm.
2. Dynamic Connectivity Problems:
   1. Determining connected components in an undirected graph.
3. Clustering:
   1. Grouping data into clusters where each cluster is disjoint from others.

## References

- https://www.youtube.com/watch?v=ID00PMy0-vE&t=4s&ab_channel=TusharRoy-CodingMadeSimple
