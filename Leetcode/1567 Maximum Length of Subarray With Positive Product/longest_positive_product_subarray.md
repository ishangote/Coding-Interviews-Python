# 1567. Maximum Length of Subarray With Positive Product

## Problem Statement

> Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
> A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
> Return the maximum length of a subarray with positive product.

> Constraints:
>
> - 1 <= nums.length <= 10<sup>5</sup>
> - -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
```

Example 2:

```
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
```

Example 3:

```
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
```

## Brute Force Solution

```
Input:
nums =
[-1, -2, -3, 0, 1]
  ^
  *
product = -1

nums =
[-1, -2, -3, 0, 1]
  ^
      *
product = 2
max_length = 2

nums =
[-1, -2, -3, 0, 1]
  ^
          *
product = -6

nums =
[-1, -2, -3, 0, 1]
  ^
             *
product = 0

nums =
[-1, -2, -3, 0, 1]
  ^
                *
product = 0


nums =
[-1, -2, -3, 0, 1]
      ^
      *
product = -2


nums =
[-1, -2, -3, 0, 1]
      ^
          *
product = 6
max_length = 2
...

Time: O(n^2)
Space: O(1)

Output: 2

```

## Optimized Solution

```
Input:
nums =
[1, 2, 3, 4]        * CASE 1: All numbers positive  => return length of nums
Output:
4
```

```
Input:
nums =
[-1, 1, -2, -3, 2, -1]      * CASE 2: Number of -ve values is even => return length of nums
Output:
6
```

```
Input:
nums =
[2, -2, 3, 6, 4, -7, -9, 2, 9, 9]   * CASE 3: Number of -ve values is odd
     ^                *

=> Eliminate first -ve value

nums =
 0   1  2  3  4   5   6  7  8  9
[2, -2, 3, 6, 4, -7, -9, 2, 9, 9]
        ------------------------        * res = 8


=> Eliminate last -ve value

nums =
 0   1  2  3  4   5   6  7  8  9
[2, -2, 3, 6, 4, -7, -9, 2, 9, 9]
 ------------------                     * res = 6

Output:
8
```

```
Input:
nums =
[-2, 2, 0, 3, -3, -6, 0, 9, 8, -7, 6]   * CASE 4: Zero in between
 -----     ---------     -----------

* Split the array on zeroes and apply the same logic on the splits

  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
  ^
  *
count_negatives = 0


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
  ^
      *
count_negatives = 1
first_negative = 1 (idx)
last_negative = 1 (idx)


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
  ^
         *
count_negatives = 1
first_negative = 1 (idx)
last_negative = 1 (idx)

res = max((lastn - 1) - (0) + 1)
res = max((1 - 0), (2 - 1)) = 1


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
            ^
            *
count_negatives = 0
first_negative = -1
last_negative = -1


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
            ^
                *
count_negatives = 1
first_negative = 4
last_negative = 4


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
            ^
                    *
count_negatives = 2
first_negative = 4
last_negative = 5


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
            ^
                       *
count_negatives = 2
first_negative = 4
last_negative = 5
res = 5 - 3 + 1 = 3


  0   1  2  3   4   5  6  7  8   9  10
[ 2, -2, 0, 3, -3, -6, 0, 9, 8, -7, 6]
                          ^
                          *
count_negatives = 0
first_negative = -1
last_negative = -1

...

Output:
3
```

```
Input:
nums =
 0  1  2  3  4  5  6  7
[1, 2, 3, 4, 1, 3, 2, 1]
 ^
                         *

count_negatives = 0
first_negative = -1
last_negative = -1
res = 0
```
