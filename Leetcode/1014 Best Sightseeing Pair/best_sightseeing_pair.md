# 1014. Best Sightseeing Pair

## Problem Statement

> You are given an integer array values where `values[i]` represents the value of the i<sup>th</sup> sightseeing spot. Two sightseeing spots `i` and `j` have a distance `j - i` between them.
>
> The score of a pair `(i < j)` of sightseeing spots is `values[i] + values[j] + i - j`: the sum of the values of the sightseeing spots, minus the distance between them.
>
> Return the maximum score of a pair of sightseeing spots.

> Constraints:
>
> - 2 <= values.length <= 5 \* 10<sup>4</sup>
> - 1 <= values[i] <= 1000

## Examples

Example 1:

```
                 0  1  2  3  4
Input: values = [8, 1, 5, 2, 6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
```

Example 2:

```
Input: values = [1, 2]
Output: 2
```

## Solution

```

score = values[i] + values[j] + i - j, where i < j
      = (values[i] + i) + (values[j] - j)

=> While iterating over j, keep track of maximum (values[i] + i) and keep track of maximum result


Input:
          0  1  2  3  4
values = [8, 1, 5, 2, 6]
res = -inf
max_left_score = 8 + 0 = 8


          0  1  2  3  4
values = [8, 1, 5, 2, 6]
             ^
res = max(-inf, 8 + 1 - 1)
max_left_score = max(8, 1 + 1)

          0  1  2  3  4
values = [8, 1, 5, 2, 6]
                ^
res = max(8, 5 + 8 - 2) = 11
max_left_score = max(8, 5 + 2)


...

Output:
11
```
