import unittest
import heapq
from collections import defaultdict


class SlidingWindowMedianHelper:
    def __init__(self, window_size):
        self.max_heap = []
        self.min_heap = []
        self.window_size = window_size
        self.max_heap_size = 0
        self.min_heap_size = 0
        self.deletions = defaultdict(int)

    def add(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
        self.make_balance()

    def remove(self, num):
        self.deletions[num] += 1
        if self.max_heap and num <= -self.max_heap[0]:
            self.max_heap_size -= 1
            # If the element to be removed is exactly at the top, prune it immediately.
            if num == -self.max_heap[0]:
                self.prune(self.max_heap)

        else:
            self.min_heap_size -= 1
            # Similarly, if it is at the top of the min_heap, remove it.
            if self.min_heap and num == self.min_heap[0]:
                self.prune(self.min_heap)

        self.make_balance()

    def prune(self, heap):
        # Remove elements from the top of the heap if they are marked for deletion.
        while heap:
            if heap is self.max_heap:
                current = -self.max_heap[0]
            else:
                current = self.min_heap[0]

            if self.deletions[current] > 0:
                self.deletions[current] -= 1
                heapq.heappop(heap)

            else:
                break

    def make_balance(self):
        # Balance the heaps such that max_heap may contain one extra element.
        if self.max_heap_size > self.min_heap_size + 1:
            num = -heapq.heappop(self.max_heap)
            self.max_heap_size -= 1
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
            self.prune(self.max_heap)

        elif self.max_heap_size < self.min_heap_size:
            num = heapq.heappop(self.min_heap)
            self.min_heap_size -= 1
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
            self.prune(self.min_heap)

    def get_median(self):
        if self.window_size % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


# Time: O(nlogk), where n => length of nums
# Space: O(k)
def sliding_window_median(nums, k):
    res = []
    helper = SlidingWindowMedianHelper(k)

    for idx, num in enumerate(nums):
        helper.add(num)
        if idx >= k - 1:
            res.append(helper.get_median())
            outgoing = nums[idx - k + 1]
            helper.remove(outgoing)

    return res


class TestSlidingWindowMedian(unittest.TestCase):
    def test_sliding_window_median(self):
        self.assertListEqual(
            sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000],
        )
        self.assertListEqual(
            sliding_window_median([1, 2, 3, 4, 2, 3, 1, 4, 2], 3),
            [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000],
        )

    def test_single_element_window(self):
        # When window size is 1, each element is its own median.
        self.assertListEqual(
            sliding_window_median([5, -1, 3, 8, 2], 1),
            [5.00000, -1.00000, 3.00000, 8.00000, 2.00000],
        )

    def test_window_equals_array_length(self):
        # When the window covers the entire array, there is only one median.
        self.assertListEqual(
            sliding_window_median([4, 1, 7, 2, 5], 5),
            [4.00000],
        )

    def test_all_elements_same(self):
        # All elements are the same, so the median remains the same.
        self.assertListEqual(
            sliding_window_median([3, 3, 3, 3, 3, 3], 3),
            [3.00000, 3.00000, 3.00000, 3.00000],
        )


if __name__ == "__main__":
    unittest.main()
