# 594. Longest Harmonious Subsequence

## Problem Statement

> We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
>
> Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
>
> A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

## Examples

Example 1:

```
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].
```

Example 2:

```
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.
```

Example 3:

```
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.
```

## Sorting Solution

```
Input:
nums = [1, 3, 2, 2, 5, 2, 3, 7]

harmonic subsequences =
[1, 2, 2, 2]
[3, 2, 2, 2, 3]


* Consider following harmonic subsequences:
1 2 2 1
1 2 1 2
1 1 2 2
2 1 2 1

* Any harmonic subsequence can only have 2 unique numbers (max and the min)
* Order does not matter but only the difference between the unique numbers should be equal to 1

* Sort the array
nums = [1, 2, 2, 2, 3, 3, 5, 7]
        ----------
           -------------            => find the larger subsequence

Output:
5
```

## Counting Solution

```

Input:
nums = [1, 3, 2, 2, 5, 2, 3, 7]

count_nums = {
    1: 1
    3: 2    *
    2: 3    *
    5: 1
    7: 1
}

* For each num in count_nums:
    - check if num + 1 is in count_nums
        -  calculate result by adding the counts

Output:
5
```
