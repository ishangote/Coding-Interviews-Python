import unittest
import heapq


# Time: O(nlogk), where n => length of nums
# Space: O(k)
def kth_largest_element(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return heapq.heappop(min_heap)


class TestKthLargestElementsInArray(unittest.TestCase):
    def edge_case(self):
        self.assertEqual(kth_largest_element([], 3), -1)
        self.assertEqual(kth_largest_element([3], 3), -1)
        self.assertEqual(kth_largest_element([1, 2], -1), -1)

    def test_generic(self):
        self.assertEqual(kth_largest_element([3, 2, 1, 5, 6, 4], 2), 5)


if __name__ == "__main__":
    unittest.main()
