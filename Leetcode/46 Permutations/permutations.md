# 46. Permutations

## Problem Statement

> Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
> A permutation is a rearrangement of all the elements of an array.

> Constraints:
>
> - 1 <= nums.length <= 2
> - -10 <= nums[i] <= 10
> - All the integers of nums are unique.

## Examples

Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

Example 2:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

Example 3:

```
Input: nums = [1]
Output: [[1]]
```

## Backtracking Solution

```
Input:
nums = [1, 2, 3]

                                                    cur  decision_space
                                                     []  {1, 2, 3}
                                                          ^
                            /                           |                       \
                        [1] {2, 3}                   [2] {1,3}                  [3] {1,2}
                        /     \                       /      \                   /        \
                    [1,2] {3}  [1,3] {2}           [2,1]{3}  [2,3] {1}        [3,1] {2}   [3,2] {1}
                    /           \                   /           \              /            \
                  [1,2,3] {}    [1,3,2] {}      [2,1,3] {}      [2,3,1] {}  [3,1,2] {}      [3,2,1] {}

Output:
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]
```

## References

- https://www.youtube.com/watch?v=GCm7m5671Ps&t=556s&ab_channel=BackToBackSWE
