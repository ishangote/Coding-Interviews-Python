# 1891. Cutting Ribbons

## Problem Statement

> You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.
>
> For example, if you have a ribbon of length 4, you can:
>
> - Keep the ribbon of length 4,
> - Cut it into one ribbon of length 3 and one ribbon of length 1,
> - Cut it into two ribbons of length 2,
> - Cut it into one ribbon of length 2 and two ribbons of length 1, or
> - Cut it into four ribbons of length 1.
>
> Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.
>
> Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.

> Constraints:
>
> - 1 <= ribbons.length <= 10<sup>5</sup>
> - 1 <= ribbons[i] <= 10<sup>5</sup>
> - 1 <= k <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
```

Example 2:

```
Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
```

Example 3:

```
Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
```

## Binary Search Solution

1. Key observations:

- We need to find the maximum possible length for k ribbons of equal length obtained from the given ribbons array.
- If it’s not possible to obtain k ribbons of the same length, return 0.

2. Binary Search Setup:

- Define the search range:
  - low = 1: The smallest possible length of a ribbon segment.
  - high = max(ribbons): The longest possible ribbon segment length we could use.
- Use binary search on this range to identify the maximum length for which it’s feasible to create k ribbons.

```
Input:
ribbons = [7, 5, 9]
k = 4

lo = 1, hi = 9
mid = 5

Cut ribbons =>
Ribbon 7 ➔ 1 ribbon of length 5, remainder discarded
Ribbon 5 ➔ 1 ribbon of length 5
Ribbon 9 ➔ 1 ribbon of length 5, remainder discarded
* Total ribbons = 3 (less than k), we decrease length => hi = mid - 1

----------------------------------------

lo = 1, hi = 4
mid = 2
Ribbon 7 ➔ 3 ribbon of length 2, remainder discarded
Ribbon 5 ➔ 2 ribbon of length 2, remainder discarded
Ribbon 9 ➔ 4 ribbon of length 2, remainder discarded
* Total ribbons = 9 (more than k), we increase length => lo = mid + 1

----------------------------------------

lo = 3, hi = 4
mid = 3
Ribbon 7 ➔ 2 ribbon of length 3, remainder discarded
Ribbon 5 ➔ 1 ribbon of length 3, remainder discarded
Ribbon 9 ➔ 3 ribbon of length 3
* Total ribbons = 6 (more than k), we increase length => lo = mid + 1

----------------------------------------
lo = 4, hi = 4
Ribbon 7 ➔ 2 ribbon of length 3, remainder discarded
Ribbon 5 ➔ 1 ribbon of length 3, remainder discarded
Ribbon 9 ➔ 3 ribbon of length 3

Output:
4
```
