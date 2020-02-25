"""
Given an array of numbers, write an algorithm to find the index of the kth largest number.
1,3,4,8,5,2
k = 2 should return 4 because 5 is the 2nd largest number.

0 1 2 3 4 5
1,3,4,8,5,2  k = 2
          ^
heap = [(5, 4), 8]

0 1 2 3 4 5			[3, 3, 5, 8]			k = 4
1,3,3,8,5,2

[2, 5,8] k = 4
"""
import heapq
def kth_largest(arr, k):
    if not arr or k <= 0 or k > len(arr): return -1
    min_heap = []
    for i, v in enumerate(arr):
        heapq.heappush(min_heap, (v, i))
        if len(min_heap) > k: heapq.heappop(min_heap)
    
    return heapq.heapop(min_heap)[1]

"""
TESTING
[2] k = 1

i v  []
0 1
1 -2
 
[1, -2, 3]		k = 3 		=> 1 (index of 1)

[(1, 0) (3, 2)]

[1, 5, 8, 2]		
"""
"""
Follow Up Questions:
def heappush(heap, val, index):
def balance_heap(heap, val):

"""
"""
Feedback:
Leadership:
Intro: succinct: Why looking job -> one sentence -> Not needed
Research -> first sentence about lab (More lab focused) -> What you are researching/investigating/GA<->ML/What your paper is trying to do?
You specically did what? -> Your impact -> What you did to meet those small deadlines -> You asked for help/manager -> YOu worked despite tight deadline
Website not managed -> developed/created a website...

Red FLAG: CTCI task Binary Heap -> Data Structures spend some time
handle edge cases -> time?
1. Duplicates, questions
2. Heap Node
"""