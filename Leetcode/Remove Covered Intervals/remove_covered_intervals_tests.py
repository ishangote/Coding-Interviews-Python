import unittest
from remove_covered_intervals import remove_intervals

class TestRemoveCoveredIntervals(unittest.TestCase):
    def test_leetcode(self):
        for (intv, length) in [([[1,4],[3,6],[2,8]], 2), ([[1,4],[2,3]], 1), ([[0,10],[5,12]], 2), ([[3,10],[4,10],[5,11]], 2), ([[1,2],[1,4],[3,4]], 1)]:
            self.assertEqual(remove_intervals(intv), length)

if __name__ == "__main__":
    unittest.main()