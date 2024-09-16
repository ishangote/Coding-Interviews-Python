# 226. Invert Binary Tree

## Problem Statement

> Given the root of a binary tree, invert the tree, and return its root.

```
Example 1:

Input:
        4
      /   \
     2     7
    / \   /  \
   1   3 6    9

Output:

        4
      /   \
     7     2
    / \   /  \
   9   6 3    1


Example 2:

Input:
        2
       / \
      1   3

Output:
        2
       / \
      3   1
```

> Constraints:
> The number of nodes in the tree is in the range [0, 100].
> -100 <= Node.val <= 100

## Recursive Solution

```
Example 1:

Input:
        1
Output:
        1

------------------------------
Base Case: if node does not have children then stop
Else: swap node.left and node.right

Example 2:

Input:
        2*
       / \
      1   3

        2
       / \
     *3   1

        2
       / \
      3   1*


Output:
        2
       / \
      3   1

------------------------------

Example 3:

Input:
        4*
      /   \
     2     7
    / \   /  \
   1   3 6    9

        4
      /   \
    *7     2
    / \   /  \
   6   9 1    3

        4
      /   \
     7     2
    / \   /  \
  *9   6 1    3


        4
      /   \
     7     2
    / \   /  \
   9  *6 1    3

        4
      /   \
     7     2*
    / \   /  \
   9   6 1    3

        4
      /   \
     7     2
    / \   /  \
   9   6 3*   1

Output:
        4
      /   \
     7     2
    / \   /  \
   9   6 3    1*
```

## References

- Leetcode: https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
