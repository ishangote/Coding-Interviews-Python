import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def degree_of_array(nums):
    nums_count = {}
    degree = 1

    for idx, num in enumerate(nums):
        if num not in nums_count:
            nums_count[num] = [1, [idx, idx]]

        else:
            nums_count[num][0] += 1
            degree = max(degree, nums_count[num][0])

            nums_count[num][1][1] = idx

    res = len(nums)
    for num in nums_count:
        if nums_count[num][0] != degree:
            continue

        (first_seen, last_seen) = nums_count[num][1]
        res = min(res, last_seen - first_seen + 1)

    return res


class TestDegreeOfArray(unittest.TestCase):
    def test_degree_of_array(self):
        self.assertEqual(degree_of_array([1, 2, 2, 3, 1]), 2)
        self.assertEqual(degree_of_array([1, 2, 2, 3, 1, 4, 2]), 6)
        self.assertEqual(degree_of_array([0, 2, 0, 1, 2, 3, 4, 1]), 3)


if __name__ == "__main__":
    unittest.main()
