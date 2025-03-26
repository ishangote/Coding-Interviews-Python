# 31. Next Permutation

## Problem Statement

> A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
>
> - For example, for arr = [1,2,3], the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.
>
> The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
>
> - For example, the next permutation of `arr` = `[1,2,3]` is `[1,3,2]`.
> - Similarly, the next permutation of `arr` = `[2,3,1]` is `[3,1,2]`.
> - While the next permutation of `arr` = `[3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.
>
> Given an array of integers nums, find the next permutation of nums.
>
> The replacement must be in place and use only constant extra memory.

> Constraints:
>
> - 1 <= nums.length <= 100
> - 0 <= nums[i] <= 100

## Examples

Example 1:

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

Example 2:

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

Example 3:

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

## Brute Force Solution

- Generate all possible permutations of the array `O(n!)` and find the next lexicographical permutation.
- This is highly inefficient for larger arrays.

## Optimized Solution

Instead of generating all permutations, we identify the next lexicographical order using these steps:

Step 1: Find the Pivot

- Start from the rightmost element and find the **first decreasing element** (pivot).
- This is the point where the order starts breaking from the right.
- If no pivot is found, the array is already the last permutation (reverse it to get the first permutation).

Step 2: Find the Successor

- Find the **smallest element in the right section that is larger than the pivot**.
- Swap them to get a slightly larger number.

Step 3: Reverse the Suffix

- The remaining right part is in descending order, so reverse it to get the next smallest order.

## Variation (Find Previous Permutation)

Differences:

- Pivot: Find the first element (from the right) that is larger than its next element.
- Predecessor: Instead of finding the smallest element greater than the pivot,
  find the largest element that is smaller than the pivot.
- Reverse: As before, reverse the suffix to get the highest order for that section.

## References

- https://www.youtube.com/watch?v=quAS1iydq7U&ab_channel=BackToBackSWE
- https://www.youtube.com/watch?v=v5Fz177Ihow&ab_channel=CodingwithMinmer
