# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?


"""
# [IMPORTANT] -> positive and not greater than length of array and also greater than zero

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

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
    #solved it for n number of times repeat. Hence use set.
    ans = set()
    
    for x in nums:
        if nums[abs(x) - 1] > 0: nums[abs(x) - 1] *= -1
        else: ans.add(abs(x))

    return list(ans)

import unittest
class TestFindDuplicatesInArray(unittest.TestCase):
    def test_no_duplicates_input(self):
        self.assertEqual(find_all_duplicates([1, 4, 2, 3]), [])
        
    def test_positive_input(self):
        self.assertEqual(find_all_duplicates([1, 2, 3, 1, 3, 6, 6]), [1, 3, 6])

if __name__ == "__main__": unittest.main()