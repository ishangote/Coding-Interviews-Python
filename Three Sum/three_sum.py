# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? F
# ind all unique triplets in the array which gives the sum of zero.
#Note: The solution set must not contain duplicate triplets.

"""
[-1, 0, 1, 2, -1, -4]
  
Sort: 

[-4, -1, -1, 0, 1, 2]
  ^   l 
          r

[[-1, -1, 2], [-1, 0, 1]]


[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""

import unittest
def three_sum(nums):

    result = []
    
    nums = sorted(nums)
    for idx in range(0, len(nums) - 3):
        #No duplicates condition =>
        if idx == 0 or nums[idx] > nums[idx - 1]:
            left, right = idx + 1, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + nums[idx] == 0: 
                    result.append([nums[idx], nums[left], nums[right]])
                    #We still have to increment/decrement left/right

                if nums[left] + nums[right] + nums[idx] < 0:
                    curr_left = left
                    #Not to consider same values of left
                    while(nums[left] == nums[curr_left] and left < right):
                        left += 1

                else:
                    curr_left = left
                    #Not to consider same values of left
                    while(nums[left] == nums[curr_left] and left < right):
                        right -= 1

    return result

class TestThreeSum(unittest.TestCase):
    def test_generic_example(self):
        self.assertEqual(three_sum([-4, -1, -1, 0, 1, 2]), [[-1, -1, 2]], [-1, 0, 1])

    def test_all_zero_input(self):
        self.assertEqual(three_sum([0, 0, 0, 0, 0]), [[0, 0, 0]])

    def test_only_two_values_input(self):
        self.assertEqual(three_sum([-1 , 1]), [])

    def test_no_three_pairs_input(self):
        self.assertEqual(three_sum([2, 3, 4, 5, 6, 7]), [])

if __name__ == "__main__": unittest.main()


