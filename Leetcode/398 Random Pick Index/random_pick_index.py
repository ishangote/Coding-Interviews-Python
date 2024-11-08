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
        res = -1
        count = 0

        for idx, num in enumerate(self.nums):
            if num == target:
                # Increment count of target occurrences
                count += 1

                # Replace result with the current index with probability 1/count
                if random.randint(1, count) == 1:
                    res = idx

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


if __name__ == "__main__":
    unittest.main()
