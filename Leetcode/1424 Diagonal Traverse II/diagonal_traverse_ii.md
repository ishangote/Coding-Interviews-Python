# 1424. Diagonal Traverse II

## Problem Statement

> Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

> Constraints:
>
> - 1 <= nums.length <= 10<sup>5</sup>
> - 1 <= nums[i].length <= 10<sup>5</sup>
> - 1 <= sum(nums[i].length) <= 10<sup>5</sup>
> - 1 <= nums[i][j] <= 10<sup>5</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png)

```
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png)

```
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

## Hash Map Solution

```
    0   1   2   3   4
   ___________________
0.| 1 | 2 | 3 | 4 | 5 |
1.| 6 | 7 |   |   |   |
2.| 8 |   |   |   |   |
3.| 9 | 10| 11|   |   |
4.| 12| 13| 14| 15| 16|

* All elements along a diagonal share the same value of i + j
* Track the max_diagonal_key to not have to sort the hash map
* Iterate over the hash map and return results

diagonal_elements =
{
    8: [16]
    7: [15]
    6: [14]
    5: [13, 11]
    4: [12, 10, 5]
    3: [9, 4]
    2: [8, 7, 3]
    1: [6, 2]
    0: [1]
}
```

## BFS/Level Order Traversal Solution

```
Matrix:
  1   3   6
  2   5
  4   7

45° Rotation:
       1
    2     3
 4     5     6
    7

Steps:
1. Push the bottom cell first (remember to check that the next row has a valid column index).
2. Push the right cell second.
```

## References

- https://www.youtube.com/watch?v=URiyTWfIxPo&t=3s&ab_channel=CodingwithMinmer
