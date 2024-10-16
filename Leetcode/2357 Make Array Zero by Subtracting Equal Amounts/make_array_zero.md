# 2357. Make Array Zero by Subtracting Equal Amounts

## Problem Statement

> You are given a non-negative integer array nums. In one operation, you must:
>
> - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
> - Subtract x from every positive element in nums.
>
> Return the minimum number of operations to make every element in nums equal to 0.

> Constraints:
>
> - 1 <= nums.length <= 100
> - 0 <= nums[i] <= 100

## Examples

Example 1:

```
Input: nums = [1, 5, 0, 3, 5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
```

Example 2:

```
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
```

## Min Heap Solution

1. Convert the array into a min-heap.
2. Repeatedly pop the smallest element, subtract it from all remaining elements, and increment the operation count. Skip zeroes during this process.

## HashSet Solution

- Use a hash set to store all unique positive numbers in the array.
- The number of operations required is equal to the number of unique positive numbers since each operation can reduce the array by one of these unique numbers.
