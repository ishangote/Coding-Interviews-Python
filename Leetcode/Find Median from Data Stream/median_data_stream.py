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
        self.median = -float('inf')
        self.max_heap = []
        self.min_heap = []

    def add_input(self, input):
        # Add input to Min Heap
        if input >= self.median:
            if len(self.min_heap) == 1 + len(self.max_heap):
                num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -num)
            
            heapq.heappush(self.min_heap, input)

        # Add input to Max Heap
        else:
            if len(self.max_heap) == len(self.min_heap):
                num = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num)

            heapq.heappush(self.max_heap, -input)

        self.median = (self.min_heap[0] + -self.max_heap[0]) / 2 if (len(self.min_heap) + len(self.max_heap)) % 2 == 0 else self.min_heap[0]

    def find_median(self):
        return self.median

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