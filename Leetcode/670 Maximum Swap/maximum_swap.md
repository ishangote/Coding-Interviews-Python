# 670. Maximum Swap

## Problem Statement

> You are given an integer num. You can swap two digits at most once to get the maximum valued number. Return the maximum valued number you can get.

> Constraints:
>
> - 0 <= num <= 10<sup>8</sup>

## Examples

Example 1:

```
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```

Example 2:

```
Input: num = 9973
Output: 9973
Explanation: No swap.
```

## Two Pass Solution

```
Input
digits =
 0. 1. 2. 3
[9, 5, 3, 6]
 ^
right_max =
[0, 3, 3, 3]         <- stores maximum number index to the right for each idx


digits =
 0. 1. 2. 3
[9, 5, 3, 6]
    ^                <- check if there exists a max number to the right, swap
    swap

Output:
[9, 6, 3, 5]

```

## One Pass Solution

```
Input:
num = 3729814932
      ^      ^

* MSD (most significant digit must have the max digit (from right)) i.e
* 3729814932   we should not swap these
  ^  ^

Output:
9729814332
```

```
Input:
num = 9783

* if max digit is already MSD, then the next digit can be swapped with next max digit (8)

Output:
9873
```

```
* Track the last occurrence of each digit:

       0 1 2 3 4 5 6 7 8 9
num = "3 7 2 9 8 1 4 9 3 2"
                         ^

hm: {
    0:
    1: 5
    2: 2 -> 9
    3: 0 -> 8
    4: 6
    5:
    6:
    7: 1
    8: 4
    9: 3 -> 7
}


       0 1 2 3 4 5 6 7 8 9
num = "3 7 2 9 8 1 4 9 3 2"
       ^

for each idx:
    for max_digit in 978..0:
        swap (idx, hm[9])

Approach
- Track the last occurrence of each digit: We store the last position of every digit (from 0 to 9) in an array, allowing us to know where the highest digits appear.
- Identify a potential swap: As we traverse the number, for each digit, we check if there's a larger digit appearing later. If we find one, we swap the two digits.
- Return the result: Once the optimal swap is performed (if any), return the new number. If no swap is needed, return the original number.
```

## References

- Two Pass: https://www.youtube.com/watch?v=4FZtJ8420m8&ab_channel=NeetCodeIO
- One Pass: https://leetcode.com/problems/maximum-swap/solutions/5922945/beats-100-00-step-by-step-breakdown/
