import unittest


# Time: O(n), where n => length of nums
# Space: O(k), where k => size of the window
def contains_duplicate_ii(nums, k):
    window = set()
    lo = 0

    for hi in range(len(nums)):
        if len(window) == k + 1:
            window.remove(nums[lo])
            lo += 1

        if nums[hi] in window:
            return True

        window.add(nums[hi])

    return False


class TestContainsDuplicateII(unittest.TestCase):
    def test_contains_duplicate_ii(self):
        self.assertEqual(contains_duplicate_ii([1, 2, 3, 1, 3, 1], 2), True)
        self.assertEqual(contains_duplicate_ii([1, 2, 3, 1], 3), True)
        self.assertEqual(contains_duplicate_ii([1, 0, 1, 1], 1), True)
        self.assertEqual(contains_duplicate_ii([1, 2, 3, 1, 2, 3], 2), False)


if __name__ == "__main__":
    unittest.main()
