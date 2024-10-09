# 671. Second Minimum Node In a Binary Tree

## Problem Statement

> Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
>
> Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
>
> If no such second minimum value exists, output -1 instead.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 25].
> - 1 <= Node.val <= 2<sup>31</sup> - 1
> - root.val == min(root.left.val, root.right.val) for each internal node of the tree.

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)

```
Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
```

Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)

```
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
```

## DFS Solution

```
Input:
root =
        5
      /   \
     7     5
          / \
         5   6

* We can not add number '4' to the above tree at any position while following the rule:
* node.val = min(node.left.val, node.right.val)

* root will always hold the minimum number of all nodes
* We need to traverse node to check if root.val < node.value < smallest seen so far

root =
        5
      /   \
     7     5
          / \
         5   6

res = inf
smallest = 5

root =
        5* 5 < 5 < inf  => No
      /   \
     7     5
          / \
         5   6


        5
      /   \
     7*    5        5 < 7 < inf => update res = 7
          / \
         5   6


        5
      /   \
     7     5 *  5 < 5 < 7   => No
          / \
         5   6


        5
      /   \
     7     5
          / \
         5   6
         *      5 < 5 < 7 => No

        5
      /   \
     7     5
          / \
         5   6*      6 < 6 < 7 => res = 6
```
