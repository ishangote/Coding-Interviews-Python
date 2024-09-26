# 367. Valid Perfect Square

## Problem Statement

> Given a positive integer num, return true if num is a perfect square or false otherwise.
> A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
> You must not use any built-in library function, such as sqrt.

> Constraints:
>
> - 1 <= num <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: num = 16
Output: true
Explanation: We return true because 4 \* 4 = 16 and 4 is an integer.
```

Example 2:

```
Input: num = 14
Output: false
Explanation: We return false because 3.742 \* 3.742 = 14 and 3.742 is not an integer.
```

## Binary Search Solution

```
* The square root of a number is less than or equal to n // 2 and greater than 1
* Binary search to find the number
```
