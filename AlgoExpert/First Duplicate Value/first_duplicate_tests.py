import unittest
from brute_first_duplicate_value import brute_first_duplicate_val
from set_first_duplicate_value import set_first_duplicate_val
from optim_first_duplicate_value import optim_first_duplicate_val

class TestFirstDuplicateValue(unittest.TestCase):
    def setUp(self):
        self.arrays = [[2, 1, 5, 2, 3, 3, 4], [6, 15, 7, 10, 9, 14, 10, 1, 10, 1, 2, 11, 1, 6, 8], [2, 1, 5, 3, 3, 2, 4], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 3, 16, 9, 11, 14, 13, 1, 10, 12, 5, 17, 4, 16, 10, 5, 4], [4, 1, 5, 1, 4]]
        self.sols = [2, 10, 3, 2, 16, 1]

    def test_naive(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.sols[idx], brute_first_duplicate_val(arr))

    def test_set(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.sols[idx], set_first_duplicate_val(arr))
    
    def test_optim(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.sols[idx], optim_first_duplicate_val(arr))

if __name__ == "__main__": unittest.main()