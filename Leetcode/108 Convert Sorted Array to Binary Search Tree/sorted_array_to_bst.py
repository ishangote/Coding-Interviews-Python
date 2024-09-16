class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def recursive_helper(nums, lo, hi):
    if hi < lo: return None
    
    mid = (lo + hi) // 2
    root = BTNode(nums[mid])

    root.left = recursive_helper(nums, lo, mid - 1)
    root.right = recursive_helper(nums, mid + 1, hi)

    return root

# Time: O(n) where n => length of nums
# Space: O(logn) => implied call stack memory
def sorted_array_to_bst(nums):
    return recursive_helper(nums, 0, len(nums) - 1)

import unittest
class TestSortedArrayToBST(unittest.TestCase):
    def test_edge_case(self):
        nums = []
        self.assertEqual(sorted_array_to_bst(nums), None)

    def test_sorted_array_to_bst(self):
        nums = [-10, -3, 0, 5, 9]
        root = sorted_array_to_bst(nums)

        self.assertEqual(root.value, 0)

        self.assertEqual(root.left.value, -10)
        self.assertEqual(root.right.value, 5)
        
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right.value, -3)

        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right.value, 9)

if __name__ == "__main__": unittest.main()
