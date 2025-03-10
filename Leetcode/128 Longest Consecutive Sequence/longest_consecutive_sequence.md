# 128. Longest Consecutive Sequence

## Problem Statement

> Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
> You must write an algorithm that runs in O(n) time.

> Constraints:
>
> - 0 <= nums.length <= 10<sup>5</sup>
> - -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

Example 2:

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

Example 3:

```
Input: nums = [1,0,1,2]
Output: 3
```

## Hash Set and Two Pointers Solution

- HashSet for Fast Lookups:

  - The solution converts the list into a set to allow O(1) time checks for the presence of consecutive numbers.

- Bidirectional Sequence Expansion:

  - For each number, the algorithm expands upward (num + 1, num + 2, …) and downward (num - 1, num - 2, …) to count the full consecutive sequence.

- Removal of Processed Elements:

  - Elements are removed from the set as they are processed, ensuring that each number is only examined once and reducing redundant checks.
