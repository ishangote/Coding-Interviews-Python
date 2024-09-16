# 6. Zigzag Conversion

## Problem Statement

> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

> And then read line by line: "PAHNAPLSIIGYIR"
> Write the code that will take a string and make this conversion given a number of rows: `string convert(string s, int numRows);`

## Examples

Example 1:

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

Example 3:

```
Input: s = "A", numRows = 1
Output: "A"
```

## Solution

```
Input:
numRows = 4
s =
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G

ZigZag Pattern:
0    P       I       I
1    A    L  S    R  N
2    Y  A    H  I    G
3    P       I

0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
^
idx = 0
direction = "DOWN"
level = 0

res = [
    [P]  0
    []   1
    []   2
    []   3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
  ^
idx = 1
direction = "DOWN"
level = 1 => 2

res = [
    [P]  0
    [A]  1
    []   2
    []   3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
    ^
idx = 2
direction = "DOWN"
level = 2 => 3

res = [
    [P]  0
    [A]  1
    [Y]  2
    []   3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
      ^
idx = 3
direction = "DOWN" => "UP" (Reached the bottom => level = numRows - 1)
level = 3 => level - 1 = 2 (Since direction got flipped)

* If direction is UP then decrement level

res = [
    [P]  0
    [A]  1
    [Y]  2
    [P]  3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
        ^
idx = 4
direction = "UP"
level = 2 => 1

res = [
    [P]     0
    [A]     1
    [Y, A]  2
    [P]     3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
          ^
idx = 5
direction = "UP"
level = 1 => 0

res = [
    [P]     0
    [A, L]  1
    [Y, A]  2
    [P]     3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
            ^
idx = 6
direction = "UP" => "DOWN"
level = 0 => 1

res = [
    [P, I]      0
    [A, L]      1
    [Y, A]      2
    [P]         3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
              ^
idx = 7
direction = "DOWN"
level = 1 => 2

res = [
    [P, I]         0
    [A, L, S]      1
    [Y, A]         2
    [P]            3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                ^
idx = 8
direction = "DOWN"
level = 2 => 3

res = [
    [P, I]         0
    [A, L, S]      1
    [Y, A, H]      2
    [P]            3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                  ^
idx = 9
direction = "DOWN" => "UP"
level = 3 => 2

res = [
    [P, I]         0
    [A, L, S]      1
    [Y, A, H]      2
    [P, I]         3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                    ^
idx = 10
direction = "UP"
level = 2 => 1

res = [
    [P, I]         0
    [A, L, S]      1
    [Y, A, H, R]   2
    [P, I]         3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                       ^
idx = 11
direction = "UP"
level = 1 => 0

res = [
    [P, I]         0
    [A, L, S, I]   1
    [Y, A, H, R]   2
    [P, I]         3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                          ^
idx = 12
direction = "UP" => "DOWN"
level = 0 => 1

res = [
    [P, I, N]      0
    [A, L, S, I]   1
    [Y, A, H, R]   2
    [P, I]         3
]

------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R  I  N  G
                             ^
idx = 13
direction = "DOWN"
level = 1 => 2

res = [
    [P, I, N]         0
    [A, L, S, I, G]   1
    [Y, A, H, R]      2
    [P, I]            3
]

Join the string in each and return ans = "PINALSIGYAHRPI"
```

## References

- [Leetcode](https://leetcode.com/problems/zigzag-conversion/)
- [Youtube](https://www.youtube.com/watch?v=2NMMVnxV6lo&ab_channel=GregHogg)
