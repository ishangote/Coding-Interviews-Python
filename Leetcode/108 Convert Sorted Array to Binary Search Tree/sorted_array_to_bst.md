# 108. Convert Sorted Array to Binary Search Tree

## Problem Statement

> A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
>
> Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

> Constraints:
>
> - 1 <= nums.length <= 104
> - -104 <= nums[i] <= 104
> - nums is sorted in a strictly increasing order.

## Examples

Example 1:

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

            0                               0
          /   \                           /   \
        -3     9            OR          -10    5
        /     /                           \     \
     -10     5                            -3     9

Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

## Solution

Example 1:

```
Input:
nums = [1]
Output:
    1
```

Example 2:

```
nums =
   0   1  2  3  4
[-10, -3, 0, 5, 9]
          ^

* Root will be at the the middle position

root = nums[0]
root.left => recursively calculate root for left half of the array
root.right => recursively calculate root for right half of the array
return root

* Base Case: if length of nums = 0 then return None

               0   1  2  3  4
            [-10, -3, 0, 5, 9] *return 0
               /            \
            0    1           3  4
          [-10, -3] *-10    [5, 9] *5
            /  \             /  \
                 1               4
         []    [-3] *-3    []   [9]*9
```
