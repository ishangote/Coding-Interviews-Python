import unittest
import random
from collections import defaultdict


class RandomPickIndex:
    # Time: O(n), where n => length of nums
    # Space: O(n)
    def __init__(self, nums):
        self.nums = nums
        self.index_dict = defaultdict(list)

        for idx, num in enumerate(nums):
            self.index_dict[num].append(idx)

    # Time: O(1)
    # Space: O(1)
    def pick(self, target):
        return random.choice(self.index_dict[target])

    # Time: O(n), where n => length of nums
    # Space: O(1)
    def pick_reservoir_sampling(self, target):
        count = 0  # Count occurrences of target
        chosen_index = -1  # Store the chosen index

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # With probability 1/count, replace the chosen index
                # random.randint(1, count) generates a random integer between 1 and count (inclusive).
                if random.randint(1, count) == 1:
                    chosen_index = i

        return chosen_index

    # Time: O(n)
    # Space: O(1)
    def pick_k_random_elements(self, k):
        if k > self.nums:
            return self.nums[:]

        res = self.nums[:k]

        for idx in range(k, len(self.nums)):
            pick_idx = random.randint(0, idx)
            if pick_idx < k:
                res[pick_idx] = self.nums[idx]

        return res


class TestRandomPickIndex(unittest.TestCase):
    def test_random_pick_index(self):
        random_pick_index = RandomPickIndex([1, 2, 3, 3, 3])

        index = random_pick_index.pick(3)
        print("Picked index: ", index)
        self.assertTrue(index == 2 or index == 3 or index == 4)

    def test_random_pick_index_reservoir_sampling(self):
        random_pick_index = RandomPickIndex([1, 2, 3, 3, 3])

        index = random_pick_index.pick_reservoir_sampling(3)
        print("Picked index: ", index)
        self.assertTrue(index == 2 or index == 3 or index == 4)

    def test_random_pick_index_reservoir_sampling(self):
        random_pick_index = RandomPickIndex([6, 8, 2, 1, 3, 10, 4])

        nums_picked = random_pick_index.pick_k_random_elements(3)
        print("Picked numbers: ", nums_picked)
        self.assertTrue(len(nums_picked) == 3)


if __name__ == "__main__":
    unittest.main()
