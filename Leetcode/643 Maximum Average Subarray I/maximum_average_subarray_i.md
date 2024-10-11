# 643. Maximum Average Subarray I

## Problem Statement

> You are given an integer array nums consisting of n elements, and an integer k.
>
> Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

> Constraints:
>
> - n == nums.length
> - 1 <= k <= n <= 10<sup>5</sup>
> - -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

Example 2:

```
Input: nums = [5], k = 1
Output: 5.00000
```

## Brute Force Solution

```
* Compute subarrays as a list of all subarrays of nums with size k
* Calculate average of each subarray in subarrays
* Return the maximum average
```

## Sliding Window Solution

```
Input
k = 4
nums =
 0   1   2   3  4   5
[1, 12, -5, -6, 50, 3]
 -------------  current_sum = (1 + 12 + (-5) + (-6)) = 2
                avg = 2 / 4 = 0.5


 0   1   2   3  4   5
[1, 12, -5, -6, 50, 3]
    --------------  current_sum = 2 - 1 + 50 = 51 * as 1 moves out of the window
    and 50 gets added to the window
                    avg = 51 / 4 = 12.75


 0   1   2   3  4   5
[1, 12, -5, -6, 50, 3]
        -------------  current_sum = 51 - 12 + 3 = 42 * as 12 moves out of the window
    and 3 gets added to the window
                    avg = 42 / 4 = 10.5

* Keep track of result as maximum average found

Output: 12.75
```

```
Input
k = 4
nums [1, 2, 3, 4]
      ----------
                current_sum = 10
                average = 2.5

Output:
2.5
```
