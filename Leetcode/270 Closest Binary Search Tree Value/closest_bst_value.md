# 270. Closest Binary Search Tree Value

## Problem Statement

> Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
> - 0 <= Node.val <= 10<sup>9</sup>
> - -10<sup>9</sup> <= target <= 10<sup>9</sup>

## Examples

Example 1:

```
Input:
root =
            4
          /   \
         2     5
        / \
       1   3

target = 3.714286

Output:
4
```

Example 2:

```
Input:
root = 1
target = 3.714286
Output:
1
```

## Solution

```
Input:
target = 3.714286
root =
           *4 (4 - 3.714286) = 0.29
          /   \
         2     5
        / \
       1   3

root =
                              4
                            /   \
(2 - 3.714286) = 1.71     *2     5
                          / \
                         1   3

root =
                              4
                            /   \
                           2     5
                          / \
                         1   3* (3 - 3.714286) = 0.71

Return 4 since min_distance = 4
* if current distance is equal to min distance then compare the values

Output:
4
```
