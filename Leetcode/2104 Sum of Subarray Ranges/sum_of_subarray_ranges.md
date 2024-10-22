# 2104. Sum of Subarray Ranges

## Problem Statement

> You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
> Return the sum of all subarray ranges of nums.
> A subarray is a contiguous non-empty sequence of elements within an array.

> Constraints:
>
> - 1 <= nums.length <= 1000
> - -109 <= nums[i] <= 10<sup>9</sup>

> Follow-up: Could you find a solution with O(n) time complexity?

## Examples

Example 1:

```
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
```

Example 2:

```
Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
```

Example 3:

```
Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
```

## Brute Force Solution

```

* Compute all subarrays of a nums   => Time: O(n^2)
* Iterate over subarrays to find range  => Time: O(n^2) => (n(n+1)) / 2 subarrays

Input:
nums = [1, 2, 3]
        ^
        *               range = 0

nums = [1, 2, 3]
        ^
           *               range = 1

nums = [1, 2, 3]
        ^
              *               range = 2

nums = [1, 2, 3]
           ^
           *               range = 0

nums = [1, 2, 3]
           ^
              *               range = 1

nums = [1, 2, 3]
              ^
              *               range = 0

Output: 4
```

## Optimized Solution

```
Input:
nums = [3]
Output:
0
```

```
Input:

num =
[1, 4, 3, 2]

subarrays =
[1]                 range = 0                (1 - 1)
[1, 4]                  range = 3            (4 - 1)
[1, 4, 3]                   range = 3        (4 - 1)
[1, 4, 3, 2]                    range = 3    (4 - 1)
[4]                 range = 0                (4 - 4)
[4, 3]                  range = 1            (4 - 3)
[4, 3, 2]                   range = 2        (4 - 2)
[3]                 range = 0                (3 - 3)
[3, 2]                  range = 1            (3 - 2)
[2]                 range = 0                (2 - 2)
                                              ^   *

                                              ^ => subarray maximums
                                              * => subarray minimums

=> res = sum subarray maximums - sum subarray minimums
=> res = sum(1, 4, 4, 4, 4, 4, 4, 3, 3, 2) - sum (1, 1, 1, 1, 4, 3, 2, 3, 2, 2)
=> res = 13

Output:
13
```

## References

- https://www.youtube.com/watch?v=v0e8p9JCgRc&ab_channel=takeUforward
- [Sum of Subarray Minimums (Leetcode 907)](../907%20Sum%20of%20Subarray%20Minimums/sum_of_subarray_mins.md)
