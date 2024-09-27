# 422. Valid Word Square

## Problem Statement

> Given an array of strings words, return true if it forms a valid word square.
> A sequence of strings forms a valid word square if the kth row and column read the same string, where `0 <= k < max(numRows, numColumns)`.

> Constraints:
>
> - 1 <= words.length <= 500
> - 1 <= words[i].length <= 500
> - words[i] consists of only lowercase English letters.

## Examples

Example 1:

![example 1 img](https://assets.leetcode.com/uploads/2021/04/09/validsq1-grid.jpg)

```
Input: words = ["abcd","bnrt","crmy","dtye"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.
```

Example 2:

![example 2 img](https://assets.leetcode.com/uploads/2021/04/09/validsq2-grid.jpg)

```
Input: words = ["abcd","bnrt","crm","dt"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crm".
The 4th row and 4th column both read "dt".
Therefore, it is a valid word square.
```

Example 3:

![example 3 img](https://assets.leetcode.com/uploads/2021/04/09/validsq3-grid.jpg)

```
Input: words = ["ball","area","read","lady"]
Output: false
Explanation:
The 3rd row reads "read" while the 3rd column reads "lead".
Therefore, it is NOT a valid word square.
```

## Solution

```
Input:
words = ["abcd","bnrt","crmy","dtye"]

* Construct the grid

grid = [
      0 1 2 3
   0 [a b c d]
   1 [b n r t]
   2 [c r m y]
   3 [d t y e]
]

grid[r][c] = grid[r`][c`]

r c    r c
0 0 == 0 0
0 1 == 1 0
0 2 == 2 0
0 3 == 3 0

1 0 == 0 1
1 1 == 1 1
...

* Check if all conditions satisfy
* Note: We don't need to construct the grid since we can simply iterate on the strings

Output: True
```

```
Input:
words = ["abcd","bnrt","crm","dt"]

* Construct the grid

grid = [
      0 1 2 3  <- c
   0 [a b c d]
   1 [b n r t]
   2 [c r m  ]
   3 [d t    ]
]

grid[r][c] = grid[r`][c`]

r c    r c
0 0 == 0 0
0 1 == 1 0
0 2 == 2 0
0 3 == 3 0

1 0 == 0 1
1 1 == 1 1
1 2 == 2 1
1 3 == 3 1

2 0 == 0 2
2 1 == 1 2
2 2 == 2 2
* Will not go to 2, 3

...

* Check if all conditions satisfy
* Note: We don't need to construct the grid since we can simply iterate on the strings

Output: False
```
