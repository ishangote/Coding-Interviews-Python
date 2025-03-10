import unittest


# Time: O(n*n!), where n => length of nums
# Space: O(n) (not considering result) else O(n*n!)
def permutations(nums):
    res = []

    def backtrack(res, cur, nums):
        if len(cur) == len(nums):
            res.append(list(cur))

        else:
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(res, cur, nums)
                    cur.pop()

    backtrack(res, [], nums)
    return res


class TestPermutations(unittest.TestCase):
    def test_generic(self):
        self.assertListEqual(
            permutations([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )
        self.assertListEqual(
            permutations([0, 1]),
            [[0, 1], [1, 0]],
        )
        self.assertListEqual(
            permutations([1]),
            [[1]],
        )


if __name__ == "__main__":
    unittest.main()
