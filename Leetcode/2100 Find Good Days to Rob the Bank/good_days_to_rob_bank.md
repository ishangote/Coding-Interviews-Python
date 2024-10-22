# 2100. Find Good Days to Rob the Bank

## Problem Statement

> You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the i<sup>th</sup> day. The days are numbered starting from 0. You are also given an integer time.

> The i<sup>th</sup> day is a good day to rob the bank if:
>
> - There are at least time days before and after the ith day,
> - The number of guards at the bank for the time days before i are non-increasing, and
> - The number of guards at the bank for the time days after i are non-decreasing.
>
> More formally, this means day i is a good day to rob the bank if and only if `security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]`.
>
> Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter.

> Constraints:
>
> - 1 <= security.length <= 10<sup>5</sup>
> - 0 <= security[i], time <= 10<sup>5</sup>

## Examples

Example 1:

```
Input: security = [5,3,3,3,5,6,2], time = 2
Output: [2,3]
Explanation:
On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
```

Example 2:

```
Input: security = [1,1,1,1,1], time = 0
Output: [0,1,2,3,4]
Explanation:
Since time equals 0, every day is a good day to rob the bank, so return every day.
```

Example 3:

```
Input: security = [1,2,3,4,5,6], time = 2
Output: []
Explanation:
No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.
```

## Brute Force Solution

```
Example
security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
 ----           ----        * These will never be part of res
time = 2


 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
       -------              * Search space is reduced by 2 x time

=> For each idx in range =>

 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
       ^
 *  *                       * 2 days before and the day at ^ are non-increasing


 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
       ^
          *  *             * the day ^ and 2 days after are non-decreasing

res = [3]
```

## Optimization

```
Example:
security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
 ^
num_days_before =                  * # days before idx where security[idx - 1] >= security[idx]
[0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
    ^
num_days_before =                  * 3 <= 5
[0, 1]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
       ^
num_days_before =                  * 3 <= 3
[0, 1, 2]

...

security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
             ^
num_days_before =                  * 0 days before idx that are <= 5
[0, 1, 2, 3, 0]

security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
                   ^
num_days_before =                  * 0 days before idx that are <= 5
[0, 1, 2, 3, 0, 0, 1]

-------------------------------------------------

security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
                   ^
                                   * # days after idx where security[idx] <= security[idx + 1]
num_days_after =
[0, 0, 0, 0, 0, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
                ^
num_days_after =
[0, 0, 0, 0, 0, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
             ^
num_days_after =
[0, 0, 0, 0, 1, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
          ^
num_days_after =
[0, 0, 0, 2, 1, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
       ^
num_days_after =
[0, 0, 3, 2, 1, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
    ^
num_days_after =
[0, 4, 3, 2, 1, 0, 0]


security =
 0  1  2  3  4  5  6
[5, 3, 3, 3, 5, 6, 2]
 ^
num_days_after =
[0, 4, 3, 2, 1, 0, 0]

-------------------------------------------------

security =
[5, 3, 3, 3, 5, 6, 2]

num_days_after =
 0  1  2  3  4  5  6
[0, 4, 3, 2, 1, 0, 0]

num_days_before =
 0  1  2  3  4  5  6
[0, 1, 2, 3, 0, 0, 1]

idx 2, 3 have # days before and # days after >= time

Output:
[2, 3]
```
