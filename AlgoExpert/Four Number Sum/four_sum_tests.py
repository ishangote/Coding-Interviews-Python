import unittest
from four_sum import four_sum

class TestFourSum(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[7, 6, 4, -1, 1, 2], [1, 2, 3, 4, 5, -5, 6, -6]]
        self.targets = [16, 5]
        self.quads = [[[-1, 4, 6, 7], [1, 2, 6, 7]], [[-6, 1, 4, 6], [-6, 2, 3, 6], [-6, 2, 4, 5], [-5, 1, 3, 6], [-5, 1, 4, 5], [-5, 2, 3, 5]]]

    def test_generic(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.quads[idx], four_sum(arr, self.targets[idx]))

if __name__ == "__main__": unittest.main()