import unittest
import random


class RandomPickWithWeight:
    # Time: O(n), where n => length of weights,
    # Space: O(n)
    def __init__(self, weights):
        self.prefix_sums = [weights[0]]

        for idx in range(1, len(weights)):
            self.prefix_sums.append(self.prefix_sums[idx - 1] + weights[idx])

    # Time: O(n), where n => length of weights
    # Space: O(1)
    def pick_index_linear(self):
        pick = random.randint(0, self.prefix_sums[-1] - 1)

        for idx, prefix_sum in enumerate(self.prefix_sums):
            if pick < prefix_sum:
                return idx

    def binary_search_helper(self, pick):
        lo, hi = 0, len(self.prefix_sums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if self.prefix_sums[mid] > pick:
                hi = mid
            elif self.prefix_sums[mid] <= pick:
                lo = mid + 1

        return lo

    # Time: O(logn), where n => length of weights
    # Space: O(1)
    def pick_index_binary_search(self):
        pick = random.randint(0, self.prefix_sums[-1] - 1)

        return self.binary_search_helper(pick)


class TestRandomPickWithWeight(unittest.TestCase):
    def test_random_pick_with_weight_linear(self):
        random_pick = RandomPickWithWeight([2, 1, 4])
        pick = random_pick.pick_index_linear()

        print("Picked index: ", pick)

        self.assertTrue(pick == 0 or pick == 1 or pick == 2)

    def test_random_pick_with_weight_binary_search(self):
        random_pick = RandomPickWithWeight([2, 1, 4])
        pick = random_pick.pick_index_binary_search()

        print("Picked index: ", pick)

        self.assertTrue(pick == 0 or pick == 1 or pick == 2)


if __name__ == "__main__":
    unittest.main()
