# 958. Check Completeness of a Binary Tree

## Problem Statement

> Given the root of a binary tree, determine if it is a complete binary tree.
>
> In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far > left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 100].
> - 1 <= Node.val <= 1000

## Examples

Example 1:

![alt text](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

## Level Order Traversal

Key Intuition:

- We use a queue to traverse the tree level by level, starting from the root.
- As we traverse the tree, we look for any `None` nodes. The first time we encounter a `None` node, it signifies that we've reached a node that could have potential empty child nodes, which is acceptable for a complete binary tree as long as the subsequent nodes are all `None` (i.e., no nodes should appear after the first `None` node).
- If we encounter any `non-None` nodes after having already seen a `None` node, it means the tree is not complete, and we return False.
