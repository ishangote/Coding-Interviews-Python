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

1. Handle Empty Input:

- If nums is empty, return `[[lower, upper]]` since the entire range is missing.

2. Check Missing Range Before the First Element:

- If lower is less than `nums[0]`, add `[lower, nums[0] - 1]` to the result.

3. Find Missing Ranges Between Consecutive Elements:

- Iterate through nums and check if there is a gap between `nums[i-1]` and `nums[i]`.
- If the difference is more than 1, append the missing range `[nums[i-1] + 1, nums[i] - 1]`.

4. Check Missing Range After the Last Element:

- If upper is greater than `nums[-1]`, append `[nums[-1] + 1, upper]` to the result.
