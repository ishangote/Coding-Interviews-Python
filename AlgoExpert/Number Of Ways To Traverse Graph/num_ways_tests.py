import unittest
from num_ways import *

class TestNumberOfWaysToTraverseGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.widths = [3, 2, 5, 5, 5, 2, 9]
        self.heights = [4, 3, 5, 6, 7, 10, 5]
        self.ways = [10, 3, 70, 126, 210, 10, 495]
    
    def test_naive(self):
        for idx, ans in enumerate(self.ways):
            self.assertEqual(ans, num_ways_naive(self.widths[idx], self.heights[idx]))
    
    def test_space_optim(self):
        for idx, ans in enumerate(self.ways):
            self.assertEqual(ans, num_ways_space_optim(self.widths[idx], self.heights[idx]))
    
    def test_time_optim(self):
        for idx, ans in enumerate(self.ways):
            self.assertEqual(ans, num_ways_time_optim(self.widths[idx], self.heights[idx]))

if __name__ == "__main__": unittest.main()