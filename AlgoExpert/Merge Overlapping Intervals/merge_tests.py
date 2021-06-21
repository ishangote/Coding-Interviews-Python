import unittest
from merge_overlapping import merge_intervals

class TestMergeOverlappingIntervals(unittest.TestCase):
    def test_generic(self):
        self.assertEqual([[1, 2], [3, 8], [9, 10]], merge_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
        self.assertEqual([[1, 10]], merge_intervals([[1, 10]]))
        self.assertEqual([[-50, 20], [70, 95]], merge_intervals([[89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]]))
        self.assertEqual([[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]], merge_intervals([[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]]))
        self.assertEqual([[0, 1]], merge_intervals([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]))

if __name__ == "__main__": unittest.main()

