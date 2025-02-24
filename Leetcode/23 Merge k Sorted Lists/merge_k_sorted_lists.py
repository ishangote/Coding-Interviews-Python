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


if __name__ == "__main__":
    unittest.main()
