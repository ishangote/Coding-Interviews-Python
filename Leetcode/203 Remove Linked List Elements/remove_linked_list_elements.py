import unittest


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n), where n => number of nodes in linked list
# Space: O(1)
def remove_linked_list_elements(head, target):
    dummy = SLLNode("DUMMY")
    dummy.next = head

    prev = dummy
    current = head

    while current:
        if current.value != target:
            prev = current
            current = current.next

        else:
            prev.next = current.next
            current = current.next

    return dummy.next


class TestRemoveLinkedListElements(unittest.TestCase):
    def test_remove_linked_list_elements_edge(self):
        self.assertEqual(remove_linked_list_elements(None, 1), None)

        head = SLLNode(1)
        self.assertEqual(remove_linked_list_elements(head, 1), None)

    def test_remove_linked_list_elements(self):
        head = SLLNode(1)
        expected_result = head.next = SLLNode(2)
        head.next.next = SLLNode(1)
        head.next.next.next = SLLNode(1)
        head.next.next.next.next = SLLNode(3)
        head.next.next.next.next.next = SLLNode(1)

        self.assertEqual(remove_linked_list_elements(head, 1), expected_result)


if __name__ == "__main__":
    unittest.main()
