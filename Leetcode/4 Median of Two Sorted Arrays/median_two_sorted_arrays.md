# 4. Median of Two Sorted Arrays

## Problem Statement

> Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.
>
> The overall run time complexity should be O(log (m+n)).

> Constraints:
>
> - nums1.length == m
> - nums2.length == n
> - 0 <= m <= 1000
> - 0 <= n <= 1000
> - 1 <= m + n <= 2000
> - -10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup>

## Examples

Example 1:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

Example 2:

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Binary Search Solution

#### Understanding the Median

If the combined length of the arrays is odd, the median is the middle element.
`Example: [4, 5, 7] → Median = 5`

If the combined length is even, the median is the average of the two middle elements.
`Example: [4, 5, 7, 10] → Median = (5 + 7) / 2 = 6`

#### Idea

We perform a binary search on the smaller array to find a partition such that all elements on the left partition are less than or equal to all elements on the right partition.

```
What is median?
Odd: [4, 5, 7]  * median = 5
Even: [4, 5, 7, 10]  * median = (5 + 7) / 2
```

```
CASE 1: Total numbers: EVEN

We can place a partition at any of the len(arr) possible positions between elements. Partition number indicates how many elements lie to the left.

      0.   1.   2.   3.   4.   5.
X ->  x1   x2   x3   x4   x5   x6
    ↑    ↑    ↑    ↑    ↑    ↑    ↑
    0    1    2    3    4    5    6

      0.   1.   2.   3.   4.   5.   6.   7.
Y ->  y1   y2   y3   y4   y5   y6   y7   y8
    ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑     ↑
    0    1    2    3    4    5    6    7     8

------------------------------------------------

      0.   1.   2.   3.   4.   5.
X ->  x1   x2   x3   x4   x5   x6
              ↑
              2 (2 elements to the left)

      0.   1.   2.   3.   4.   5.   6.   7.
Y ->  y1   y2   y3   y4   y5   y6   y7   y8
                             ↑
                             5

we need to select partitions s.t
partition_x + partition_y = [len(X) + len(Y)] // 2

i.e we can find partition_y from partition_x
partition_y = ([len(X) + len(Y)] // 2) - partition_x
partition_y = (14 / 2) - 2 = 5

------------------------------------------------

A partition is correct if all elements on the left (from both X and Y) are
less than or equal to all elements on the right (from both X and Y).

i.e

if =>
left_x = X[partition_x - 1]
right_x = X[partition_x]

left_y = Y[partition_y - 1]
right_y = Y[partition_y]

then =>
left_x <= right_y AND left_y <= right_x


Since total elements are even, the median is the avg of two middle numbers

=> median = avg(max(left_x, left_y), min(right_x, right_y))
```

```
CASE 2: Total numbers: ODD

      0.   1.   2.   3.   4.
X ->  x1   x2   x3   x4   x5
              ↑
              2 (2 elements to the left)

      0.   1.   2.   3.   4.   5.   6.   7.
Y ->  y1   y2   y3   y4   y5   y6   y7   y8
                        ↑
                        4
if =>
partition_x = 2
then =>
partition_y = [(len(X) + len(Y)) // 2] - partition_x
partition_y = (13 // 2) - 2 = 4

* so 6 total elements in the left partitions
* and 7 total elements in the right partitions

**We need to ensure that the left partition always has
one more element than the right partition when the total length is odd.**

* Hence use formula partition_y = [(total_length + 1) // 2] - partition_x

if =>
left_x = X[partition_x - 1]
left_y = Y[partition_y - 1]

=> median = max(left_x, left_y)
```

#### Pseudo Code

```
X, Y s.t len(X) <= len(Y)
total_length = len(X) + len(Y)

lo, hi = 0, len(X)  * partitions are bound by [0, len(X)], not indices!

X, Y such that len(X) <= len(Y)
total_length = len(X) + len(Y)

lo, hi = 0, len(X)  # partitions are bound by [0, len(X)], not indices!

while lo <= hi:
    partition_x = (lo + hi) // 2
    partition_y = (total_length // 2) - partition_x

    left_x = X[partition_x - 1] if partition_x > 0 else -∞
    right_x = X[partition_x] if partition_x < len(X) else ∞

    left_y = Y[partition_y - 1] if partition_y > 0 else -∞
    right_y = Y[partition_y] if partition_y < len(Y) else ∞

    if left_x <= right_y and left_y <= right_x:
        if total_length % 2 == 0:
            return avg(max(left_x, left_y), min(right_x, right_y))
        else:
            return max(left_x, left_y)

    elif left_x > right_y:
        hi = partition_x - 1  # move partition_x left (too many elements taken from X)
    else:
        lo = partition_x + 1  # move partition_x right
```

## References

- https://www.youtube.com/watch?v=LPFhl65R7ww&t=1196s&ab_channel=TusharRoy-CodingMadeSimple
