import unittest

# * Problem: Previous Smaller
# * Direction: Right to Left
# * Stack Type: Increasing


# Time: O(n), where n => length of nums
# Space: O(n)
def previous_smaller_indices(nums):
    res = [-1] * len(nums)
    stack = []

    for idx in range(len(nums) - 1, -1, -1):
        while stack and nums[idx] < nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


class TestPreviousSmallerIndices(unittest.TestCase):
    def test_previous_smaller_indices(self):
        self.assertListEqual(
            previous_smaller_indices([2, 1, 2, 4, 3]), [-1, -1, 1, 2, 2]
        )


if __name__ == "__main__":
    unittest.main()
