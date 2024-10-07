import unittest


# Time: O(n), where n => length of time_series
# Space: O(1)
def teemo_attacking(time_series, duration):
    res = 0

    for idx, time in enumerate(time_series):
        poison_interval = [time, time + duration - 1]

        if idx + 1 != len(time_series) and poison_interval[1] >= time_series[idx + 1]:
            poison_interval[1] = time_series[idx + 1] - 1

        res += poison_interval[1] - poison_interval[0] + 1

    return res


class TestTeemoAttacking(unittest.TestCase):
    def test_teemo_attacking(self):
        self.assertEqual(teemo_attacking([1, 4], 2), 4)
        self.assertEqual(teemo_attacking([1, 3], 3), 5)
        self.assertEqual(teemo_attacking([1, 2], 2), 3)


if __name__ == "__main__":
    unittest.main()
