"""
Brute Force: Sort array
Approach 2: array to store count at respective indices
Approach 3: Use numbers as indices
"""
#Time O(n), Space O(n) => when input is read only
def repeat_missing1(nums):
    ans = [0, 0]
    count = [0 for i in range(len(nums))]
        
    for i in range(len(nums)): count[nums[i] - 1] += 1

    for i in range(len(count)):
        if count[i] == 2: ans[0] = i + 1
        elif count[i] == 0: ans[1] = i + 1
        else: continue
    return ans

#Time O(n), Space O(1)
def repeat_missing2(nums):
    ans = []
    #To find repeated
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] > 0: nums[abs(nums[i]) - 1] *= -1
        else: ans.append(abs(nums[i]))
    #To find missing
    for i in range(len(nums)):
        if nums[i] > 0: ans.append(i + 1)

    return ans

import unittest
class TestRepeatAndMissingNumber(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(repeat_missing1([3, 1, 1, 4]), [1, 2])
        self.assertEqual(repeat_missing2([3, 1, 1, 4]), [1, 2])

if __name__ == '__main__': unittest.main()