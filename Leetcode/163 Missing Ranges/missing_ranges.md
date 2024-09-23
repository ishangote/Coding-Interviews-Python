# 163. Missing Ranges

## Problem Statement

> You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
>
> A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
>
> Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

> Constraints:
>
> - -109 <= lower <= upper <= 109
> - 0 <= nums.length <= 100
> - lower <= nums[i] <= upper
> - All the values of nums are unique.

## Examples

Example 1:

```
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
```

Example 2:

```
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
```

## Brute Force

```
Example 1

Input:
nums = [1, 5]
lower = 1
upper = 5

Numbers to be present in sorted order
[1, 2, 3, 4, 5]
    ^
          *

Algorithm:
* Initialize set of nums
* Iterate over the range ([1, 5])
* Utilize two pointers to find missing range

Output: [[2, 4]]
```

## Optimized Solution

```
Example 1

Input:
lower = 0
upper = 99
nums =

 0  1  2  3   4
[0, 1, 3, 50, 75]
    ^
       *
   [2, 2]


0  1  2  3   4
[0, 1, 3, 50, 75]
       ^
          *
      [4, 49]


0  1  2   3   4
[0, 1, 3, 50, 75]
          ^
              *
        [51, 74]

Add [76, 99] since the last number is 75 which is less than upper
```

```
Example 2

lower = -3
upper = 8
nums =
 0  1  2  3  4
[1, 2, 3, 5, 7]
    ^
 *
res = []


 0  1  2  3  4
[1, 2, 3, 5, 7]
       ^
    *
res = []


 0  1  2  3  4
[1, 2, 3, 5, 7]
          ^
       *
res = [[4, 4]]


 0  1  2  3  4
[1, 2, 3, 5, 7]
             ^
          *
res = [[4, 4], [6, 6]]


 0  1  2  3  4
[1, 2, 3, 5, 7]
                ^
             *
res = [[4, 4], [6, 6], [8, 8], [-1, 0]] * Add out of bound missing ranges
```
