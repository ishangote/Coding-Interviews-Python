# 136. Single Number

## Problem Statement

> Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
> You must implement a solution with a linear runtime complexity and use only constant extra space.
>
> Constraints:
>
> - 1 <= nums.length <= 3 x 10<sup>4</sup>
> - -3 x 10<sup>4</sup> <= nums[i] <= 3 x 10<sup>4</sup>
> - Each element in the array appears twice except for one element which appears only once.

## Examples

Example 1:

```
Input: nums = [2,2,1]
Output: 1
```

Example 2:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

Example 3:

```
Input: nums = [1]
Output: 1
```

## Brute Force

```
* For each number, iterate over the array to check if it appears again,
    if not return that number
* Time: O(n^2), where n => length of array
* Space: O(1)
```

## Optimized Time Solution

```
* Iterate over the array to build a counter hashmap
* Iterate over the hashmap to find the number with count = 1
* Time: O(n), where n => length of array
* Space: O(n)
```

## Optimized Time & Space Solution

```
* Each number appears twice except one number
* Application of the xor (exclusive OR) operator will cancel out the two duplicates
* The result will only have the single number that did not appear twice

Input:
nums = [1, 2, 4, 2, 1]
           ^
res = 1 xor 2 = 3


nums = [1, 2, 4, 2, 1]
              ^
res = 3 xor 4 = 7


nums = [1, 2, 4, 2, 1]
                ^
res = 7 xor 2 = 5


nums = [1, 2, 4, 2, 1]
                    ^
res = 5 xor 1 = 4

Output: 4


* Time: O(n)
* Space: O(1)
```
