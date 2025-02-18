import unittest


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# ------------------------------------------ #


# Time: O(n + n) ~ O(n), where n => number of nodes in SLL
# Space: O(1)
def remove_nth_from_end_two_pass(head, n):
    dummy = SLLNode("DUMMY")
    dummy.next = head
    length, cur = 0, head

    # First pass: Get the length of the list
    while cur:
        length += 1
        cur = cur.next

    # Find the node before the one to be removed
    cur = dummy
    for _ in range(length - n):
        cur = cur.next

    # Remove the nth node
    cur.next = cur.next.next

    return dummy.next


# ------------------------------------------ #


# Time: O(n), where n => number of nodes in SLL
# Space: O(1)
def remove_nth_from_end_one_pass(head, n):
    if not head:
        return None

    fast = slow = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head


# ------------------------------------------ #


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def linked_list_to_list(self, head):
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

    def create_linked_list(self, values):
        if not values:
            return None
        head = SLLNode(values[0])
        current = head
        for val in values[1:]:
            current.next = SLLNode(val)
            current = current.next
        return head

    # ------------------------------------------ #

    def test_remove_nth_from_end_one_pass(self):
        # Case 1: Single Node List (Removing the only node)
        head = self.create_linked_list([1])
        self.assertIsNone(remove_nth_from_end_one_pass(head, 1))

        # Case 2: Remove last node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_one_pass(head, 1)),
            [1, 2, 3, 4],
        )

        # Case 3: Remove a middle node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_one_pass(head, 3)),
            [1, 2, 4, 5],
        )

        # Case 4: Remove the first node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_one_pass(head, 5)),
            [2, 3, 4, 5],
        )

    def test_remove_nth_from_end_two_pass(self):
        # Case 1: Single Node List (Removing the only node)
        head = self.create_linked_list([1])
        self.assertIsNone(remove_nth_from_end_two_pass(head, 1))

        # Case 2: Remove last node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_two_pass(head, 1)),
            [1, 2, 3, 4],
        )

        # Case 3: Remove a middle node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_two_pass(head, 3)),
            [1, 2, 4, 5],
        )

        # Case 4: Remove the first node
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertListEqual(
            self.linked_list_to_list(remove_nth_from_end_two_pass(head, 5)),
            [2, 3, 4, 5],
        )


if __name__ == "__main__":
    unittest.main()
