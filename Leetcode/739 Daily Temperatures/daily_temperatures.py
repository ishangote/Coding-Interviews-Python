import unittest


# Time: O(n), where n => number of temperatures
# Space: O(n)
def daily_temperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for idx in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[idx]:
            idx_to_update = stack.pop()
            res[idx_to_update] = idx - idx_to_update

        stack.append(idx)

    return res


class TestDailyTemperatures(unittest.TestCase):
    def test_daily_temperatures(self):
        self.assertListEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertListEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertListEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])


if __name__ == "__main__":
    unittest.main()
