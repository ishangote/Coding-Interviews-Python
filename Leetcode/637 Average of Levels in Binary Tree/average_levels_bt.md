# 637. Average of Levels in Binary Tree

## Problem Statement

> Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
> - -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1

## Examples

![Example 1](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

## Level-order Traversal Solution

```
Input:
            3
          /   \
         9     20
              /  \
            15    7

level order traversal:
0 [3]       -> average = 3
1 [9 20]    -> average = 29 / 2 = 14.5
2 [15 7]    -> average = 22 / 2 = 11


queue = [(3, 0)]
res = []


queue = [(9, 1), (20, 1)]
res = [[3]]

queue = [(15, 2), (7, 2), (9, 1)]
res = [[3], [20]]

queue = [(15, 2), (7, 2)]
res = [[3], [20, 9]]

queue = [(15, 2)]
res = [[3], [20, 9], [7]]


queue = []
res = [[3], [20, 9], [7, 15]]

* flatten res with output
```
