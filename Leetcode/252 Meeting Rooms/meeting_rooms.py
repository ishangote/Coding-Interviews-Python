import unittest


def custom_sort(intervals):
    return sorted(intervals, key=lambda x: x[0])


# Time: O(nlogn), where n => length of intervals
# Space: O(1)
def meeting_rooms_sort(intervals):
    intervals = custom_sort(intervals)

    for idx in range(len(intervals) - 1):
        current_meeting = intervals[idx]
        next_meeting = intervals[idx + 1]

        if current_meeting[1] <= next_meeting[0]:
            continue
        return False

    return True


class TestMeetingRooms(unittest.TestCase):
    def test_meeting_rooms(self):
        self.assertEqual(meeting_rooms_sort([[7, 10], [2, 4]]), True)


if __name__ == "__main__":
    unittest.main()
