# 645. Set Mismatch

## Problem Statement

> You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
>
> You are given an integer array nums representing the data status of this set after the error.
>
> Find the number that occurs twice and the number that is missing and return them in the form of an array.

> Constraints:
>
> - 2 <= nums.length <= 10<sup>4</sup>
> - 1 <= nums[i] <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: nums = [1,2,2,4]
Output: [2,3]
```

Example 2:

```
Input: nums = [1,1]
Output: [1,2]
```

## Brute Force Solution

```
* Sort nums
nums = [1, 1]

* Iterate over nums to find missing number
* previous number is the duplicate number
```

## Optimized Solution

```
nums =
 0  1  2  3
[4, 2, 2, 1]

* If the operation was not performed nums and nums is sorted it would look like:
 0  1  2  3
[1, 2, 3, 4]

* We can utilize the idx to keep track of missing number


 0  1  2  3
[4, 2, 2, 1]
 ^              =>  mark idx (4 - 1) with negative

 0  1  2   3
[4, 2, 2, -1]
    ^

 0  1  2   3
[4, 2, 2, -1]
    ^           => mark idx (2 - 1) with negative

 0   1  2   3
[4, -2, 2, -1]
        ^       => idx(2 - 1) is already negative => duplicate number = 2

 0   1  2   3
[4, -2, 2, -1]
            ^   => mark idx (1 - 0) with negative

  0   1  2   3
[-4, -2, 2, -1]     * All numbers are negative except for idx == 2 => missing number = 2 + 1
```
