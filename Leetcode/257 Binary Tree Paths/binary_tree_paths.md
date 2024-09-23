# 257. Binary Tree Paths

## Problem Statement

> Given the root of a binary tree, return all root-to-leaf paths in any order.
> A leaf is a node with no children.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 100].
> - -100 <= Node.val <= 100

## Examples

Example 1:

```
        1
       / \
      2   3
       \
        5

Input: root = [1, 2, 3, null, 5]
Output: ["1->2->5","1->3"]
```

Example 2:

```
Input: root = [1]
Output: ["1"]
```

## DFS Solution

```
Example 1

Input: 1
Output: ["1"]  * Leaf node base condition
```

```
Input: root = [1, 2, 3, null, 5]

                     1* [1]
                    / \
                   2   3
                    \
                     5

                     1
                    / \
          [1, 2]  *2   3
                    \
                     5


                     1
                    / \
                   2   3
                    \
                     5* [1, 2, 5]

res = ["1->2->5"]

                     1
                    / \
          [1, 2]  *2   3    => pop the current before returning from recursive function
                    \
                     5

                     1* [1]
                    / \
                   2   3
                    \
                     5

                     1
                    / \
                   2   3* [1, 3]
                    \
                     5

res = ["1->2->5","1->3"]

Output: ["1->2->5","1->3"]
```
