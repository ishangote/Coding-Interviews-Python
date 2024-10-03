# 338. Counting Bits

## Problem Statement

> Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

> Constraints:
>
> - 0 <= n <= 10<sup>5</sup>

## Examples

Example 1:

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

Example 2:

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

## Brute Force Solution

```
* How to count number of 1's for binary?

n = 3

* Is Least significant bit 1/0? =>
           *
3 => 0 0 1 1
%       %
2       2
-    -------
1       1


n = n // 2 (3 // 2 = 1)

n = 1
           *
1 => 0 0 0 1
%    -------
2       2
-    -------
1       1

n = 1 // 2 = 0
```

## Dynamic Programming Solution

```
* Binary Representation
0 -> 0 0 0 0 [0]
1 -> 0 0 0 1 [1]
2 -> 0 0 1 0 [1]
3 -> 0 0 1 1 [2]

4 -> 0 1 0 0 [1]
       * ---        => most significant bit (*) is 1 but the other bits to the right repeat
5 -> 0 1 0 1
       * ---
6 -> 0 1 1 0
       * ---
7 -> 0 1 1 1
       * ---

8 -> 1 0 0 0
     * _____       => most significant bit has shifted, offset is 8


num_bits[4] = 1 + num_bits[0]   n - 4
num_bits[5] = 1 + num_bits[1]   n - 4
num_bits[6] = 1 + num_bits[2]   n - 4
num_bits[7] = 1 + num_bits[2]   n - 4


* offsets = [1, 2, 4, 8, ...] => binary number
* Base case => num_bits[0] = 0
* num_bits[n] = 1 + num_bits[n - offset]
```

## References

- https://leetcode.com/problems/counting-bits/description/
- https://www.youtube.com/watch?v=RyBM56RIWrM&t=4s&ab_channel=NeetCode
