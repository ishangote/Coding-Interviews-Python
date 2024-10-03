# 441. Arranging Coins

## Problem Statement

> You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete. Given the integer n, return the number of complete rows of the staircase you will build.

> Constraints:
>
> - 1 <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

![Example 1](./arrangecoins1-grid.jpg)

```
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
```

Example 2:

![Example 1](./arrangecoins2-grid.jpg)

```
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
```

## Brute Force Solution

```
Input:
n = 5

1st row will have 1 coin    (n = 5 - 1 = 4)
2nd row will have 2 coins   (n = 4 - 2 = 2)
3rd row will have 3 coins   * Can not be filled since n = 2

* only row 1 and 2 can be filled completely

Output:
2
```

## Binary Search With Gauss' Formula

```
* Gauss' Formula to add numbers from 1 to n

n = [1, 2, 3, 4, 5, 6, 7, 8,....100]
     *                           *
            sum = 101

n = [1, 2, 3, 4, 5...,95, 96, 97, 98, 99, 100]
        *                             *
            sum = 101

n = [1, 2, 3, 4, 5...,95, 96, 97, 98, 99, 100]
           *                      *
            sum = 101

n = [1, 2, 3, 4, 5...,95, 96, 97, 98, 99, 100]
              *               *
            sum = 101

                 50        101
* total sum = (n / 2) * (n + 1)

* How many coins do we need to complete n rows = (n / 2) * (n + 1)
```

```
* n is the upper bound for the number of coin rows we can have
* lo = 1, hi = n


Input:
n = 5
1 2 3 4 5
l       h

m = 3

required_coins = 3 / 2 * 4 = 6      * Can not complete row 3


n = 5
1 2 3 4 5
l h

m = 1

required_coins = 1 / 2 * 2 = 1      * Can complete row 1


n = 5
1 2 3 4 5
  l
  h

m = 2

required_coins = 2 / 2 * 3 = 3      * Can complete row 2


n = 5
1 2 3 4 5
    l
  h

return h (since it will be at the last complete row)

Output:
2
```

## Math Solution

```
* number of coins in max complete row (R) must be equal to n
* Gauss' Formula

    R
    -   * (R + 1)       =       n
    2

* Solve for R
```
