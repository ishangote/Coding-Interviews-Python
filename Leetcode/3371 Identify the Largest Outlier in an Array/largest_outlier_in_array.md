# 3371. Identify the Largest Outlier in an Array

## Problem Statement

> You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.
> An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.
> Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.
> Return the largest potential outlier in nums.

> Constraints:
>
> - 3 <= nums.length <= 10<sup>5</sup>
> - -1000 <= nums[i] <= 1000
> - The input is generated such that at least one potential outlier exists in nums.

## Examples

Example 1:

```
Input: nums = [2,3,5,10]
Output: 10
Explanation:
The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.
```

Example 2:

```
Input: nums = [-2,-1,-3,-6,4]
Output: 4
Explanation:
The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.
```

Example 3:

```
Input: nums = [1,1,1,1,1,5,5]
Output: 5
Explanation:
The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.
```

## Solution

```
nums =
                         sum of
                         special  (x7)
                         numbers
[x1, x2, x3, x4, x5, x6, x7, x8, x9]
 ---------------------------------- (total_sum)
 **********  ^   ****************** (total_sum - x4)
             possible
             outlier (x4)

x1 + x2 + x3 + x5 + x6 + x7 + x8 + x9 = total_sum - x4
x1 + x2 + x3 + x5 + x6 + x8 + x9 = x7

2 * x7 = (total_sum - x4)
x7 = (total_sum - x4) // 2

=> Iterate over nums, consider each number as outlier (eg. x4),
check if x7 is in nums and at a different index.
```

## References

- https://www.youtube.com/watch?v=1oHiy5M-XiU&ab_channel=AryanMittal
