# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position. Return the max sliding window.
"""
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Brute Force:
Iterate over all (N -k + 1) sliding windows and find maximum of k elements in each window, -> O(Nk)

Approach 1: Use Max Heap
add element to a max_heap of size k -> O(logk)
Add N elements -> O(N)
So time complexity is O(Nlogk)

Approach 2: Dynamic Programming
Divide array in blocks of size k = 3

nums = 
 ________   _______  ____
 0  1   2   3  4  5  6  7
[1, 3, -1, -3, 5, 3, 6, 7]
                        ^
left_max = 
 _______   _______  ____
[1, 3, 3, -3, 5, 5, 6, 7]

nums = 
 ________   _______  ____
 0  1   2   3  4  5  6  7
[1, 3, -1, -3, 5, 3, 6, 7]
 ^
right_max = 
 _______   _______  ____
[3, 3, -1, 5, 5, 3, 7, 7]

nums = 
 ________   _______  ____
 0  1   2   3  4  5  6  7
[1, 3, -1, -3, 5, 3, 6, 7]

left_max = 
 _______   _______  ____
[1, 3, 3, -3, 5, 5, 6, 7]

right_max = 
 _______   _______  ____
[3, 3, -1, 5, 5, 3, 7, 7]

output = max(right_max[^], left_max[^ + k - 1])
[3, ]

"""

def sliding_window_maximum(nums, k):
    if not nums or not k: return None
    if k == 1: return nums

    left_max, right_max = [0] * len(nums), [0] * len(nums)

    left_max[0] = nums[0]
    right_max[-1] = nums[-1]

    for i in range(1, len(nums)):
        if i % k == 0:
            left_max[i] = nums[i]
        else:
            left_max[i] = max(left_max[i - 1], nums[i])

        j = len(nums) - i - 1
        if (j + 1) % k == 0:
            right_max[j] = nums[j]
        else:
            right_max[j] = max(right_max[j + 1], nums[j])

    ans = []
    for i in range(len(nums) - k + 1):
        ans.append(max(left_max[i + k - 1], right_max[i]))

    return ans

import unittest
class TestSlidingWindowMaximum(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(sliding_window_maximum([], 1), None)
        self.assertEqual(sliding_window_maximum([2], 0), None)

        self.assertEqual(sliding_window_maximum([2], 1), [2])
        self.assertEqual(sliding_window_maximum([2], 2), [])

    def test_generic(self):
        self.assertEqual(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

if __name__ == "__main__": unittest.main()