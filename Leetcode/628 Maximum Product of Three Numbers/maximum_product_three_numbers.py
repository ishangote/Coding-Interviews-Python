import unittest
import sys
import heapq


# Time: O(nlogn), where n => length of nums
# Space: O(1)
def maximum_product_sorting(nums):
    nums.sort()
    res = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    return res


# Time: O(n), where n => length of nums
# Space: O(1)
def maximum_product_single_scan(nums):
    max1 = max2 = max3 = -sys.maxsize
    min1 = min2 = sys.maxsize

    for num in nums:
        if num > max1:
            max1, max2, max3 = num, max1, max2

        elif num > max2:
            max2, max3 = num, max2

        elif num > max3:
            max3 = num

        else:
            pass

        if num < min1:
            min1, min2 = num, min1

        elif num < min2:
            min2 = num

        else:
            pass

    return max(max1 * max2 * max3, min1 * min2 * max1)


class TestMaximumProductThreeNumbers(unittest.TestCase):
    def test_maximum_product_sorting(self):
        self.assertEqual(maximum_product_sorting([1, 2, 3]), 6)
        self.assertEqual(maximum_product_sorting([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product_sorting([-1, -2, -3]), -6)
        self.assertEqual(maximum_product_sorting([2, -3, -1, -2, 3]), 18)

    def test_maximum_product_single_scan(self):
        self.assertEqual(maximum_product_single_scan([1, 2, 3]), 6)
        self.assertEqual(maximum_product_single_scan([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product_single_scan([-1, -2, -3]), -6)
        self.assertEqual(maximum_product_single_scan([-100, -98, -1, 2, 3, 4]), 39200)
        self.assertEqual(maximum_product_single_scan([2, -3, -1, -2, 3]), 18)


if __name__ == "__main__":
    unittest.main()
