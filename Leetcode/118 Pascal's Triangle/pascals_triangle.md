# 118. Pascal's Triangle

## Problem Statement

> Given an integer numRows, return the first numRows of Pascal's triangle.
> In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

```
                        1
                    1       1
                1       2       1
            1       3       3       1
        1       4       6       4       1
```

> Constraints:
>
> - 1 <= numRows <= 30

## Examples

Example 1:

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

Example 2:

```
Input: numRows = 1
Output: [[1]]
```

## Solution

Example 1:

```
Input:
rows = 1

Output: [[1]]
```

Example 2:

```
Input:
rows = 2

                        0
                0       1       0
            0       1       1       0


* Assume 0 if number above is not found

Output: [[1], [1, 1]]
```

Example 3:

```
Input:
rows = 3
                1
            1       1
        1       2       1


0: [1]
1: [1, 1]
2: [1, 2, 1] * number of elements in array = level + 1

Output:
  0      1        2
[[1], [1, 1], [1, 2, 1]]
```

Example 4:

```
Input:
rows = 4

0: [1]
1: [1, 1]
2: [1, 2, 1]
  ^ *              => if index is out of bounds, assume value to be 0
3: [1]

-----------
2: [1, 2, 1]
    ^  *
3: [1, 3]

-----------
2: [1, 2, 1]
       ^  *
3: [1, 3, 3]

-----------
2: [1, 2, 1]
       ^  *
3: [1, 3, 3]

-----------
2: [1, 2, 1]
          ^  *
3: [1, 3, 3, 1]
```
