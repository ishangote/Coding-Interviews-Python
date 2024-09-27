# 414. Third Maximum Number

## Problem Statement

> Given an integer array `nums`, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
>
> Follow up: Can you find an O(n) solution?

> Constraints:
>
> - 1 <= nums.length <= 104
> - -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
```

Example 2:

```
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
```

Example 3:

```
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
```

## Brute Force Solution

```
* Remove duplicates (set)
* Sort and return num at idx [-3]

# Time: O(nlogn), where n => length of array
# Space: O(n), to store nums in set
```

## Optimized Solution

```
nums = [2, 2, 3, 1, 0, 5]
        ^
min_heap = None
min_heap_nums = {}


nums = [2, 2, 3, 1, 0, 5]
        ^
min_heap = 2*
min_heap_nums = {2}


nums = [2, 2, 3, 1, 0, 5]
           ^
min_heap = 2
min_heap_nums = {2}     <- since 2 already exists in hash set, do not add to min heap


nums = [2, 2, 3, 1, 0, 5]
              ^
min_heap = 3 - 2*
min_heap_nums = {2, 3}


nums = [2, 2, 3, 1, 0, 5]
                 ^
min_heap = 3 - 2 - 1*
min_heap_nums = {2, 3, 1}


nums = [2, 2, 3, 1, 0, 5]
                    ^
min_heap = 3 - 2 - 1 - 0* => 3 - 2 - 1
min_heap_nums = {2, 3, 1, 0} => {2, 3, 1}

* if length of min_heap_nums set > 3 => pop from min heap and remove from set


nums = [2, 2, 3, 1, 0, 5]
                       ^
min_heap = 5 - 3 - 2 - 1    => 5 - 3 - 2*
min_heap_nums = {2, 3, 1, 5} => {2, 3, 5}

* Return top of the heap

Output: 2

# Time: O(n)
# Space: O(1)
```

```
Input:

nums = [1, 2]
min_heap = 2 - 1*
min_heap_nums = [2, 1]

* if length of min_heap_nums < 3: return the max of min_heap_nums

Output: 2
```
