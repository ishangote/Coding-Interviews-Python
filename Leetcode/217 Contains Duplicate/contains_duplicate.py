# Time: O(n), where n => lenght of nums
# Space: O(n)
def contains_duplicate(nums):
    seen_nums = set()

    for num in nums:
        if num in seen_nums: return True
        seen_nums.add(num)
    
    return False

import unittest
class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(contains_duplicate([1, 2, 3, 1]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicate([1, 1, 1, 2, 3, 4]), True)

if __name__ == "__main__": unittest.main()
