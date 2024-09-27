# 401. Binary Watch

## Problem Statement

> A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
> For example, the below binary watch reads "4:51".

![binary watch img](https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg)

> Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.
>
> The hour must not contain a leading zero:
>
> - For example, "01:00" is not valid. It should be "1:00".
>
> The minute must consist of two digits and may contain a leading zero:
>
> - For example, "10:2" is not valid. It should be "10:02".

> Constraints:
>
> - 0 <= turnedOn <= 10

## Examples

Example 1:

```
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
```

Example 2:

```
Input: turnedOn = 9
Output: []
```

## Brute Force Solution

```
    Hour            H Led Lights
                    8   4   2   1
    ------------------------------
     0              0   0   0   0
     1              0   0   0   1
     2              0   0   1   0
     3              0   0   1   1
     4              0   1   0   0
     5              0   1   0   1
     6              0   1   1   0
     7              0   1   1   1
     8              1   0   0   0
     9              1   0   0   1
     10             1   0   1   0
     11             1   0   1   1


    Minute          M Led Lights
                    32  16  8   4   2   1
    --------------------------------------
     0              0   0   0   0   0   0
     1              0   0   0   0   0   1
     2              0   0   0   0   1   0
     3              0   0   0   0   1   1
     4              0   0   0   1   0   0
     5              ...
     6
     7
     8
     9
     10
     11
     ...
     59
```

```
Pseudo-code
* Iterate h from 0 to 11
    * Iterate m from 0 59
        * Convert h to binary
        * Convert m to binary
        * if number of 1 bits in h + number of 1 bits in m == input
            * add to result after formatting
```
