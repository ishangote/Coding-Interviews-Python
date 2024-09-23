# 191. Number of 1 Bits

## Problem Statement

> A set bit refers to a bit in the binary representation of a number that has a value of 1.
> Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)).
>
> Follow up: If this function is called many times, how would you optimize it?

> Constraints:
>
> - 1 <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.
```

Example 2:

```
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.
```

Example 3:

```
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
```

## Solution

```
Example:

Input:
n =
101101

* AND the input with 1 (000001) to find out if least significant bit is 1/0?

101101 n
  &
000001 m
______
000001

count = 1

* Right Shift (>>) n to do the operation on the next bit

101101 => 010110 n
            &
          000001 m
          ______
          000000

count = 1


010110 => 001011 n
            &
          000001 m
          ______
          000001

count = 2


001011 => 000101 n
            &
          000001 m
          ______
          000001

count = 3


000101 => 000010 n
            &
          000001 m
          ______
          000000


000010 => 000001 n
            &
          000001 m
          ______
          000001
count = 4


000001 => 000000 n  * when n becomes 0 => return count
            &
          000001 m
          ______
          000000
count = 4

* Con: Example; computation of 100000001 requires AND operation for all middle 0's                             -------

Output: 4
```
