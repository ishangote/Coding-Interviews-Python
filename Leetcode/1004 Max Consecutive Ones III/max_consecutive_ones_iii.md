# 1004. Max Consecutive Ones III

## Problem Statement

> Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

## Examples

Example 1:

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

Example 2:

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

## Sliding Window Solution

```
Input:
k = 2
nums =
 0  1  2. 3. 4. 5. 6. 7. 8  9  10
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
 s
                e

nums =
 0  1  2. 3. 4. 5. 6. 7. 8  9  10
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
             s
                e

nums =
 0  1  2. 3. 4. 5. 6. 7. 8  9  10
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
             s
                            e           length = 9 - 4 + 1 = 6  * compute max_length for each increment of e

nums =
 0  1  2. 3. 4. 5. 6. 7. 8  9  10
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
                s
                               e

Output:
4
```
