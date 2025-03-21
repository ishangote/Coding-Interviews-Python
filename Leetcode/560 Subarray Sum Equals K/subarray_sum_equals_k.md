# 560. Subarray Sum Equals K

## Problem Statement

> Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
> A subarray is a contiguous non-empty sequence of elements within an array.

> Constraints:
>
> - 1 <= nums.length <= 2 \* 10<sup>4</sup>
> - -1000 <= nums[i] <= 1000
> - -10<sup>7</sup> <= k <= 10<sup>7</sup>

## Examples

Example 1:

```
Input: nums = [1,1,1], k = 2
Output: 2
```

Example 2:

```
Input: nums = [1,2,3], k = 3
Output: 2
```

## Brute Force Solution

```
* Check all possible subarrays by iterating over all pairs (i, j).

Input:
nums = [1, 2, 3], k = 3

[1]
[1, 2]          => valid
[1, 2, 3]
[2]
[2, 3]
[3]             => valid

Output: 2
```

## Prefix-Sum + Hash-Map Solution

### Mathematical Insight

```
                i           j
nums = [x1, x2, x3, x4, x5, x6, x7, x8]
        p1, p2, p3, p4, p5, p6, p7, p8      prefix sums
        ---------------------- p6
        ----------p3

        if p6 - p3 = k  =>  p3 = p6 - k
                            ^
                            Count of prefix sums = p3 will be the number of subarrays ending at j


             xxxxxxxxxxxxxxxxxxxxxxxxx k
                          xxxxxxxxxxxx k
        ****************************** n
nums = [x1, x2, x3, x4, x5, x6, x7, x8]
        ------------------n-k
        ------n-k

Formalized:
If prefix_sum[j] - prefix_sum[i] = k,
    then prefix_sum[i] = prefix_sum[j] - k
Thus, we need to find prefix_sum[i] in the map.
```

### Important Edge Case

> To account for subarrays starting at index 0, we initialize prefix_sum_count = {0: 1}.

```
Example:
nums =
[3, 4, 7]
k = 7

prefix_sum_count = {
    0: 1
    3: 1
    7: 1
    14: 1
}

nums
[3, 4, 7]
 ^
prefix_sum - k = 3 - 7 (not in prefix_sum_count => continue)

nums
[3, 4, 7]
    ^
prefix_sum - k = 7 - 7 = 0
=>  WE NEED TO SET prefix_sum = 0 in prefix_sum_count with DEFAULT count as 1
=> This will ensure we consider the subarrays that start at index 0
=> count = 1
=> res = 1

nums
[3, 4, 7]
       ^

prefix_sum - k = 7 (in prefix_sum_count)
res = 2

Output:
2
```

## Variations

1. return T/F instead of count
2. Non negative integers + return T/F -> use sliding window
3. Non negative integers + return length of sub array -> use sliding window
