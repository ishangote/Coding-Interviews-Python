"""
Hi Ishan
									
[2, 4, -1]		-> [-1, 2, 4]			[-1 1]		(-1 + 1)

What is a median? 
A) Half of the numbers are below the median value and half are above

5, 1, 8, 100, 6, 1000
1, 5, 6, 8, 100, 1000

Median: 7
Half numbers less than median: 1, 5, 6
Half numbers more than median: 8, 100, 1000
Median = (6+8)/2

Stream till now: 5
Sorted: 5
Median: 5
max_heap: {}
min_heap: {5}

Stream till now: 
Sorted: 1, 5
Median: (1+5)/2
max_heap: {1}
min_heap: {5}

Stream till now: 5, 1, 8
Sorted: 1, 5, 8
Median: 5
max_heap: {1}
min_heap: {5, 8}

Stream till now: 5, 1, 8, 100
Sorted: 1, 5, 8, 100
Median: (5+8)/2
max_heap: {1, 5}
min_heap: {8, 100}

Stream till now: 5, 1, 8, 100, 6
Sorted: 1, 5, 6, 8, 100
Median: 6
max_heap: {1, 5}
min_heap: {6, 8, 100}

Stream till now: 5, 1, 8, 100, 6, 1000
Sorted: 1, 5, 6, 8, 100, 1000
Median: (6+8)/2
max_heap: {1, 5, 6}
min_heap: {8, 100, 1000}

Stream till now: 5, 1, 8, 100, 6, 1000, 3
Sorted: 1, 3, 5, 6, 8, 100, 1000
Median: 6
max_heap: {1, 3, 5}
min_heap: {6, 8, 100, 1000}100


Pseudo Code:
if input >= median: 
  if len(min_heap) == 1 + len(max_heap): min_to_max()
  add input to min_heap
  
else:
	if len(max_heap) == len(min_heap):	max_to_min()
  add input to max_heap
	
if len(min_heap) + len(max_heap) % 2 == 0
	median = (peek_min_heap + peek_max_heap) / 2
else:
	median = peek_min_heap
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

"""
TEST CASES:

CASE L70
Stream: 3, 1
Median = 2
max_heap: [1] <- {1}	    		
min_heap: [3] <- {3}

Input = 2
max_heap: [1] <- {1}	    		
min_heap: [2] <- {2, 3}


CASE: L69
Stream: 3, 1, 2
Median = 2
max_heap: [2] <- {1, 2}	    		
min_heap: [2] <- {2, 3}

Input = 2

CASE L77:
Stream: 3, 1
Median = 2
max_heap: [1] <- {1}	    		
min_heap: [3] <- {3}

Input = 1

max_heap: [1] <- {1}	    		
min_heap: [1] <- {1, 3}
"""

"""
Feedback:
Behavioral/Resume Review:
What kind of RA?
Genetic algorithms?
Optimization algorithms based on mutation or crossover theories. 

Coding interview:
Initial example was very small.
Initial example was not properly written.
Ideally it should be written like this:

Median definition not clear:
What is a median? -> Half of the numbers are below the median value and half are above

Duplicates issue not found out.

Jumped into data structures rather than stating brute force
DID NOT STATE BRUTE FORCE!!!!

Self centric => 
"I would have to"
"If I add".. Lot of I's again as usual. No change.
"Hence I'll store.."
"I will have to transfer"
"I think that 1 heap will store ... I told you that!!" 

You should say is this what you thinking about?
Language is so memory based
"we have to do"
"Should I always"

Horizontal writing KILLS you
Most of your time goes in tabs and spaces to verticle align. Annoying!!
Do not be conservative of the screen, kept the linked list example there only!!

In case of odd elements, extra element goes in min_heap  --> DID NOT MENTION
"""