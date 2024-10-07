import unittest


# Time: O(nlogn) where n => length of scores
# Space: O(n)
def relative_ranks_brute_force(scores):
    res = [""] * len(scores)
    score_idx_map = [(score, idx) for idx, score in enumerate(scores)]

    score_idx_map.sort(reverse=True, key=lambda x: x[0])

    for rank, (score, idx) in enumerate(score_idx_map):
        if rank == 0:
            res[idx] = "Gold Medal"

        elif rank == 1:
            res[idx] = "Silver Medal"

        elif rank == 2:
            res[idx] = "Bronze Medal"

        else:
            res[idx] = str(rank + 1)

    return res


class TestRelativeRanks(unittest.TestCase):
    def test_relative_ranks_brute_force(self):
        self.assertEqual(
            relative_ranks_brute_force([5, 4, 3, 2, 1]),
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        )

        self.assertEqual(
            relative_ranks_brute_force([10, 3, 8, 9, 4]),
            ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
        )


if __name__ == "__main__":
    unittest.main()
