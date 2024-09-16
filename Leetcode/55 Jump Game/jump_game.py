from collections import defaultdict
def recursive_helper(idx, nums, memo):
    if idx > len(nums) - 1: return False
    if idx == len(nums) - 1: return True

    if idx in memo: return memo[idx]

    memo[idx] = False
    for jump in range(1, nums[idx] + 1):
        next_idx = idx + jump
        if next_idx > len(nums) - 1 or memo[idx]: break

        memo[idx] = memo[idx] or recursive_helper(next_idx, nums, memo)
    
    return memo[idx]

def jump_game_brute_force(nums):
    memo = defaultdict(bool)
    return recursive_helper(0, nums, memo)

# ---------------------------------------------------- #

# Time: O(n)
# Space: O(1)
def jump_game_greedy(nums):
    goal = len(nums) - 1

    for idx in range(len(nums) - 2, -1, -1):
        if idx + nums[idx] >= goal: goal = idx
    
    return True if goal == 0 else False

# ---------------------------------------------------- #

import unittest
class TestJumpGame(unittest.TestCase):
    def test_jump_game_brute_force(self):
        self.assertEqual(jump_game_brute_force([4]), True)
        self.assertEqual(jump_game_brute_force([2, 3, 1, 1, 4]), True)
        self.assertEqual(jump_game_brute_force([3, 2, 1, 0, 4]), False)

    def test_jump_game_greedy(self):
        self.assertEqual(jump_game_greedy([4]), True)
        self.assertEqual(jump_game_greedy([2, 3, 1, 1, 4]), True)
        self.assertEqual(jump_game_greedy([3, 2, 1, 0, 4]), False)
    
if __name__ == "__main__": unittest.main()
