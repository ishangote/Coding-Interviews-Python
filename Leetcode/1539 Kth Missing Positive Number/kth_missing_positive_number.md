# 1539. Kth Missing Positive Number

## Problem Statement

> Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
> Return the kth positive integer that is missing from this array.
> Could you solve this problem in less than O(n) complexity?

## Examples

Example 1:

```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

Example 2:

```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```

## Key Observations

1. Understanding Missing Numbers

- The given array is sorted in strictly increasing order (no duplicates).
- A number is missing if it is not in `arr` but is within the range `[1, max(arr) + k]`.
- The missing numbers form a sequence that grows as we progress through the array.

2. Gap Between Expected and Actual Values

- If there were no missing numbers, the first `n` elements of a sorted array should be [1, 2, 3, ..., n].
- The expected value at index `i` should be `i + 1`.
- The actual value at `i` is `arr[i]`.
- The number of missing values before `arr[i]` is: `missing_count=arr[i]-(i+1)`
- If missing_count at `i` is greater than or equal to k, the kth missing number is somewhere before `arr[i]`.

## One Pass Solution

```
1. Iterate num from [1, len(arr) + k + 1)
2. If num != arr[idx], increment missing count, else increment idx and increment num
3. Stop processing when missing count becomes k
3. Time Complexity: O(n) since we iterate through arr and count missing numbers.

Initialize:
missing_count = 0
num = 1

Input:
k = 2
arr =
 0  1  2  3  4  5  6
[1, 2, 3, 7, 9]
             ^
num = 5
missing_count = 2
```

## Binary Search Solution

1. Initialize the `lo` and `hi` pointers:

- `lo = 0` (left bound of the array)
- `hi = len(arr)` (right bound of the array). This is crucial because by setting `hi = len(arr)`, we include the possibility that the Kth missing number is greater than the largest element in the array.

2. Binary Search Loop (`while lo < hi`):

- The middle index mid is calculated as` (lo + hi) // 2`.
- The difference between `arr[mid]` and its index is compared with `k`:
- If `arr[mid] - (mid + 1)` is greater than or equal to `k`, we move the `hi` pointer to `mid` because the missing numbers up to this point include the Kth missing number.
- Otherwise, we move the `lo` pointer to `mid + 1`, as the missing number lies after this point.

3. Return the result:

- The final result is `lo + k`, as `lo` represents the position where the Kth missing number is found in the sequence.

## References

- https://leetcode.com/problems/kth-missing-positive-number/?envType=company&envId=facebook&favoriteSlug=facebook-six-months
