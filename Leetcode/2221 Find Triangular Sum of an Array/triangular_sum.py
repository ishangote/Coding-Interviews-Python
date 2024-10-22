import unittest


def helper(nums):
    res = []

    for idx in range(0, len(nums) - 1):
        res.append((nums[idx] + nums[idx + 1]) % 10)

    return res


# Time: O(n^2), where n => length of nums
# Space: O(n)
def triangular_sum_brute_force(nums):
    while len(nums) > 1:
        nums = helper(nums)

    return nums[0]


class TestTriangularSum(unittest.TestCase):
    def test_triangular_sum(self):
        self.assertEqual(triangular_sum_brute_force([1, 2, 3, 4, 5]), 8)
        self.assertEqual(triangular_sum_brute_force([5]), 5)


if __name__ == "__main__":
    unittest.main()
