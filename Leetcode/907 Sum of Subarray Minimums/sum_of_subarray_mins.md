# 907. Sum of Subarray Minimums

## Problem Statement

> Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer `modulo` 10<sup>9</sup> + 7.

> - Constraints:
>
> - 1 <= arr.length <= 3 \* 10<sup>4</sup>
> - 1 <= arr[i] <= 3 \* 10<sup>4</sup>

## Examples

Example 1:

```
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

Example 2:

```
Input: arr = [11,81,94,43,3]
Output: 444
```

## Brute Force Solution

```
Input:
nums =
[3, 1, 2, 4]

* Track current min value and res while computing all subarrays
```

## Monotonic Stack Technique Solution

```
Example:
nums =
[1, 4, 3, 2]

subarrays =             Min Values
[1]                     1
[1, 4]                  1
[1, 4, 3]               1
[1, 4, 3, 2]            1
[4]                     4
[4, 3]                  3
[4, 3, 2]               2
[3]                     3
[3, 2]                  2
[2]                     2


res = 1 + 1 + 1 + 1 + 4 + 3 + 2 + 3 + 2 + 2

* How many times does each number contribute to the answer?
1 => 4  (1 x 4)
4 => 1  (4 x 1)
3 => 2  (3 x 2)
2 => 3  (2 x 3)
        -------
          20

* How many subarrays is a number part of where it is the minimum value?

Example
                         0  1  2  3  4  5  6  7
                        [1, 4, 6, 7, 3, 7, 8, 1]
                            --------- ------
                                     ^

* All subarrays formed in idx range [1, 6] will have minimum value of 3

* How many subarrays can be formed =

subarrays with 3 as minimum
[4, 6, 7, 3, 7, 8]
[4, 6, 7, 3, 7]
[4, 6, 7, 3]
[6, 7, 3, 7, 8]
[6, 7, 3, 7]
[6, 7, 3]
[7, 3, 7, 8]
[7, 3, 7]
[7, 3]
[3, 7, 8]
[3, 7]
[3]

# nums to the left (including 3) * # nums to the right (including 3)
= 4 * 3 = 12

* Hence there will be 12 subarrays where 3 is minimum, i.e 3 will contribute to res 12 times

* We need to find the previous smaller number index and the next smaller number index for each number
```

```
Input:
nums =
[3, 1, 2, 4]

subarrays =>
                * Mins
[3]             3
[3 1]           1
[3 1 2]         1
[3 1 2 4]       1
[1]             1
[1 2]           1
[1 2 4]         1
[2]             2
[2 4]           2
[4]             4


res = 3 + 1 * 6 + 2 * 2 + 4
            ---     ---

* 1 is the minimum value in 6 subarrays
    * 1 is the minimum of all values to the left
    * 1 is the minimum of all values to the right

* 2 is the minimum value in 2 subarrays
    * 2 itself is the min value to the left [2]
    * 2 is the minimum of all values to the right [2, 4]

[3, 1, 2, 4]
       -
       ----

# subarrays where 2 is minimum =
    # nums to left where 2 is min * # nums to right where 2 is min

* Next Smaller Indices =>
Iterate: Left to Right
Stack Type: Increasing

nums =
[3, 1, 2, 4]
stack = []
next_smaller_index =
[4, 4, 4, 4]            * Initialize to len(nums)

nums =
[3, 1, 2, 4]
 ^
stack = [(0, 3)]
next_smaller_index =
[4, 4, 4, 4]

nums =
 0  1  2  3
[3, 1, 2, 4]
    ^
stack = [(1, 1)]
next_smaller_index =
 0  1  2  3
[1, 4, 4, 4]

nums =
 0  1  2  3
[3, 1, 2, 4]
       ^
stack = [(1, 1), (2, 2)]
next_smaller_index =
 0  1  2  3
[1, 4, 4, 4]

nums =
 0  1  2  3
[3, 1, 2, 4]
          ^
stack = [(1, 1), (2, 2), (3, 4)]
next_smaller_index =
 0  1  2  3
[1, 4, 4, 4]

* Previous Smaller Indices =>
Iterate: Right to Left
Stack Type: Increasing

nums =
[3, 1, 2, 4]
stack = []
prev_smaller_index =
[-1, -1, -1, -1]        * Initialize to -1


nums =
 0  1  2  3
[3, 1, 2, 4]
          ^
stack = [(3, 4)]
prev_smaller_index =
[-1, -1, -1, -1]


nums =
 0  1  2  3
[3, 1, 2, 4]
       ^
stack = [(2, 2)]
prev_smaller_index =
[-1, -1, -1, 2]


nums =
 0  1  2  3
[3, 1, 2, 4]
    ^
stack = [(1, 1)]
prev_smaller_index =
[-1, -1, 1, 2]


nums =
 0  1  2  3
[3, 1, 2, 4]
 ^
stack = [(1, 1), (3, 3)]
prev_smaller_index =
[-1, -1, 1, 2]


* Calculate Result
                      0  1  2  3
nums               = [3, 1, 2, 4]
prev_smaller_index = [-1, -1, 1, 2]
next_smaller_index = [1, 4, 4, 4]


res =
3 * [(0 - (-1 + 1) + 1) * ((1 - 1) - 0 + 1)] => 3 * 1
+
1 * [(1 - (-1 + 1) + 1) * ((4 - 1) - 1 + 1)]    => 1 * [2 * 3]
+
2 * [(2 - (1 + 1) + 1) * ((4 - 1) - 2 + 1)]
...
```
