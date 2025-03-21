import unittest


class SparseVector:
    # Time: O(m), where m => number of non-zero integers in nums
    # Space: O(n)
    def __init__(self, nums):
        self.index_map = {idx: num for idx, num in enumerate(nums) if num != 0}

    # Time: O(m), where m => number of non-zero integers in nums
    # Space: O(1)
    def dotProduct(self, vec):
        res = 0
        smaller_map, larger_map = self.index_map, vec.index_map

        if len(self.index_map) > len(vec.index_map):
            smaller_map, larger_map = vec.index_map, self.index_map

        for idx, num in smaller_map.items():
            if idx in larger_map:
                res += num * larger_map[idx]

        return res


class TestSparseVector(unittest.TestCase):
    def test_sparse_vector(self):
        nums1 = SparseVector([1, 0, 0, 2, 3])
        nums2 = SparseVector([0, 3, 0, 4, 0])

        self.assertEqual(nums1.dotProduct(nums2), 8)


if __name__ == "__main__":
    unittest.main()
