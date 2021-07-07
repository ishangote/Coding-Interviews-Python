import unittest
from minimm_passes_matrix import minimum_passes
class TestMinimumMatrixPasses(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [[[-2, 0, -2, 1],[-2, -1, -1, -1]], [[1, 0, 0, -2, -3],[-4, -5, -6, -2, -1],[0, 0, 0, 0, -1],[-1, 0, 3, 0, 3]]]
        self.passes = [5, -1]

    def test_generic(self):
        for idx, mat in enumerate(self.matrix):
            self.assertEqual(self.passes[idx], minimum_passes(mat))

if __name__ == "__main__": unittest.main()