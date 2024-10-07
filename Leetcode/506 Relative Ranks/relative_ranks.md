# 506. Relative Ranks

## Problem Statement

> You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
> The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
>
> - The 1st place athlete's rank is "Gold Medal".
> - The 2nd place athlete's rank is "Silver Medal".
> - The 3rd place athlete's rank is "Bronze Medal".
> - For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
>
> Return an array answer of size n where answer[i] is the rank of the ith athlete.

> Constraints:
>
> - n == score.length
> - 1 <= n <= 10<sup>4</sup>
> - 0 <= score[i] <= 10<sup>6</sup>
> - All the values in score are unique.

## Examples

Example 1:

```
Input: score = [5, 4, 3, 2, 1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
```

Example 2:

```
Input: score = [10, 3, 8, 9, 4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
```

## Brute Force Solution

```
Input:
score = [10, 3, 8, 9, 4]

       0  1  2  3  4
res = ["","","","",""]

score_with_idx = [(10, 0), (3, 1), (8, 2), (9, 3), (4, 4)]

reverse sort based on score =>
score_with_idx = [(10, 0), (9, 3), (8, 2), (4, 4), (3, 1)]
                    ^
* Populate result

res = ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Output:
["Gold Medal","5","Bronze Medal","Silver Medal","4"]
```
