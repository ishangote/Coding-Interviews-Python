import unittest


def binary_search_first_occurrence_helper(nums, lo, hi, target):
    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo if lo < len(nums) and nums[lo] == target else -1


def binary_search_last_occurrence_helper(nums, lo, hi, target):
    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1

    return lo - 1 if lo - 1 >= 0 and nums[lo - 1] == target else -1


# Time: O(logn), where n => length of nums
# Space: O(1)
def find_first_and_last_position(nums, target):
    first_occurrence_idx = binary_search_first_occurrence_helper(
        nums, 0, len(nums), target
    )

    if first_occurrence_idx == -1:
        return [-1, -1]

    last_occurrence_idx = binary_search_last_occurrence_helper(
        nums, first_occurrence_idx, len(nums), target
    )

    return [first_occurrence_idx, last_occurrence_idx]


class TestFirstAndLastPositionOfElementInSortedArray(unittest.TestCase):
    def test_target_in_middle(self):
        nums = [1, 2, 2, 2, 3, 4]
        target = 2
        self.assertEqual(find_first_and_last_position(nums, target), [1, 3])

    def test_target_at_beginning(self):
        nums = [2, 2, 3, 4, 5]
        target = 2
        self.assertEqual(find_first_and_last_position(nums, target), [0, 1])

    def test_target_at_end(self):
        nums = [1, 2, 3, 4, 4, 4]
        target = 4
        self.assertEqual(find_first_and_last_position(nums, target), [3, 5])

    def test_target_not_found(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(find_first_and_last_position(nums, target), [-1, -1])

    def test_empty_list(self):
        nums = []
        target = 1
        self.assertEqual(find_first_and_last_position(nums, target), [-1, -1])

    def test_single_element_found(self):
        nums = [5]
        target = 5
        self.assertEqual(find_first_and_last_position(nums, target), [0, 0])

    def test_single_element_not_found(self):
        nums = [5]
        target = 3
        self.assertEqual(find_first_and_last_position(nums, target), [-1, -1])


if __name__ == "__main__":
    unittest.main()
