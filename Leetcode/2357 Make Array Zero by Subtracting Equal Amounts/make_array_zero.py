import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def make_array_zero(nums):
    nums_set = set(nums)
    nums_set.discard(0)

    return len(nums_set)


class TestMakeArrayZero(unittest.TestCase):
    def test_make_array_zero(self):
        self.assertEqual(make_array_zero([1, 5, 0, 3, 5]), 3)
        self.assertEqual(make_array_zero([0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
