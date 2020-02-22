#Find the kth largest element in an unsorted array. 
#Note that it is the kth largest element in the sorted order, not the kth distinct element.

"""
Brute Force => sort array O(nlogn) and traverse arr till k => O(nlogn)

Appraoch: Keep k largest elements at a given time in a heap => O(logk)

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""

import heapq
def findKthLargest(nums, k):
    if not nums or k <=0 or k > len(nums): return -1
    min_heap = []
    for i, v in enumerate(nums):
        heapq.heappush(min_heap, (v, i))
        if len(min_heap) > k: heapq.heappop(min_heap)
    #If modification to question to return index: return heapq.heappop(min_heap)[1]
    return heapq.heappop(min_heap)[0]

import unittest
class TestKthLargestElementsInArray(unittest.TestCase):
    def edge_case(self):
        self.assertEqual(findKthLargest([], 3), -1)
        self.assertEqual(findKthLargest([3], 3), -1)
        self.assertEqual(findKthLargest([1, 2], -1), -1)

    def test_generic(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 2), 5)

if __name__ == "__main__": unittest.main()