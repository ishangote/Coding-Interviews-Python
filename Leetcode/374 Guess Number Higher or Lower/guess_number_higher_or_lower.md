# 374. Guess Number Higher or Lower

## Problem Statement

> We are playing the Guess Game. The game is as follows:
> I pick a number from 1 to n. You have to guess which number I picked.
> Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
>
> You call a pre-defined API `int guess(int num)`, which returns three possible results:
>
> - -1: Your guess is higher than the number I picked (i.e. num > pick).
> - 1: Your guess is lower than the number I picked (i.e. num < pick).
> - 0: your guess is equal to the number I picked (i.e. num == pick).
>
> Return the number that I picked.

> Constraints:
>
> - 1 <= n <= 2<sup>31</sup> - 1
> - 1 <= pick <= n

## Examples

Example 1:

```
Input: n = 10, pick = 6
Output: 6
```

Example 2:

```
Input: n = 1, pick = 1
Output: 1
```

Example 3:

```
Input: n = 2, pick = 1
Output: 1
```

## Binary Search Solution

```
n = 10, guess = 6

lo = 1
hi = 10
mid = 5 -> guess will return +1 (my guess is lower)

lo = 6
hi = 10
mid = 8 -> guess will return -1 (my guess is higher)

lo = 6
hi = 7
mid = 6 -> correct guess (stop)
```
