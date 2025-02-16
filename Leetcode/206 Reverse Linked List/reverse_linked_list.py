import unittest


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n), where n => number of nodes in sll
# Space: O(1)
def reverse_linked_list_iterative(head):
    prev, cur = None, head

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list_iterative(self):
        self.assertEqual(reverse_linked_list_iterative(None), None)

        head = SLLNode(2)
        head.next = SLLNode(6)
        expected_head = head.next.next = SLLNode(9)

        self.assertEqual(reverse_linked_list_iterative(head), expected_head)


if __name__ == "__main__":
    unittest.main()
