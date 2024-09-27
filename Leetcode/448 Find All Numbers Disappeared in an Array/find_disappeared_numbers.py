import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def find_disappeared_numbers(nums):
    res = []

    for num in nums:
        # Important check, since it can toggle between marking positive and negative
        if nums[abs(num) - 1] > 0:
            nums[abs(num) - 1] *= -1

    for idx, num in enumerate(nums):
        if num < 0:
            continue

        res.append(idx + 1)

    return res


class TestFindDisappearedNumbers(unittest.TestCase):
    def test_find_disappeared_numbers(self):
        self.assertEqual(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        self.assertEqual(find_disappeared_numbers([1, 1]), [2])


if __name__ == "__main__":
    unittest.main()
