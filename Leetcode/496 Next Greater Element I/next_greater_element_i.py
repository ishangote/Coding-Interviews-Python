import unittest


# Time: O(n * m), where n => length of nums1 and m => length of nums2
# Space: O(n)
def next_greater_element(nums1, nums2):
    nums1_idx_map = {num: idx for idx, num in enumerate(nums1)}
    res = [-1] * len(nums1)

    for idx in range(len(nums2)):
        if nums2[idx] not in nums1_idx_map:
            continue

        for runner in range(idx + 1, len(nums2)):
            if nums2[runner] > nums2[idx]:
                res[nums1_idx_map[nums2[idx]]] = nums2[runner]
                break

    return res


# Time: O(n + m), where n => length of nums1, and m => length of nums2
# Space: O(n)
def next_greater_element_mono(nums1, nums2):
    nums1_idx_map = {num: idx for idx, num in enumerate(nums1)}
    mono_stack, res = [], [-1] * len(nums1)

    for num in nums2:
        while mono_stack and num > mono_stack[-1]:
            val = mono_stack.pop()
            res[nums1_idx_map[val]] = num

        if num in nums1_idx_map:
            mono_stack.append(num)

    return res


class TestNextGreaterElementI(unittest.TestCase):
    def test_next_greater_element_brute_force(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])

    def test_next_greater_element_mono(self):
        self.assertEqual(
            next_greater_element_mono([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]
        )


if __name__ == "__main__":
    unittest.main()
