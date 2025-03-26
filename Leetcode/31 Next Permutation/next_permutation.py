import unittest


def reverse(start, nums):
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# ------------------------------------------------------------------------
# Next Permutation: Finds the next lexicographical permutation.
#
# Steps:
# 1. Identify the pivot: the first element (from the right) that is smaller than its neighbor.
# 2. Find the successor: the smallest element greater than the pivot from the right.
# 3. Swap the pivot with the successor.
# 4. Reverse the suffix (elements to the right of the pivot) to get the smallest order.
def next_permutation(nums):
    # Step 1: Find the pivot (first decreasing element from the right)
    pivot = -1
    for idx in range(len(nums) - 2, -1, -1):
        if nums[idx] < nums[idx + 1]:
            pivot = idx
            break

    # If no pivot found, the array is in descending order (last permutation)
    # Reverse it to get the smallest permutation.
    if pivot == -1:
        reverse(0, nums)
        return nums

    # Step 2: Find the successor (smallest element greater than nums[pivot] from the right)
    for idx in range(len(nums) - 1, pivot, -1):
        if nums[idx] > nums[pivot]:
            nums[idx], nums[pivot] = nums[pivot], nums[idx]
            break

    # Step 3: Reverse the suffix to get the next permutation
    reverse(pivot + 1, nums)
    return nums


# ------------------------------------------------------------------------
# * Variation: Previous Permutation *


def previous_permutation(nums):
    # Step 1: Find the pivot.
    # For previous permutation, we look for the first element from the right that is greater than its neighbor.
    pivot = -1
    for idx in range(len(nums) - 2, -1, -1):
        if nums[idx] > nums[idx + 1]:
            pivot = idx
            break

    # If no pivot is found, the array is already the smallest permutation.
    # Reverse it to obtain the largest permutation.
    if pivot == -1:
        reverse(0, nums)
        return nums

    # Step 2: Find the predecessor.
    # Find the largest element (from the right) that is smaller than the pivot element.
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] < nums[pivot]:
            nums[idx], nums[pivot] = nums[pivot], nums[idx]
            break

    # Step 3: Reverse the suffix starting from pivot+1.
    reverse(pivot + 1, nums)
    return nums


# ------------------------------------------------------------------------
# Unit Tests for next_permutation and previous_permutation


class TestNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        self.assertEqual(next_permutation([2, 1]), [1, 2])
        self.assertEqual(next_permutation([2, 1, 3]), [2, 3, 1])
        self.assertEqual(next_permutation([2, 3, 1, 3, 3]), [2, 3, 3, 1, 3])
        self.assertEqual(next_permutation([1, 3, 2, 4, 6, 5]), [1, 3, 2, 5, 4, 6])
        self.assertEqual(next_permutation([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(next_permutation([2, 2, 3, 3]), [2, 3, 2, 3])


class TestPreviousPermutation(unittest.TestCase):
    def test_previous_permutation(self):
        self.assertEqual(previous_permutation([1, 2]), [2, 1])
        self.assertEqual(previous_permutation([2, 1]), [1, 2])
        self.assertEqual(previous_permutation([1, 3, 2]), [1, 2, 3])
        self.assertEqual(previous_permutation([2, 1, 3]), [1, 3, 2])
        self.assertEqual(previous_permutation([2, 3, 1, 3, 3]), [2, 1, 3, 3, 3])
        self.assertEqual(previous_permutation([1]), [1])
        self.assertEqual(previous_permutation([]), [])


if __name__ == "__main__":
    unittest.main()
