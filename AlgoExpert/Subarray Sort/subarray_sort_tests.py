import unittest
from subarray_sort import subarray_sort

class SubarraySort(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57], [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]]
        self.subarray_indexes = [[3, 9], [-1, -1], [0, 11], [4, 9]]
        return super().setUp()
    
    def test_generic(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.subarray_indexes[idx], subarray_sort(self.arrays[idx]))

if __name__ == "__main__": unittest.main()