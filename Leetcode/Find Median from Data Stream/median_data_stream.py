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
        self.left_bucket, self.right_bucket = [], []

    def add_input(self, input):
        if not self.left_bucket or input <= -self.left_bucket[0]:
            heapq.heappush(self.left_bucket, -input)
        else:
            heapq.heappush(self.right_bucket, input)
            
        if len(self.left_bucket) - len(self.right_bucket) == 2:
            heapq.heappush(self.right_bucket, -heapq.heappop(self.left_bucket))
        
        elif len(self.left_bucket) - len(self.right_bucket) == -1:
            heapq.heappush(self.left_bucket, -heapq.heappop(self.right_bucket))

    def find_median(self):
        return -self.left_bucket[0] if len(self.left_bucket) != len(self.right_bucket) else (-self.left_bucket[0] + self.right_bucket[0]) / 2

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