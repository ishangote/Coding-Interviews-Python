import unittest
from cycle_directed import is_cyclic
class TestCycleInGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graphs = [[[1, 3],[2, 3, 4],[0],[],[2, 5],[]], [[],[0, 3],[0],[1, 2]], [[0]], [[1],[2, 3, 4, 5, 6, 7],[],[2, 7],[5],[],[4],[0]], [[],[0, 2],[0, 3],[0, 4],[0, 5],[0]], [[1],[2, 3, 4, 5, 6, 7],[],[2, 7],[5],[],[4],[]]]
        self.is_cyclic = [True, True, True, True, False, False]

    def test_generic(self):
        for idx, edges in enumerate(self.graphs):
            self.assertEqual(self.is_cyclic[idx], is_cyclic(edges))

if __name__ == "__main__": unittest.main()