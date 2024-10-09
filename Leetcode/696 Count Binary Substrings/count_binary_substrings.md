# 696. Count Binary Substrings

## Problem Statement

> Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
>
> Substrings that occur multiple times are counted the number of times they occur.

> Constraints:
>
> - 1 <= s.length <= 10<sup>5</sup>
> - s[i] is either '0' or '1'.

## Examples

Example 1:

```
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
```

Example 2:

```
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
```

## Brute Force Solution

A brute force approach would involve checking every possible substring of the input string s, and for each substring, checking if:

- It contains an equal number of 0's and 1's.
- The 0's and 1's are grouped consecutively.

```
Steps:
1. Generate all possible substrings.
2. For each substring, check if:
      - The number of 0's equals the number of 1's.
      - All the 0's are grouped together, and all the 1's are grouped together.
```

## Optimization

```
* For a valid substring eg. "000011" can be broken down 2 times to form further valid substrings (since count of 1's is 2)
* i.e 0011, 01

* So in the above case there are 4 0's 2 1's. The number of substrings = min (4, 2) = 2


Input:
s = 001110

* consecutive count =
[2, 3, 1]   => 2 0's -> 3 1's -> 1 0


* res = min (2, 3) + min (3, 1) = 2 + 1 = 3

```
