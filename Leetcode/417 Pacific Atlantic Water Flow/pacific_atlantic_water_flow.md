# 417. Pacific Atlantic Water Flow

## Problem Statement

> There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
>
> The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.
>
> The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
>
> Return a 2D list of grid coordinates result where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

> Constraints:
>
> - m == heights.length
> - n == heights[r].length
> - 1 <= m, n <= 200
> - 0 <= heights[r][c] <= 10<sup>5</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

Example 2:

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

## DFS Solution

```
   P        PACIFIC      A
   A     0.  1.  2.  3.  T
   C  0. 1   2   2   3   L
   I  1. 3   2   3   4   A
   F  2. 2   4   5   3   N
   I  3. 6   7   1   4   T
   C  4. 5   1   1   2   I
            ATLANTIC     C

Instead of starting at each co-ordinate and checking if we can reach Pacific
and Atlantic, we can traverse from Pacific and Atlantic as many co-ordinates
as possible, and return intersection.
```

## Approach Summary:

DFS Traversal:

- Start from all cells adjacent to the Pacific Ocean (first row & first column) and mark all reachable cells.
- Start from all cells adjacent to the Atlantic Ocean (last row & last column) and mark all reachable cells.
- Use a recursive DFS function (recursive_helper) to explore each cell.

Intersection of Reachable Cells:

- The final result consists of all the cells that can be visited from both the Pacific and Atlantic Oceans.

## References

- https://www.youtube.com/watch?v=s-VkcjHqkGI&ab_channel=NeetCode
