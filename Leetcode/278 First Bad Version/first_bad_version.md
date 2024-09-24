# 278. First Bad Version

## Problem Statement

> You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
> Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
> You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

> Constraints:
>
> - 1 <= bad <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

Example 2:

```
Input: n = 1, bad = 1
Output: 1
```

## Binary Search Solution

```
Input:
n = 6
isBadVersion(4) -> true

lo = 1
hi = 6
mid = 3 -> false (set lo to mid + 1)

lo = 4
hi = 6
mid = 5 -> true (set hi to mid) * 5 can potentially be the first bad version

lo = 4
hi = 5
mid = 4 -> true (set hi to mid) * 4 can potentially be the first bad version

lo = 4
hi = 4
lo == hi => return 4
```

```
Input:
n = 3
isBadVersion(2) -> true

lo = 1
hi = 3
mid = 2 -> false (set lo to mid + 1)

lo = 3
hi = 3
lo == hi: return 3
```
