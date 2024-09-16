# 217. Contains Duplicate

## Problem Statement

> Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

> Constraints:
>
> - 1 <= nums.length <= 105
> - -109 <= nums[i] <= 109

## Examples

Example 1:

```
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
```

Example 2:

```
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
```

Example 3:

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Brute Force

Algorithm:

1. For each number in nums iterate over rest of the array to check if it exists

## Solution 1

Algorithm:

1. Sort the array
2. Iterate over array and check if previous number is same as the current number

Time Complexity: O(nlog(n))
Space Complexity: O(1)

## Solution 2

Algorithm:

1. Iterate over nums and populate a set if the number does not exist
2. If the number already exists in set return true

Time Complexity: O(n)
Space Complexity: O(n)
