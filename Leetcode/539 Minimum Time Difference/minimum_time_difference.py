import unittest
import sys


# Time: O(nlogn), where n => number of time points
# Space: O(n)
def minimum_time_difference(time_points):
    res = sys.maxsize
    minutes = []

    for points in time_points:
        [hour, minute] = points.split(":")

        minutes.append(int(hour) * 60 + int(minute))

    minutes = sorted(minutes)
    minutes.append(1440 + minutes[0])  # 24:00 = 1440 minutes

    for idx in range(len(minutes) - 1):
        res = min(res, minutes[idx + 1] - minutes[idx])

    return res


class TestMinimumTimeDifference(unittest.TestCase):
    def test_minimum_time_difference(self):
        time_points = ["17:30", "14:30", "00:00", "01:00", "23:59"]
        self.assertEqual(minimum_time_difference(time_points), 1)

        time_points = ["02:00", "22:00"]
        self.assertEqual(minimum_time_difference(time_points), 240)


if __name__ == "__main__":
    unittest.main()
