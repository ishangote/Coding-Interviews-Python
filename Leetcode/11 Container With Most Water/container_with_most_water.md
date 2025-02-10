# 11. Container With Most Water

## Problem Statement

> You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i<sup>th</sup> line are `(i, 0)` and `(i, height[i])`.
>
> Find two lines that together with the x-axis form a container, such that the container contains the most water.
>
> Return the maximum amount of water a container can store.
>
> Notice that you may not slant the container.

> Constraints:
>
> - n == height.length
> - 2 <= n <= 10<sup>5</sup>
> - 0 <= height[i] <= 10<sup>4</sup>

## Examples

Example 1:

![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:

```
Input: height = [1,1]
Output: 1
```

## Brute Force

```
Input:
height =

 0  1  2  3  4  5  6  7  8
[1, 8, 6, 2, 5, 4, 8, 3, 7]

* Container's height is bound by the minimum of height of left wall and height of right wall

* Container's width is equal to distance between walls

Calculate area for each left_index, right_index =>
Area (water) = min(left_height, right_height) * (right_index - left_index)
```

## Two Pointers Solution

```
- We want to maximize the left_height and right_height and distance between the left and right wall

Input
height =

 0  1  2  3  4  5  6  7  8
[1, 8, 6, 2, 5, 4, 8, 3, 7]
 l                       r

area = min(1, 7) * (8 - 0) = 8


 0  1  2  3  4  5  6  7  8
[1, 8, 6, 2, 5, 4, 8, 3, 7]
    l                    r      * move left since left_height is less than right_height

area = min(8, 7) * (8 - 1) = 49

...

Output: 49
```
