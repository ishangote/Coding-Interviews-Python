import unittest
import heapq


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # We are pushing a tuple (head.value, head) into the heap.
    # Since Python natively compares tuples element-wise, it first compares head.value (which is an integer).
    # If there is a tie (two nodes with the same value), Python attempts to compare the second element: head, which is an instance of SLLNode.
    # Because SLLNode does not define < or <=, Python raises the error.
    # Hence we need this.
    def __eq__(self, node):
        if not isinstance(node, SLLNode):
            return False
        return self.value == node.value


def merge_k_sorted_lists(list):
    min_heap = []
    for head in list:
        if head:
            heapq.heappush(min_heap, (head.value, head))

    dummy = SLLNode("DUMMY")
    cur = dummy
    while min_heap:
        _, node = heapq.heappop(min_heap)
        cur.next = node
        cur = cur.next

        if node.next:
            node = node.next
            heapq.heappush(min_heap, (node.value, node))

    return dummy.next


# --------------------------------------------------------------- #

# * Variation 1: Input is a nested array of integers
"""
Input:
nums = [
    [3, 5, 6, 9]
    [1, 2, 3]
    [6]
]

Output:
[1, 2, 3, 3, 5, 6, 6, 9]
"""


def merge_k_sorted_arrays(nums):
    res, min_heap = [], []

    for row in range(len(nums)):
        heapq.heappush(min_heap, (nums[row][0], row, 0))

    while min_heap:
        value, row, col = heapq.heappop(min_heap)
        res.append(value)
        if col + 1 < len(nums[row]):
            heapq.heappush(min_heap, (nums[row][col + 1], row, col + 1))

    return res


# --------------------------------------------------------------- #

# * Variation 2: Implement MergeKIterator class


class MergeKIterator:
    def __init__(self, nums):
        self.nums, self.min_heap = nums, []

        for row in range(len(nums)):
            if nums[row]:
                heapq.heappush(self.min_heap, (nums[row][0], row, 0))

    def has_next(self):
        return len(self.min_heap) > 0

    def next(self):
        if not self.has_next():
            raise Exception("No next element available")

        value, row, col = heapq.heappop(self.min_heap)
        if col + 1 < len(self.nums[row]):
            heapq.heappush(self.min_heap, (self.nums[row][col + 1], row, col + 1))

        return value


class TestMergeKSortedLists(unittest.TestCase):
    def linked_list_to_list(self, head):
        """Helper function to convert a linked list to a Python list for easy comparison."""
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

    def test_empty_list(self):
        """Test merging an empty list of lists."""
        self.assertIsNone(merge_k_sorted_lists([]))

    def test_all_none_lists(self):
        """Test merging a list of None values."""
        self.assertIsNone(merge_k_sorted_lists([None, None, None]))

    def test_single_list(self):
        """Test merging a single non-empty linked list."""
        sll1 = SLLNode(1)
        sll1.next = SLLNode(3)
        sll1.next.next = SLLNode(5)

        merged = merge_k_sorted_lists([sll1])
        self.assertEqual(self.linked_list_to_list(merged), [1, 3, 5])

    def test_multiple_empty_lists(self):
        """Test merging multiple empty lists."""
        self.assertIsNone(merge_k_sorted_lists([None, None]))

    def test_merge_two_lists(self):
        """Test merging two sorted linked lists."""
        sll1 = SLLNode(1)
        sll1.next = SLLNode(4)
        sll1.next.next = SLLNode(5)

        sll2 = SLLNode(2)
        sll2.next = SLLNode(3)
        sll2.next.next = SLLNode(6)

        merged = merge_k_sorted_lists([sll1, sll2])
        self.assertEqual(self.linked_list_to_list(merged), [1, 2, 3, 4, 5, 6])

    def test_merge_k_lists_generic(self):
        """Test merging multiple sorted linked lists."""
        sll1 = SLLNode(1)
        sll1.next = SLLNode(4)
        sll1.next.next = SLLNode(5)

        sll2 = SLLNode(1)
        sll2.next = SLLNode(3)
        sll2.next.next = SLLNode(4)

        sll3 = SLLNode(2)
        sll3.next = SLLNode(6)

        merged = merge_k_sorted_lists([sll1, sll2, sll3])
        self.assertEqual(self.linked_list_to_list(merged), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_merge_with_null_middle_list(self):
        """Test merging lists where a null list is present between valid lists."""
        sll1 = SLLNode(2)
        sll1.next = SLLNode(4)

        sll2 = None

        sll3 = SLLNode(3)
        sll3.next = SLLNode(5)

        merged = merge_k_sorted_lists([sll1, sll2, sll3])
        self.assertEqual(self.linked_list_to_list(merged), [2, 3, 4, 5])

    def test_merge_single_node_lists(self):
        """Test merging multiple single-node linked lists."""
        lists = [SLLNode(5), SLLNode(3), SLLNode(8), SLLNode(1)]
        merged = merge_k_sorted_lists(lists)
        self.assertEqual(self.linked_list_to_list(merged), [1, 3, 5, 8])


class TestMergeKSortedArrays(unittest.TestCase):
    def test_merge_k_sorted_arrays(self):
        self.assertListEqual(
            merge_k_sorted_arrays([[3, 5, 6, 9], [1, 2, 3], [6]]),
            [1, 2, 3, 3, 5, 6, 6, 9],
        )


class TestMergeKIterator(unittest.TestCase):
    def test_multiple_lists(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        it = MergeKIterator(lists)
        result = []
        while it.has_next():
            result.append(it.next())
        self.assertEqual(result, [1, 1, 2, 3, 4, 4, 5, 6])

    def test_single_list(self):
        lists = [[1, 2, 3]]
        it = MergeKIterator(lists)
        self.assertTrue(it.has_next())
        self.assertEqual(it.next(), 1)
        self.assertTrue(it.has_next())
        self.assertEqual(it.next(), 2)
        self.assertTrue(it.has_next())
        self.assertEqual(it.next(), 3)
        self.assertFalse(it.has_next())

    def test_empty_lists(self):
        lists = [[], [1, 2, 3], []]
        it = MergeKIterator(lists)
        result = []
        while it.has_next():
            result.append(it.next())
        self.assertEqual(result, [1, 2, 3])

    def test_all_empty(self):
        lists = [[], [], []]
        it = MergeKIterator(lists)
        self.assertFalse(it.has_next())
        with self.assertRaises(Exception):
            it.next()  # should raise an exception because there's no element

    def test_next_beyond_end(self):
        lists = [[1]]
        it = MergeKIterator(lists)
        self.assertTrue(it.has_next())
        self.assertEqual(it.next(), 1)
        self.assertFalse(it.has_next())
        # Attempting to call next() beyond the end should raise an Exception
        with self.assertRaises(Exception):
            it.next()


if __name__ == "__main__":
    unittest.main()
