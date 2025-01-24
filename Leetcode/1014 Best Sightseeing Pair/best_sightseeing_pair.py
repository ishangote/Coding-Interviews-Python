import unittest
import sys


# Time: O(n), where n => number of values
# Space: O(1)
def best_sightseeing_pair(values):
    res = -sys.maxsize
    max_left_score = values[0]

    for idx in range(1, len(values)):
        res = max(res, max_left_score + values[idx] - idx)
        max_left_score = max(max_left_score, values[idx] + idx)

    return res


class TestBestSightseeingPair(unittest.TestCase):
    def test_best_sightseeing_pair(self):
        self.assertEqual(best_sightseeing_pair([8, 1, 5, 2, 6]), 11)
        self.assertEqual(best_sightseeing_pair([1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
