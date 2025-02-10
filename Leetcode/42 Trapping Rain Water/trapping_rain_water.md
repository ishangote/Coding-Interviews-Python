# 42. Trapping Rain Water

## Problem Statement

> Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

> Constraints:
>
> - n == height.length
> - 1 <= n <= 2 \* 10<sup>4</sup>
> - 0 <= height[i] <= 10<sup>5</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

Example 2:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Dynamic Programming Solution

```
* water trapped is defined by min(left_max, right_max) at any given index
* water trapped at idx = min(left_max, right_max) - height[idx]

Input:
              0  1  2  3  4  5  6  7  8  9  10  11
height    =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2,  1]
left_max  =  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3,  3]


              0  1  2  3  4  5  6  7  8  9  10  11
height    =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2,  1]
right_max =  [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2,  1]

Calculate res += min(left_max, right_max) - height[idx]

Output: 6
```

## Two Pointers Solution

- The two-pointer approach optimizes space complexity to O(1) while maintaining a time complexity of O(n). It leverages the fact that the trapped water at any index is determined by the minimum of the maximum heights to its left and right.
- Notice that as long as `right_max[i] > left_max[i]` (from element 0 to 6), the water trapped depends upon the `left_max`. Hence we can add `left_max - heights[left]` to result.
- and the case when `left_max[i] > right_max[i]` (from element 8 to 11), the water trapped depends upon the `right_max`. Hence we can add `right_max - heights[right]` to result.

## References

- https://www.youtube.com/watch?v=Uog2Jmyb3iY&t=64s
- https://www.youtube.com/watch?v=lhzrp3Nbj-w&t=365s
- https://www.youtube.com/watch?v=pq7Xon_VXeU
