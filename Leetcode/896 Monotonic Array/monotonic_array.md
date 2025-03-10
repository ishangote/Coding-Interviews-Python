# 896. Monotonic Array

## Problem Statement

> An array is monotonic if it is either monotone increasing or monotone decreasing.
> An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
> Given an integer array nums, return true if the given array is monotonic, or false otherwise.

> Constraints:
>
> - 1 <= nums.length <= 10<sup>5</sup>
> - -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>

## Examples

Example 1:

```
Input: nums = [1,2,2,3]
Output: true
```

Example 2:

```
Input: nums = [6,5,4,4]
Output: true
```

Example 3:

```
Input: nums = [1,3,2]
Output: false
```

## Solution

1. Edge Case Handling:

- If the array has fewer than 2 elements, return True since an empty or single-element array is trivially monotonic.

2. Initialize direction:

- The direction variable is initially None and will store either "INCREASING" or "DECREASING" based on the first change in elements.

3. Single Pass Check:

- Iterate from the second element to the last.
- If arr[idx] is greater than arr[idx - 1], set direction to "INCREASING" (if not already set).
- If arr[idx] is smaller, set direction to "DECREASING".
- If a contradiction occurs (i.e., increasing followed by decreasing or vice versa), return False immediately.

4. Return Result:

- If the loop completes without contradictions, return True.
- Time Complexity: O(N) since we iterate through the array once, O(1) extra space since we use only a few variables.

## References

- https://leetcode.com/problems/monotonic-array/solutions/4102869/95-15-single-pass-check/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
