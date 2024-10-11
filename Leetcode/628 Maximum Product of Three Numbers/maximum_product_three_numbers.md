# 628. Maximum Product of Three Numbers

## Problem Statement

> Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

> Constraints:

> - 3 <= nums.length <= 10<sup>4</sup>
> - -1000 <= nums[i] <= 1000

## Examples

Example 1:

```
Input: nums = [1,2,3]
Output: 6
```

Example 2:

```
Input: nums = [1,2,3,4]
Output: 24
```

Example 3:

```
Input: nums = [-1,-2,-3]
Output: -6
```

## Sorting Solution

Time: O(nlogn)
Space: O(1)

```
Input:
nums = [2, 3, 1, 4, 5]

* sort nums
nums = [1, 2, 3, 4, 5]
              -------

Output:
3 * 4 * 5
```

```
Input:
nums = [-100, -99, -98, 4, 5]

* sort nums
nums = [-100, -99, -98, 4, 5]
        ---------          -

Output:
-100 * -99 * 5
```

- Two Cases: ` nums[-1] * nums[-2] * nums[-3] OR nums[0] * nums[1] * nums[-1]`

## Single Scan Solution

```
Input:
nums =
[2, 3, 1, 4, 5]

* Initialize
max1, max2, max3 = -inf


[2, 3, 1, 4, 5]
 ^
max1 = 2
max2 = -inf
max3 = -inf


[2, 3, 1, 4, 5]
    ^
max1 = 3
max2 = 2
max3 = -inf


[2, 3, 1, 4, 5]
       ^
max1 = 3
max2 = 2
max3 = 1


[2, 3, 1, 4, 5]
          ^
max1 = 4
max2 = 3
max3 = 2


[2, 3, 1, 4, 5]
             ^
max1 = 5
max2 = 4
max3 = 3

Output:
5 * 4 *3
```

```
Input:
nums = [5, -98, 4, -100, -99]

* Initialize
max1, max2, max3 = -inf
min1, min2 = inf

[5, -98, 4, -100, -99]
 ^

max1 = 5
max2 = -inf
max3 = -inf

min1 = 5
min2 = inf


[5, -98, 4, -100, -99]
     ^

max1 = 5
max2 = -98
max3 = -inf

min1 = -98
min2 = inf


[5, -98, 4, -100, -99]
         ^

max1 = 5
max2 = 4
max3 = -98

min1 = -98
min2 = 4


[5, -98, 4, -100, -99]
              ^

max1 = 5
max2 = 4
max3 = -98

min1 = -100
min2 = -98


[5, -98, 4, -100, -99]
                   ^

max1 = 5
max2 = 4
max3 = -98

min1 = -100
min2 = -99

Output:
-100 * -99 * 5
```
