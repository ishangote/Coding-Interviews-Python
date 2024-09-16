"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?

## Questions:
1. Can there be -ve numbers? Yes
2. Is the array sorted? No

## Brute Force:
Example 1:
Input: 
nums = [2, 2, 1, 1, 1, 2, 2, 3, 2]
n/2 = 4

=> Sort array
=> Number at index n // 2 will always be the majority element

 0  1  2  3  4  5  6  7
[1, 1, 1, 2, 2, 2, 2, 2]

nums[4] = 2

Output: 2

### Moore Voting Algorithm
The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array. 
This assumption guarantees that even if the count is reset to 0 by other elements, the majority element will eventually regain the lead.

Example 1:
Input: 
nums = 
 0  1  2  3  4  5  6  7  8
[2, 2, 1, 1, 1, 2, 2, 3, 2]
                         ^
count = 0

idx = 0
count = 1
candidate = 2

idx = 1
count = 2
candidate = 2

idx = 2
count = 1
candidate = 2

idx = 3
count = 0
candidate = 2

idx = 4
count = 1
candidate = 1

idx = 5
count = 0
candidate = 1

idx = 6
count = 1
candidate = 2

idx = 7
count = 0
candidate = 2

idx = 8
count = 0
candidate = 2

Output = 2
"""

# Time: O(n)
# Space: O(n)
from collections import Counter
def majority_element_bf(nums):
    frequency_map = Counter(nums)
    for num, frequency in frequency_map.items():
        if frequency > len(nums) // 2: return num


# Time: O(nlogn)
# Space: O(1)
def majority_element_optimized(nums):
    nums.sort()
    return nums[len(nums) // 2]

# Moore Voting Algorithm
# Time: O(n)
# Space: O(1)
def majority_element_moore(nums):
    count = 0
    candidate = -999

    for num in nums:
        if count == 0: candidate = num
        if num == candidate: count += 1
        else: count -= 1
    
    return candidate

import unittest
class TestMajorityElement(unittest.TestCase):
    def test_majority_element_bf(self):
        self.assertEqual(majority_element_bf([2, 2, 1, 1, 1, 2, 2, 3, 2]), 2)
        self.assertEqual(majority_element_bf([2,2,1,1,1,2,2]), 2)

    def test_majority_element_optimized(self):
        self.assertEqual(majority_element_optimized([2, 2, 1, 1, 1, 2, 2, 3, 2]), 2)
        self.assertEqual(majority_element_optimized([2,2,1,1,1,2,2]), 2)

    def test_majority_element_moore(self):
        self.assertEqual(majority_element_moore([2, 2, 1, 1, 1, 2, 2, 3, 2]), 2)
        self.assertEqual(majority_element_moore([2,2,1,1,1,2,2]), 2)

if __name__ == "__main__": unittest.main()