import unittest

# * Problem: Previous Greater
# * Direction: Right to Left
# * Stack Type: Decreasing


# Time: O(n), where n => length of nums
# Space: O(n)
def previous_greater_indices(nums):
    res = [-1] * len(nums)
    stack = []

    for idx in range(len(nums) - 1, -1, -1):
        while stack and nums[idx] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


class TestPreviousGreaterIndices(unittest.TestCase):
    def test_previous_greater_indices(self):
        self.assertListEqual(
            previous_greater_indices([2, 1, 2, 4, 3]), [-1, 0, -1, -1, 3]
        )


if __name__ == "__main__":
    unittest.main()
