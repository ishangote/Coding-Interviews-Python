# 827. Making A Large Island

## Problem Statement

> You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
> Return the size of the largest island in grid after applying this operation.
> An island is a 4-directionally connected group of 1s.

> Constraints:
>
> - n == grid.length
> - n == grid[i].length
> - 1 <= n <= 500
> - grid[i][j] is either 0 or 1.

## Examples

Example 1:

```
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
```

Example 2:

```
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
```

Example 3:

```
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
```

## Solution

1. Compute Island Areas (compute_island_areas)

- Purpose: Identify all islands and assign them unique labels (2, 3, 4, ...), while computing their sizes.
- Method: Use DFS to explore islands and store their sizes in a dictionary {island_label: size}.
- Things to Remember:
  - Mark visited cells by changing their value to island_label.
  - Use a mutable list (area = [0]) to track size during recursion.
  - Start labeling islands from 2 (since 0 and 1 are already in use).

1. Calculate Maximum Island if a Water Cell is Converted (calculate_potential_island)

- Purpose: For every 0, check how many distinct islands it connects.
- Method:
  - Check its four neighbors.
  - Use a set (visited) to track already counted islands.
  - Sum up their sizes from island_area and add 1 (the converted water cell).
- Things to Remember:
  - Avoid double-counting islands (use a set for tracking).
  - If no 0 exists, return the largest island found (edge case).

3. Iterate Over Grid and Find Maximum Possible Island (making_a_large_island)

- Purpose: Try converting each 0 into 1 and calculate the max possible island.
- Method:
  - Iterate over all cells and apply calculate_potential_island.
  - Track the maximum possible size.
- Things to Remember:
  - If the entire grid is land (all 1s), return rows \* cols directly.
  - Edge case: If the entire grid is water (all 0s), return 1.

## References

- https://www.youtube.com/watch?v=pq61VNqXGvA&t=1067s&ab_channel=NeetCodeIO
