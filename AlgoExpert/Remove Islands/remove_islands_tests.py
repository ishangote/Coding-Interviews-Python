import unittest
from remove_islands import remove_islands
class TestRemoveIslands(unittest.TestCase):
    def setUp(self) -> None:
        self.input_matrix = [[[1, 0, 0, 1, 0],[0, 1, 0, 1, 0],[0, 0, 1, 1, 0]], [[1, 0, 0, 0, 0, 0],[0, 1, 0, 1, 1, 1],[0, 0, 1, 0, 1, 0],[1, 1, 0, 0, 1, 0],[1, 0, 1, 1, 0, 0],[1, 0, 0, 0, 0, 1]]]
        self.output_matrix = [[[1, 0, 0, 1, 0],[0, 0, 0, 1, 0],[0, 0, 1, 1, 0]], [[1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 1, 0],[1, 1, 0, 0, 1, 0],[1, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 1]]]

    def test_generic(self):
        for idx, mat in enumerate(self.input_matrix):
            self.assertEqual(self.output_matrix[idx], remove_islands(mat))

if __name__ == "__main__": unittest.main()