# 62. Unique Paths

## Problem Statement

> There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e.,` grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
>
> Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
>
> The test cases are generated so that the answer will be less than or equal to 2 \* 10<sup>9</sup>.

> Constraints:
>
> - 1 <= m, n <= 100

## Examples

Example 1:

```
Input: m = 3, n = 7
Output: 28
```

Example 2:

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Top Down Recursion with Memoization Solution

```
Base Case:
- number of ways to reach (m - 1, n - 1) from (m - 1, n - 1) is 1
- number of ways to reach outside grid is 0

Recursion:
- number of ways to reach (m - 1, n - 1) from (row, col) =
    - number of ways to reach (m - 1, n - 1) from (row, col + 1) +
    - number of ways to reach (m - 1, n - 1) from (row + 1, col)

Memoization:
- HashMap with (row, col)
```

## Dynamic Programming Solution

```
Initialization:
- Create a 2D DP table `dp` of size (m × n).
- Set `dp[i][0] = 1` for all `i` (only one way to reach locations on first column (move down)).
- Set `dp[0][j] = 1` for all `j` (only one way to reach locations on first row (move right)).

Transition:
- For each cell (i, j) from (1,1) to (m-1, n-1):
  - `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
  - Number of ways to reach (i, j) is sum of:
    - Ways to reach from the top (`dp[i-1][j]`)
    - Ways to reach from the left (`dp[i][j-1]`)

Final Answer:
- Return `dp[m-1][n-1]`
```

## Dynamic Programming Space Optimization Solution

```
Optimization:
- Instead of storing a full `m × n` table, store only two 1D arrays:
  - `prev_row` stores results of previous row.
  - `cur_row` stores results of current row.

Initialization:
- `prev_row = [1] * cols` (first row is all 1s).

Transition:
- Iterate over rows from `1` to `m-1`:
  - Initialize `cur_row = [1] + [0] * (cols - 1)`
  - For each column from `1` to `n-1`:
    - `cur_row[j] = prev_row[j] + cur_row[j-1]`
  - Update `prev_row = cur_row` after each row.

Final Answer:
- Return `prev_row[-1]`
```
