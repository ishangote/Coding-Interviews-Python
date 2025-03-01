# 695. Max Area of Island

## Problem Statement

> You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
>
> The area of an island is the number of cells with a value 1 in the island.
>
> Return the maximum area of an island in grid. If there is no island, return 0.

> Constraints:
>
> m == grid.length
> n == grid[i].length
> 1 <= m, n <= 50
> grid[i][j] is either 0 or 1.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

Example 2:

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Meta Phone Screen Interview [02-2025]

> Follow Up: What are some practical limitations for this?

For a question like this in an interview, the interviewer is likely testing your ability to analyze the real-world constraints of your solution. Here are some practical limitations you could have discussed:

1. Stack Overflow (Recursion Depth)
   The recursive implementation relies on Python’s function call stack, which has a recursion depth limit (default is 1000 in CPython). If the grid has a large connected island, you may hit a recursion limit and get a RecursionError.
   Alternative: Convert the recursive DFS to an iterative approach using an explicit stack (BFS or DFS with a stack).
2. Memory Usage
   The visited set and recursion call stack consume extra memory. In the worst case (one large island), space usage is O(m \* n).
   Alternative: If modifying the input grid is allowed, mark visited cells by changing 1 to 0 instead of using a separate visited set.
3. Time Complexity in Worst Case
   The solution is O(m \* n) in the worst case, which is optimal for this problem, but if the grid is extremely large, processing time could still be a concern.
   Alternative: Parallelization could be considered for large-scale applications.
4. Grid Modification Limitations
   If modifying grid instead of using visited, there might be cases where the grid is immutable (e.g., read-only constraints in a database-backed system).
5. Handling Large Sparse Grids
   If the grid is very sparse (lots of 0s), scanning the entire grid could be inefficient.
   Alternative: If the grid is stored in a sparse format (e.g., only storing positions of 1s), a more efficient approach might be possible.
   What Would Be a Strong Response?
   If the interviewer asks this, you could say:

"One practical limitation of this approach is that it relies on recursion, which could cause a stack overflow if the island is very large. A better approach would be to use an iterative DFS or BFS. Additionally, the space complexity is O(m \* n) due to the visited set, which can be optimized by modifying the grid directly if allowed. If the grid is large, processing time could become a concern, and we might explore parallelization or sparse storage techniques."
