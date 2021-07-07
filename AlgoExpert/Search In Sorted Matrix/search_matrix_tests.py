import unittest
from search_matrix import search_matrix

class TestSearchInSortedMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [[[1, 4, 7, 12, 15, 1000],[2, 5, 19, 31, 32, 1001],[3, 8, 24, 33, 35, 1002],[40, 41, 42, 44, 45, 1003],[99, 100, 103, 106, 128, 1004]]]
        self.targets = [44]
        self.indexes = [[3, 3]]
    
    def test_generic(self):
        for idx, mat in enumerate(self.matrix):    
            self.assertEqual(self.indexes[idx], search_matrix(mat, self.targets[idx]))
    
if __name__ == "__main__": unittest.main()