import unittest
from collections import Counter
import heapq


# Time: O(nlogk), where n => length of nums
# Space: O(n)
def top_k_frequent_elements(nums, k):
    min_heap = []
    count_map = Counter(nums)

    for num, count in count_map.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [item[1] for item in min_heap]


class TestTopKFrequentElements(unittest.TestCase):
    def test_top_k_frequent_elements(self):
        self.assertListEqual(top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2), [2, 1])
        self.assertListEqual(top_k_frequent_elements([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
