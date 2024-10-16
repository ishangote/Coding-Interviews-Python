import unittest


def longest_subarray_helper(lo, hi, first_negative, last_negative, count_negatives):
    if count_negatives % 2 == 0:
        return hi - lo + 1

    return max((last_negative - 1) - lo, hi - (first_negative + 1)) + 1


# Time: O(n), where n => length of nums
# Space: O(1)
def longest_positive_product_subarray(nums):
    count_negatives = 0
    first_negative, last_negative = -1, -1
    lo, hi = 0, 0
    res = 0

    while hi < len(nums):
        if nums[hi] == 0:
            res = max(
                res,
                longest_subarray_helper(
                    lo, hi - 1, first_negative, last_negative, count_negatives
                ),
            )
            lo = hi + 1
            count_negatives = 0
            first_negative, last_negative = -1, -1

        else:
            if nums[hi] < 0:
                count_negatives += 1

                if first_negative == -1:
                    first_negative = hi
                last_negative = hi

            res = max(
                res,
                longest_subarray_helper(
                    lo, hi, first_negative, last_negative, count_negatives
                ),
            )

        hi += 1

    return res


class TestLongestPositiveProductSubarray(unittest.TestCase):
    def test_longest_positive_product_subarray_edge(self):
        self.assertEqual(longest_positive_product_subarray([1]), 1)
        self.assertEqual(longest_positive_product_subarray([0]), 0)
        self.assertEqual(longest_positive_product_subarray([0, 0]), 0)
        self.assertEqual(longest_positive_product_subarray([-1]), 0)

    def test_longest_positive_product_subarray(self):
        self.assertEqual(longest_positive_product_subarray([1, -2, -3, 4]), 4)
        self.assertEqual(longest_positive_product_subarray([0, 1, -2, -3, -4]), 3)
        self.assertEqual(longest_positive_product_subarray([-1, -2, -3, 0, 1]), 2)
        self.assertEqual(longest_positive_product_subarray([-5, -13, 2, 6, 0]), 4)
        self.assertEqual(
            longest_positive_product_subarray([-17, -9, 17, -3, -5, -13, 2, 6, 0]), 7
        )


if __name__ == "__main__":
    unittest.main()
