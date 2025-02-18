import unittest


def reverse(start, nums):
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# Time: O(n), where n => length of nums
# Space: O(1)
def next_permutation(nums):
    # Step 1: Find the pivot (first decreasing element from the right)
    pivot = -1
    for idx in range(len(nums) - 2, -1, -1):
        if nums[idx] < nums[idx + 1]:
            pivot = idx
            break

    # If no pivot found, reverse the entire array (last permutation case)
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


class TestNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        self.assertEqual(next_permutation([2, 1]), [1, 2])
        self.assertEqual(next_permutation([2, 1, 3]), [2, 3, 1])
        self.assertEqual(next_permutation([2, 3, 1, 3, 3]), [2, 3, 3, 1, 3])
        self.assertEqual(next_permutation([1, 3, 2, 4, 6, 5]), [1, 3, 2, 5, 4, 6])
        self.assertEqual(next_permutation([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(next_permutation([2, 2, 3, 3]), [2, 3, 2, 3])


if __name__ == "__main__":
    unittest.main()
