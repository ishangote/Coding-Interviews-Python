# 697. Degree of an Array

## Problem Statement

> Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
> Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

> Constraints:
>
> - nums.length will be between 1 and 50,000.
> - nums[i] will be an integer between 0 and 49,999.

## Examples

Example 1:

```
Input: nums = [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

Example 2:

```
Input: nums = [1, 2, 2, 3, 1, 4, 2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
```

## Brute Force Solution

```
Input:
nums = [1, 2, 1, 3, 1, 2, 2]

nums =
[1, 2, 1, 3, 1, 2, 2]

* Find all numbers contributing to degree
degree-nums = [1, 2]

* Search contiguous sub-array containing all 1's
nums =
[1, 2, 1, 3, 1, 2, 2]
 ^           ^

* Search contiguous sub-array containing all 2's
nums =
[1, 2, 1, 3, 1, 2, 2]
    ^              ^

* Return length of shorter sub-array

Output: 5
```

## Optimization

```
Input:
nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
 *     *
    ^        ^                  => smallest contiguous sub-arrays containing all degree contributing numbers
          +           +

* goal is to find the first seen location and the last seen location of all degree contributing numbers
* we can do this while counting the occurences itself

nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
 ^

nums_count = {
    0: [1, (0, 0)]      => [count, (first_seen, last_seen)] * set default last_seen as the idx itself
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
    ^

nums_count = {
    0: [1, (0, 0)]
    2: [1, (1, 1)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
       ^

nums_count = {
    0: [2, (0, 2)]  => update the last seen of 0 along with the count
    2: [1, (1, 1)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
          ^

nums_count = {
    0: [2, (0, 2)]
    2: [1, (1, 1)]
    1: [1, (3, 3)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
             ^

nums_count = {
    0: [2, (0, 2)]
    2: [2, (1, 4)]      => update last seen as well as count
    1: [1, (3, 3)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
                ^

nums_count = {
    0: [2, (0, 2)]
    2: [2, (1, 4)]
    1: [1, (3, 3)]
    3: [1, (5, 5)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
                   ^

nums_count = {
    0: [2, (0, 2)]
    2: [2, (1, 4)]
    1: [1, (3, 3)]
    3: [1, (5, 5)]
    4: [1, (5, 5)]
}


nums =
 0  1  2  3  4  5  6  7
[0, 2, 0, 1, 2, 3, 4, 1]
                      ^

nums_count = {
    0: [2, (0, 2)] *
    2: [2, (1, 4)] *    => find shortest sub array => last_seen - first_seen
    1: [2, (3, 7)] *
    3: [1, (5, 5)]
    4: [1, (5, 5)]
}
```

#### Coding Note

> `TypeError: 'tuple' object does not support item assignment`

We can not utilize tuples to store `(first_seen, last_seen)` since we can not update the last seen by assignment
