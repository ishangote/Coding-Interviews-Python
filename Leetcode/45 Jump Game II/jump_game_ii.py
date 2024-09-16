import sys

# Time: O(n)
# Space: O(1)
def jump_game_ii(nums):
    res = 0
    left, right = 0, 0

    while right < len (nums) - 1:
        next_right = -sys.maxsize
        for idx in range(left, right + 1):
            next_right = max(next_right, idx + nums[idx])
        
        left = right + 1
        right = next_right

        res += 1
    
    return res

# ------------------------------------------------------------ #

import unittest
class TestJumpGameII(unittest.TestCase):
    def test_jump_game_ii(self):
        self.assertEqual(jump_game_ii([2, 3, 1, 1, 4]), 2)
        self.assertEqual(jump_game_ii([2, 3, 0, 1, 4]), 2)
        self.assertEqual(jump_game_ii([3, 1, 3, 1, 4]), 2)

if __name__ == "__main__": unittest.main()