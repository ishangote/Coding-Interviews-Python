# 317. Shortest Distance from All Buildings

## Problem Statement

> You are given an `m x n` grid grid of values `0`, `1`, or `2`, where:
>
> - each 0 marks an empty land that you can pass by freely,
> - each 1 marks a building that you cannot pass through, and
> - each 2 marks an obstacle that you cannot pass through.
>
> You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.
>
> Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return `-1`.
>
> The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
>
> The distance is calculated using Manhattan Distance, where distance `(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|`.

> Constraints:
>
> - m == grid.length
> - n == grid[i].length
> - 1 <= m, n <= 50
> - grid[i][j] is either 0, 1, or 2.
> - There will be at least one building in the grid.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/14/buildings-grid.jpg)

```
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
```

Example 2:

```
Input: grid = [[1,0]]
Output: 1
```

Example 3:

```
Input: grid = [[1]]
Output: -1
```

## Solution

1. Identify Buildings

- First, iterate through the grid and collect all building positions.

2. Multi-Source BFS for Each Building

- Perform BFS from each building to compute:
  - distance_grid[row][col]: Sum of distances from all buildings.
  - reach_grid[row][col]: Count of buildings that can reach this cell.
- Only process empty land (0) in each BFS.
- Use empty_land marker to differentiate visited levels.

3. Select Minimum Distance Cell

- Iterate through all cells.
- Find the minimum distance_grid[row][col] where reach_grid[row][col] matches the total number of buildings.

4. Edge Cases

- If an empty cell cannot reach all buildings, return -1.

## References:

- https://youtu.be/yjHXS2w_IvY?si=6W_IRAGqXriByIYz
