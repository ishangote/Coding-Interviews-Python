# Given an array of n elements which contains elements from 0 to n-1
# with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.
# For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.



"""
# [IMPORTANT] -> positive and not greater than length of array

The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. 
We do this by making elements at certain indexes negative. See the full explanation here

Initial:
 0  1  2  3  4  5  6
[1, 2, 3, 1, 3, 6, 6]

nums[abs(x) - 1] = 0 >= 0 => nums[abs(x) - 1] *= -1 = -1
  0  1  2  3  4  5  6
[-1, 2, 3, 1, 3, 6, 6]
 ^

nums[abs(x) - 1] = 2 >= 0 => nums[abs(x) - 1] *= -1 = -1
  0   1  2  3  4  5  6
[-1, -2, 3, 1, 3, 6, 6]
      ^

nums[abs(x) - 1] = 3 >= 0 => nums[abs(x) - 1] *= -1 = -1
  0   1   2  3  4  5  6
[-1, -2, -3, 1, 3, 6, 6]
          ^

nums[abs(x) - 1] = -1 < 0 => res.append(abs(x)) = [1]
  0   1   2  3  4  5  6
[-1, -2, -3, 1, 3, 6, 6]
             ^

nums[abs(x) - 1] = -3 < 0 => res.append(abs(x)) = [1, 3]
  0   1   2  3  4  5  6
[-1, -2, -3, 1, 3, 6, 6]
                ^

nums[abs(x) - 1] = 6 >= 0 => nums[abs(x) - 1] *= -1 = -1
  0   1   2  3  4  5  6
[-1, -2, -3, 1, 3,-6, 6]
                   ^

nums[abs(x) - 1] = -6 < 0 => res.append(abs(x)) = [1, 3, 6]
  0   1   2  3  4  5  6
[-1, -2, -3, 1, 3,-6, 6]
                      ^
"""

def find_all_duplicates(nums):
    if not nums: return None
    ans = []
    
    for x in nums:
        if nums[abs(x) - 1] > 0: nums[abs(x) - 1] *= -1
        else: ans.append(abs(x))

    return ans

import unittest
class TestFindDuplicatesInArray(unittest.TestCase):
    def test_no_duplicates_input(self):
        self.assertEqual(find_all_duplicates([1, 4, 2, 3]), [])

    def test_positive_input(self):
        self.assertEqual(find_all_duplicates([1, 2, 3, 1, 3, 6, 6]), [1, 3, 6])

if __name__ == "__main__": unittest.main()