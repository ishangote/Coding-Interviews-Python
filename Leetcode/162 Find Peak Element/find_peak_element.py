import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def find_peak_element_brute_force(nums):
    for idx in range(len(nums) - 1):
        if nums[idx] < nums[idx + 1]:
            continue

        return idx

    return len(nums) - 1


# Time: O(logn), where n => length of nums
# Space: O(1)
def find_peak_element_binary_search(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return lo


# ** Variation: Find Valley Element **
# Time: O(logn), where n => length of nums
# Space: O(1)
def find_valley_element_binary_search(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] < nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return lo


class TestFindPeakElement(unittest.TestCase):
    def test_find_peak_element_brute_force(self):
        self.assertEqual(find_peak_element_brute_force([9, 8, 6, 5]), 0)
        self.assertEqual(find_peak_element_brute_force([5, 6, 8, 9]), 3)
        self.assertEqual(find_peak_element_brute_force([1, 2, 1, 3, 5, 6, 4]), 1)
        self.assertEqual(find_peak_element_brute_force([1, 2, 5, 3, 1, 2, 3]), 2)

    def test_find_peak_element_binary_search(self):
        self.assertEqual(find_peak_element_binary_search([9, 8, 6, 5]), 0)
        self.assertEqual(find_peak_element_binary_search([5, 6, 8, 9]), 3)
        self.assertEqual(find_peak_element_binary_search([1, 2, 1, 3, 5, 6, 4]), 5)
        self.assertEqual(find_peak_element_binary_search([1, 2, 5, 3, 1, 2, 3]), 2)


class TestFindValleyElement(unittest.TestCase):
    def test_valley_v_shape(self):
        self.assertEqual(find_valley_element_binary_search([9, 6, 3, 4, 8]), 2)

    def test_descending_array(self):
        self.assertEqual(find_valley_element_binary_search([9, 8, 7, 6]), 3)

    def test_ascending_array(self):
        self.assertEqual(find_valley_element_binary_search([1, 2, 3, 4]), 0)

    def test_single_element(self):
        self.assertEqual(find_valley_element_binary_search([10]), 0)

    def test_valley_with_symmetry(self):
        self.assertEqual(find_valley_element_binary_search([5, 3, 2, 3, 5]), 2)


if __name__ == "__main__":
    unittest.main()
