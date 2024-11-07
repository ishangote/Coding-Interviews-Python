import unittest
import heapq


# Time: O(nlogn), where n => length of s
# Space: O(n)
def custom_sort_string(order, input_string):
    res = []
    min_heap = []

    for char in input_string:
        if char not in order:
            res.append(char)

        else:
            heapq.heappush(min_heap, (order.index(char), char))

    while min_heap:
        res.append(heapq.heappop(min_heap)[1])

    return "".join(res)


class TestCustomSortString(unittest.TestCase):
    def test_custom_sort_string(self):
        self.assertEqual(custom_sort_string("bcafg", "abcd"), "dbca")
        self.assertEqual(custom_sort_string("bcafg", "xyz"), "xyz")
        self.assertEqual(custom_sort_string("bcafg", "gfacb"), "bcafg")


if __name__ == "__main__":
    unittest.main()
