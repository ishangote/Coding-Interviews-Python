# 492. Construct the Rectangle

## Problem Statement

> A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
>
> - The area of the rectangular web page you designed must equal to the given target area.
> - The width W should not be larger than the length L, which means L >= W.
> - The difference between length L and width W should be as small as possible.
>
>   Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

> Constraints:
>
> - 1 <= area <= 10<sup>7</sup>

## Examples

Example 1:

```
Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
```

Example 2:

```
Input: area = 37
Output: [37,1]
```

Example 3:

```
Input: area = 122122
Output: [427,286]
```

## Brute Force Solution

```
Input:
A = 4
Output:
[2, 2]

* Two Pointers

1 2 3 4
w     l     * A = 4 => possible solution => Length = 4 Width = 1

1 2 3 4     * A = 6 > 4 => move l to the left
  w l

1 2 3 4     * A = 4 => update solution => Length = 2 Width = 2
  w
  l
```

## Optimization

```
* The width and length must be as close to sqrt(area)
* Iterate width from sqrt(area) to 1
* length = area / width
```
