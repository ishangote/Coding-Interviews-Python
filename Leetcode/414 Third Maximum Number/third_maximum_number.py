import unittest
import heapq


# Time: O(n), where n => length of nums
# Space: O(1)
def third_maximum_number(nums):
    min_heap = []
    min_heap_nums = set()

    for num in nums:
        if num in min_heap_nums:
            continue

        heapq.heappush(min_heap, num)
        min_heap_nums.add(num)

        if len(min_heap_nums) > 3:
            min_heap_nums.remove(heapq.heappop(min_heap))

    return max(min_heap_nums) if len(min_heap_nums) < 3 else heapq.heappop(min_heap)


class TestThirdMaximumNumber(unittest.TestCase):
    def test_third_maximum_number(self):
        self.assertEqual(third_maximum_number([2, 3, 2, 1, 0, 5]), 2)
        self.assertEqual(third_maximum_number([2, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()
