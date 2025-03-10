# 480. Sliding Window Median

## Problem Statement

> The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
>
> - For examples, if arr = [2,3,4], the median is 3.
> - For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
>
> You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
>
> Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

> Constraints:
>
> - 1 <= k <= nums.length <= 10<sup>5</sup>
> - -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
```

Example 2:

```
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

## Max Heap Min Heap Solution

1. Max-Heap (Lower Half):

- This heap stores the smaller half of the numbers.
- It allows you to quickly retrieve the maximum element of this half, which is a candidate for the median.

2. Min-Heap (Upper Half):

- This heap stores the larger half of the numbers.
- It allows you to quickly retrieve the minimum element of this half.

**How It Works**

- Balancing the Heaps:
  You ensure that the heaps are balanced in size (or the max-heap has one extra element if the window size is odd). This balance lets you efficiently compute the median:

- Odd k: The median is the top of the max-heap.
- Even k: The median is the average of the tops of both heaps.

- Sliding the Window:
  As the window moves:

- Insertion:

  - When a new number comes in, compare it with the top of the max-heap (which represents the largest number in the lower half) to decide which heap to insert into.

- Deletion:

  - The tricky part is removing the element that goes out of the window. Since heaps don’t support arbitrary deletion efficiently, you can use a lazy deletion strategy:
  - Mark for deletion: Keep a hash map (or dictionary) that tracks numbers that need to be removed.
  - Lazy Removal: When the number reaches the top of the heap, check if it’s marked for deletion and pop it off if necessary.

- Rebalancing:
  After every insertion and deletion, you may need to rebalance the heaps to maintain the size properties. This ensures that your median calculation remains valid.
