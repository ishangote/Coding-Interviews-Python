# Given an array of n elements, where each element is at most k away from its target position, 
# devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, 
# an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

"""
Examples:
Input : arr[] = {6, 5, 3, 2, 8, 10, 9} k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50} k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
"""

import heapq
def k_messed_sort(nums, k):
    min_heap = []
    for i in range(0, k + 1):
        heapq.heappush(min_heap, nums[i])
    
    pos = 0
    for i in range(k + 1, len(nums)):
        nums[i - (k + 1)] = heapq.heappop(min_heap)
        heapq.heappush(min_heap, nums[i])
        pos += 1

    while min_heap:
        nums[pos] = heapq.heappop(min_heap)
        pos += 1
    
    return nums

import unittest
class TestKMessedSort(unittest.TestCase):
    def test_k_messed_sort_genric(self):
        self.assertEqual(k_messed_sort([6, 5, 3, 2, 8, 10, 9], 3), [2, 3, 5, 6, 8, 9, 10])

if __name__ == "__main__": unittest.main()