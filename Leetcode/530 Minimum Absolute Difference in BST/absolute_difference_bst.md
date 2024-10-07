# 530. Minimum Absolute Difference in BST

## Problem Statement

> Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

> Constraints:
>
> -
> - The number of nodes in the tree is in the range [2, 10<sup>4</sup>].
> - 0 <= Node.val <= 10<sup>5</sup>

## Examples

Example 1:

```
            4
           / \
          2   6
         / \
        1   3

Input: root = [4,2,6,1,3]
Output: 1
```

Example 2:

```
            1
           / \
          0   48
              / \
             12  49

Input: root = [1,0,48,null,null,12,49]
Output: 1
```

## Solution

```
* In-order traversal of BST: [7, 15, 17, 4, 6]
                              ^  ^
                              *     *

* Note:
- difference between 7 and 15 will be always smaller than 7 and 17
- minimum difference nodes will always lie either in the left sub-tree or right-subtree

Input:
root =
                20
               /  \
             15    25
            /  \   /
           7   17 24


prev = None
min_diff = inf

In-order traversal =>

                20
               /  \
             15    25
            /  \   /
         * 7   17 24

node = 7
prev = None => 7
min_diff = inf


                20
               /  \
           * 15    25
            /  \   /
           7   17 24

node = 15
prev = 7
min_diff = inf => 8


                  20
               /     \
             15       25
            /  \      /
           7   17*   24

node = 17
prev = 15
min_diff = 8 => 2


                  20*
               /     \
             15       25
            /  \      /
           7   17    24

node = 20
prev = 17
min_diff = 2      * Do not update


                  20
               /     \
             15       25
            /  \      /
           7   17    24*

node = 24
prev = 20
min_diff = 2


                  20
               /     \
             15       25*
            /  \      /
           7   17    24

node = 25
prev = 24
min_diff = 2 => 1
```
