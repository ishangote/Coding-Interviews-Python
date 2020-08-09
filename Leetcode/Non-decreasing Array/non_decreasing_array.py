# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""
Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Non-Decreasing => nums[i] <= nums[i + 1]
NOTE: since not strictly increasing we can modify arr[i] to arr[i - 1]

Brute Force:
new_arr = arr
For each i new_arr[i] = new_arr[i - 1]
check monotone_increasing(nwe_arr) -> return True else new_arr = arr (Reinit)

Optimized: Atmost 1 change allowed

"""
def non_decreasing_arr(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            if i == 0: arr[i] = arr[i + 1]
            elif arr[i - 1] <= arr[i + 1]: arr[i] = arr[i - 1]
            else: arr[i + 1] = arr[i]

        if count > 1: return False

    return True

import unittest
class TestNonDecreasingArrray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(non_decreasing_arr([4, 2, 3]), True)
        self.assertEqual(non_decreasing_arr([4, 2, 1]), False)

if __name__ == "__main__": unittest.main()