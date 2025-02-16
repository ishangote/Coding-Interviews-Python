import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def max_consecutive_ones_iii(nums, k):
    start = 0
    res, count_0 = 0, 0

    for end in range(len(nums)):
        if nums[end] == 0:
            count_0 += 1
            while start <= end and count_0 > k:
                if nums[start] == 0:
                    count_0 -= 1
                start += 1

        res = max(res, end - start + 1)

    return res


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones_iii(self):
        self.assertEqual(
            max_consecutive_ones_iii([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6
        )

        self.assertEqual(
            max_consecutive_ones_iii(
                [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
            ),
            10,
        )


if __name__ == "__main__":
    unittest.main()
