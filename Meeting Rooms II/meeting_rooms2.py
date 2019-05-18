# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""
[1, 4], [3, 7], [7, 15], [20, 25]

Approach1:

timeline = [s:1, e:4, s:3, e:7, s:7, e:15, s:20, e:25]
timeline = [s:1, s:3, e:4, e:7, s:7, e:15, s:20, e:25]
                                                 ^
count       1    2    1    0    1    0     1     0

return max(count)

Approach2:
heap = []

        [1, 4], [3, 7], [7, 15], [20, 25]
                                  ^
heap    [4]     [4, 7]  [7, 15]  len([15, 20]) = 2

"""

# Solution not requiring heap ...
def meeting_rooms_ii(intervals):

    if not intervals: return None
    if len(intervals) == 0 or len(intervals) == 1: return len(intervals)
    
    timeline = []
    for interval in intervals:
        timeline.append(["start", interval[0]])
        timeline.append(["end", interval[1]])

    # sort timeline tuples by time first then by 'start' or 'end' tag
    # e.g. ('end', 13) < ('start', 13)
    timeline.sort(key = lambda x:(x[1], x[0]))
    # print(timeline)

    max_rooms = 0
    curr_rooms = 0
    for time in timeline:
        if time[0] == "start":
            curr_rooms += 1
            if curr_rooms > max_rooms: max_rooms = curr_rooms
        else: curr_rooms -= 1
        
    return max_rooms

#-------------------------------------------------------------

#Solution with heap
import heapq
def meeting_rooms_ii_heap(intervals):
    intervals.sort(key = lambda x:x[0])
    heap = []

    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            heapq.heapreplace(heap, interval[1])

        else:
            heapq.heappush(heap, interval[1])
    
    return len(heap)

#-------------------------------------------------------------
#TESTING...

import unittest
class TestMeetingRoomsII(unittest.TestCase):

    def test_one_meeting(self):
        self.assertEqual(meeting_rooms_ii([[1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[1, 13]]), 1)

    def test_meeting_rooms(self):
        self.assertEqual(meeting_rooms_ii([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(meeting_rooms_ii([[7, 10], [2, 4]]), 1)
        self.assertEqual(meeting_rooms_ii([[13, 15], [1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii([[1, 4], [3, 7], [7, 15], [20, 25]]), 3)

        self.assertEqual(meeting_rooms_ii_heap([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(meeting_rooms_ii_heap([[7, 10], [2, 4]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[13, 15], [1, 13]]), 1)
        self.assertEqual(meeting_rooms_ii_heap([[1, 4], [3, 7], [7, 15], [20, 25]]), 3)

if __name__ == "__main__": unittest.main()