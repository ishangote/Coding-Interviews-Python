"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_input(self, input):
        if not self.min_heap or input >= self.min_heap[0]: heapq.heappush(self.min_heap, input)
        else: heapq.heappush(self.max_heap, -input)

        # Balance Heaps
        if len(self.min_heap) - len(self.max_heap) == 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        elif len(self.max_heap) - len(self.min_heap) == 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def find_median(self):
        #Even Case
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]

import unittest
class TestMedianDataStream(unittest.TestCase):
    def test_case_L(self):
        median_finder = MedianFinder()

        median_finder.add_input(3)
        self.assertEqual(median_finder.find_median(), 3)
        median_finder.add_input(1)
        self.assertEqual(median_finder.find_median(), 2)
        median_finder.add_input(2)
        self.assertEqual(median_finder.find_median(), 2)
        median_finder.add_input(-1)
        self.assertEqual(median_finder.find_median(), 1.5)
        median_finder.add_input(2)
        self.assertEqual(median_finder.find_median(), 2)
        median_finder.add_input(5)
        self.assertEqual(median_finder.find_median(), 2)
        
if __name__ == "__main__": unittest.main()