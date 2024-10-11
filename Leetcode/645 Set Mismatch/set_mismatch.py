import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def set_mismatch(nums):
    duplicate, missing = -1, -1

    for idx, num in enumerate(nums):
        if nums[abs(num) - 1] < 0:
            duplicate = abs(num)

        else:
            nums[abs(num) - 1] *= -1

    for idx, num in enumerate(nums):
        if num > 0:
            missing = idx + 1
            break

    return [duplicate, missing]


class TestSetMisMatch(unittest.TestCase):
    def test_set_mismatch(self):
        self.assertListEqual(set_mismatch([4, 2, 2, 1]), [2, 3])
        self.assertListEqual(set_mismatch([1, 1]), [1, 2])
        self.assertListEqual(set_mismatch([2, 2]), [2, 1])


if __name__ == "__main__":
    unittest.main()
