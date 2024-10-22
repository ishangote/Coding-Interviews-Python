import unittest

# * Problem: Next Smaller
# * Direction: Left to Right
# * Stack Type: Increasing


# Time: O(n), where n => length of nums
# Space: O(n)
def next_smaller_indices(nums):
    res = [-1] * len(nums)
    stack = []

    for idx in range(len(nums)):
        while stack and nums[idx] < nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


class TestNextSmallerIndices(unittest.TestCase):
    def test_next_smaller_indices(self):
        self.assertListEqual(next_smaller_indices([2, 1, 2, 4, 3]), [1, -1, -1, 4, -1])


if __name__ == "__main__":
    unittest.main()
