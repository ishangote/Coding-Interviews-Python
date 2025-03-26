import unittest
import heapq


# Time: O(nlogn), where n => number of events
# Space: O(n)
def meeting_rooms_ii(intervals):
    if not intervals:
        return 0

    events = []
    for interval in intervals:
        events.append((interval[0], 1))
        events.append((interval[1], -1))

    rooms, res = 0, 0
    for event in sorted(events):
        rooms += event[1]
        res = max(res, rooms)

    return res


# -------------------------------------------------------------


# Time: O(nlogn), where n => length of intervals
# Space: O(n)
def meeting_rooms_ii_heap(intervals):
    intervals.sort(key=lambda x: x[0])
    latest_end_times = []

    for intr in intervals:
        if latest_end_times and intr[0] >= latest_end_times[0]:
            # Pop and return the smallest item from the heap, and also push the new item.
            heapq.heapreplace(latest_end_times, intr[1])

        else:
            heapq.heappush(latest_end_times, intr[1])

    return len(latest_end_times)


# -------------------------------------------------------------


class TestMeetingRoomsII(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(meeting_rooms_ii_heap([]), 0)

    def test_one_meeting(self):
        self.assertEqual(meeting_rooms_ii([[1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[1, 13]]), 1)

    def test_meeting_rooms(self):
        self.assertEqual(meeting_rooms_ii([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(meeting_rooms_ii([[7, 10], [2, 4]]), 1)
        self.assertEqual(meeting_rooms_ii([[13, 15], [1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii([[1, 4], [3, 7], [7, 15], [20, 25]]), 2)

        self.assertEqual(meeting_rooms_ii_heap([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(meeting_rooms_ii_heap([[7, 10], [2, 4]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[13, 15], [1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[1, 4], [3, 7], [7, 15], [20, 25]]), 2)


if __name__ == "__main__":
    unittest.main()
