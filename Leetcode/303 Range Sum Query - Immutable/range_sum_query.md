# 303. Range Sum Query - Immutable

## Problem Statement

> Given an integer array nums, handle multiple queries of the following type:
> Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
>
> Implement the NumArray class:
>
> - NumArray(int[] nums) Initializes the object with the integer array nums.
> - int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

> Constraints:
>
> - 1 <= nums.length <= 10<sup>4</sup>
> - -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>
> - 0 <= left <= right < nums.length
> - At most 10<sup>4</sup> calls will be made to sumRange.

## Examples

Example 1:

```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

```

## Brute Force Solution

```
* Each time sumRange is called, we use a for loop to sum each individual element from index i to j.
* Time: O(n)
* Space: O(1)

```

## Caching Solution

```
* At initialization of nums, calculate and store the sum of all possible ranges.
* Initialization will take Time: O(n^2) but sumRange will take only Time: O(1)
```

## Optimization

```
                0   1   2   3   4   5
nums =        [-2,  0,  3, -5,  2, -1]
prefix_sums = [-2, -2,  1, -4, -2, -3] <- each index stores sum till that index (inclusive)


sumRange(1, 2) = prefix_sums[2] - prefix_sums[1 - 1] = 1 - (-2) = 3

sumRange(0, 2) = prefix_sums[2] = prefix_sums[0 - 1] = 1 - 0 = 1   * Handle index out of range => 0

...

```
