# 496. Next Greater Element I

## Problem Statement

> The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
> You are given two distinct 0-indexed integer arrays `nums1` and nums2, where `nums1` is a subset of `nums2`.
> For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.
>
> Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.
>
> Follow up: Could you find an O(nums1.length + nums2.length) solution?

> Constraints:
>
> - 1 <= nums1.length <= nums2.length <= 1000
> - 0 <= nums1[i], nums2[i] <= 10<sup>4</sup>
> - All integers in nums1 and nums2 are unique.
> - All the integers of nums1 also appear in nums2.

## Examples

Example 1:

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

Example 2:

```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

## Brute Force Solution

```
Input:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

* Numbers are unique in both arrays
* next greater element of nums2 numbers => to compute this run nested for loop
{
    1: 3
    3: 4
    4: -1
    2: -1
}

* Iterate over nums1 and return result

Output:
[-1, 3, -1]
```

## Optimization of Brute Force

```
* We do not need to compute the next greater of all elements of nums2

Input:
         0  1  2
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

nums1_idx_map = {
    4: 0
    1: 1
    2: 2
}
        0   1   2
res = [-1, -1, -1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
         ^                  * 1 exists in nums1_idx_map => compute next greater and insert at idx

res = [-1, 3, -1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
            ^               * ignore since 3 does not exist in nums1_idx_map
res = [-1, 3, -1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
               ^
res = [-1, 3, -1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
                  ^
res = [-1, 3, -1]
```

## Monotonic Stack Technique

```
Input:

nums1 = [4, 1, 2]
nums2 = [2, 0, 1, 3, 4]


* How are we searching for the next greater element? For example the number 2
nums2 = [2, 0, 1, 3, 4]
         ^
            *       0 is not greater than 2, continue

nums2 = [2, 0, 1, 3, 4]
         ^
               *       1 is not greater than 2, continue


nums2 = [2, 0, 1, 3, 4]
         ^
                  *        3 is greater than 2 => it has to be greater than all numbers between 2 and 3 in the array i.e 0, 1

------------------------------------------

* Monotonic stack technique:

nums2 = [2, 0, 1, 3, 4]
         ^                  * Does num exist in num1? yes
stack = [2]


nums2 = [2, 0, 1, 3, 4]
            ^               * Is num greater than 2? => No => Does num exist in num1? => No => continue
stack = [2]


nums2 = [2, 0, 1, 3, 4]
               ^            * Is num greater than 2? => No => Does num exist in num1? => Yes =>
                                    * Add it to stack, since the nex greater element of 2 will also be the next greater element of 1
stack = [2, 1]


nums2 = [2, 0, 1, 3, 4]     * Is num greater than 1? => Yes => 3 must be greater than all elements in stack => Pop all elements and add to result =>
                                    * Does num exist in num1? => No => continue
                  ^
stack = []
res = [-1, 3, 3]


nums2 = [2, 0, 1, 3, 4]     * Is num in num1? Yes => Add to stack
                     ^
stack = [4]
res = [-1, 3, 3]


nums2 = [2, 0, 1, 3, 4]     * Pop all elements in stack and add -1 to result
                       ^
stack = []
res = [-1, 3, 3]
```

## References

- https://www.youtube.com/watch?v=68a1Dc_qVq4&ab_channel=NeetCode
- https://leetcode.com/problems/next-greater-element-i/description/
