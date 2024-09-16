# 222. Count Complete Tree Nodes

## Problem Statement

> Given the root of a complete binary tree, return the number of the nodes in the tree.
>
> According to [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees), every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.
>
> Design an algorithm that runs in less than O(n) time complexity.

## Examples

```
Example 1:
Input: None
Output: 0

Example 2:
Input:
         1
       /   \
      2     3
     / \   /
    4   5 6

Output:
6
```

## Brute Force

DFS/BFS to count each node. Time complexity: O(n), n => number of nodes. Space: O(h), h => height of BT, in worst case, h = n

## Optimization

> Formula to remember:
> #nodes = 2 ^ h - 1, for full binary tree
> h => height of BT (starting from 1)

```
Example 1:

Input:
        1

Full BT, using formula 2^h - 1 #nodes = 1

Output: 1

---------------------------

Example 2:

Input:
            1*
          /
         2* Full binary tree => return #nodes = 2^1 - 1 = 1

Output: 2

---------------------------

Example 2:

Input:
            1* Full binary tree => return #nodes = 2^2 - 1 = 3
           / \
          2   3


* Full binary tree: left sub-tree height = right sub-tree height.
* This is not the height of the BT. Just move in either left or right direction till the end to compute this height

Output: 3

---------------------------

Example 2:

Input:
            1* left_height = 3, right_height = 2
           / \
          2   3
         /
        4


            1
           / \
lh=2,rh=1 2*  3
         /
        4

            1
           / \
          2  3
         /
        4* lh = 1, rh = 1 (Full binary tree => #nodes = 2^1 - 1 = 1)


                 1
                / \
 #nodes=1+1=2  2*  3
              /
             4

Output: 4
```

## Time Complexity Analysis

- We are computing height many times. Each computation of height requires O(logn)
- We need to compute height of the last leaf nodes in the worst case. To reach this point we have computed height log(n) times
- Hence time complexity is O(logn x logn)
