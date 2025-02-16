# 162. Find Peak Element

## Problem Statement

> A peak element is an element that is strictly greater than its neighbors.
>
> Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
>
> You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
>
> You must write an algorithm that runs in O(log n) time.

> Constraints:
>
> - 1 <= nums.length <= 1000
> - -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
> - nums[i] != nums[i + 1] for all valid i.

## Examples

Example 1:

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

Example 2:

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

## Brute Force Solution

```
Constraint:
- `nums[i] != nums[i + 1]` for all valid i.

Case 1: Descending order

nums =
 0  1  2  3
[9, 5, 4, 3]
 ^
 * first element will be peak

Case 2: Ascending order
nums =
 0  1  2  3
[3, 4, 5, 9]
          *
          last element will be peak


Case 3: Peak is in mid
 0  1  2  3  4  5  6
[3, 4, 5, 9, 5, 4, 3]
 ^
 nums[i] < nums[i + 1]      => ascending


 0  1  2  3  4  5  6
[3, 4, 5, 9, 5, 4, 3]
    ^
    nums[i] < nums[i + 1]      => ascending


 0  1  2  3  4  5  6
[3, 4, 5, 9, 5, 4, 3]
       ^
       nums[i] < nums[i + 1]      => ascending


 0  1  2  3  4  5  6
[3, 4, 5, 9, 5, 4, 3]
          ^
          nums[i] > nums[i + 1]      => found peak

* Determine if the current idx is ascending or descending by looking at idx + 1
* If it is ascending, then peak must be towards the right
* If it is descending then the current number is peak or peak must be to the left
```

## Binary Search Solution

```
nums =
 0  1  2  3  4  5  6
[1, 2, 1, 3, 5, 6, 4]
 l        ^        h

nums[i] < nums[i + 1] => ascending slope => peak is to the right


nums =
 0  1  2  3  4  5  6
[1, 2, 1, 3, 5, 6, 4]
             l  ^  h

nums[i] > nums[i + 1] => descending slope => peak is current or to the left


nums =
 0  1  2  3  4  5  6
[1, 2, 1, 3, 5, 6, 4]
             l  h
             ^
nums[i] < nums[i + 1] => ascending slope => peak is to the right


nums =
 0  1  2  3  4  5  6
[1, 2, 1, 3, 5, 6, 4]
                l
                h
l == h: return mid

Output:
5
```

```
Input:
nums =
 0  1  2  3  4  5  6
[1, 2, 5, 3, 1, 2, 3]
 l        ^        h
nums[i] < nums[i + 1] => descending slope => peak is current or to the left


nums =
 0  1  2  3  4  5  6
[1, 2, 5, 3, 1, 2, 3]
 l  ^     h

nums[i] < nums[i + 1] => ascending slope => peak is to the right


nums =
 0  1  2  3  4  5  6
[1, 2, 5, 3, 1, 2, 3]
       l  h
       ^

nums [i] > nums[i + 1]  => peak is current or to the left


nums =
 0  1  2  3  4  5  6
[1, 2, 5, 3, 1, 2, 3]
       l
       h

l == h => return l

Output: 2
```

## Key Condition to Remember

1. If `nums[mid] < nums[mid + 1]`, move right (`lo = mid + 1`) → A peak exists on the right side.
2. Otherwise, move left (`hi = mid`) → A peak exists on the left or at mid.

## References

- https://leetcode.com/problems/find-peak-element/editorial/
