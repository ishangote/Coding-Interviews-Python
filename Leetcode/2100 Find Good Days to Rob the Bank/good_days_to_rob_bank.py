import unittest


# Time: O(n), where n => length of security
# Space: O(n)
def good_days_to_rob_bank(security, time):
    res = []
    num_days_before, num_days_after = [0] * len(security), [0] * len(security)

    for idx in range(1, len(security)):
        if security[idx - 1] >= security[idx]:
            num_days_before[idx] = num_days_before[idx - 1] + 1

        continue

    for idx in range(len(security) - 2, -1, -1):
        if security[idx] <= security[idx + 1]:
            num_days_after[idx] = num_days_after[idx + 1] + 1

        continue

    for idx in range(len(security)):
        if num_days_before[idx] >= time and num_days_after[idx] >= time:
            res.append(idx)

        continue

    return res


class TestGoodDaysToRobBank(unittest.TestCase):
    def test_good_days_to_rob_bank(self):
        self.assertEqual(good_days_to_rob_bank([5, 3, 3, 3, 5, 6, 2], 2), [2, 3])
        self.assertEqual(good_days_to_rob_bank([1, 2, 3, 4, 5, 6], 2), [])
        self.assertEqual(
            good_days_to_rob_bank([1, 1, 1, 1, 1, 1, 1], 0), [0, 1, 2, 3, 4, 5, 6]
        )


if __name__ == "__main__":
    unittest.main()
