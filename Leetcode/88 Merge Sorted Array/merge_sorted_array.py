import unittest


# Time: O(m + n), where m => length of nums1 and n => length of nums 2
# Space: O(1)
def merge_sorted_array(nums1, len1, nums2, len2):
    pt1, pt2, cur = len1 - 1, len2 - 1, (len1 + len2) - 1

    while pt1 >= 0 and pt2 >= 0:
        if nums1[pt1] >= nums2[pt2]:
            nums1[cur] = nums1[pt1]
            pt1 -= 1
        else:
            nums1[cur] = nums2[pt2]
            pt2 -= 1

        cur -= 1

    while pt1 >= 0:
        nums1[cur] = nums1[pt1]
        pt1 -= 1
        cur -= 1

    while pt2 >= 0:
        nums1[cur] = nums2[pt2]
        pt2 -= 1
        cur -= 1

    return


class TestMergeSortedArray(unittest.TestCase):
    def test_nums1_empty(self):
        nums1, len1 = [0, 0, 0], 0
        nums2, len2 = [2, 3, 4], 3

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [2, 3, 4])

    def test_nums2_empty(self):
        nums1, len1 = [2, 3, 4], 0
        nums2, len2 = [], 0

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [2, 3, 4])

    def test_merge_sorted_array_example1(self):
        nums1, len1 = [1, 2, 3, 0, 0, 0], 3
        nums2, len2 = [2, 5, 6], 3

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
